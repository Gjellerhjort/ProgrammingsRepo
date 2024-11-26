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

    def run_simulation(self, intervals: int) -> None:
        """
        Run the simulation for a specified number of intervals.

        Parameters:
        ----------
        intervals : int
            Total number of 5-minute intervals.
        """
        print("Starting Cooler Simulation...")
        for n in range(intervals):
            self.cooling_room.run(n)

if __name__ == "__main__":
    import sys
    sys.path.append('..') 
    import pandas as pd
    from thermostat.simple_thermostat import SimpleThermostat
    from cooling_room import CoolingRoom, Compressor, Food, Door
    from data_loader import DataLoader
    # Create the necessary objects.
    loader = DataLoader()
    loader.load_data("../data/elpris.csv")

    # Get prices as a pandas Series
    price_data = loader.get_prices()

    # Create instances of Compressor and CoolingRoom with price data
    compressor = Compressor(electric_prices=price_data)
    cooling_room = CoolingRoom(compressor=compressor, thermostat=SimpleThermostat, food=Food, door=Door, price_data=price_data)
    simulation = CoolerSimulation(cooling_room)
    simulation.run_simulation(100)