import pandas as pd
import numpy as np
from .cooling_room import CoolingRoom

class CoolerSimulation:
    """
    Simulates the cooler room dynamics and thermostat behavior.
    """

    def __init__(self, cooling_room: CoolingRoom) -> None:
        """
        Initialize the CoolerSimulation with a CoolingRoom instance.

        Parameters:
        ----------
        cooling_room : CoolingRoom
            An instance of the CoolingRoom class to simulate.
        """
        self.cooling_room = cooling_room

    def run_simulation(self, intervals: int = 8641) -> pd.DataFrame:
        """
        Run the simulation for a specified number of intervals.

        Parameters:
        ----------
        intervals : int
            Total number of 5-minute intervals.
        """
        # Pre-allocate NumPy arrays for all metrics
        temperature = np.zeros(intervals)
        compressor_on = np.zeros(intervals, dtype=bool)  # True for 'On', False for 'Off'
        door_open = np.zeros(intervals, dtype=bool)  # True for 'Open', False for 'Closed'
        food_losses = np.zeros(intervals)
        power_cost = np.zeros(intervals)
        total_cost = np.zeros(intervals)

        for interval in range(intervals):
            self.cooling_room.run(interval)

            temperature[interval] = self.cooling_room.temperature
            compressor_on[interval] = self.cooling_room.compressor_on
            door_open[interval] = self.cooling_room.door_open
            food_losses[interval] = self.cooling_room.food.food_losses
            power_cost[interval] = self.cooling_room.power_cost
            total_cost[interval] = self.cooling_room.get_total_cost()

        data = {
            "Temperature (°C)": temperature,
            "Compressor State": compressor_on,
            "Door State": door_open,
            "Food Losses": food_losses,
            "Power Cost": power_cost,
            "Total Cost": total_cost,
        }

        df = pd.DataFrame(data)
        return df 

if __name__ == "__main__":
    import sys
    sys.path.append('..') 
    import pandas as pd
    from thermostat.simple_thermostat import SimpleThermostat
    from cooling_room import CoolingRoom, Food
    from data_loader import DataLoader
    # Create the necessary objects.
    loader = DataLoader()
    loader.load_data("../data/elpris.csv")

    # Get prices as a pandas Series
    price_data = loader.get_prices()

    # Create instances of Compressor and CoolingRoom with price data

    cooling_room = CoolingRoom(thermostat=SimpleThermostat, food=Food, price_data=price_data)
    simulation = CoolerSimulation(cooling_room)
    simulation.run_simulation(100)