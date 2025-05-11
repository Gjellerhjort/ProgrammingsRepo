from .cooling_room import CoolingRoom, Food
from .data_loader import DataLoader
from .cooler_simulation import CoolerSimulation
import pandas as pd

class MonteCarloSim:
    def __init__(self) -> None:
        self.price_loader = DataLoader()
        

    def run_simulation(self, thermostat, samples: int) -> pd.Series:
        self.price_loader.load_data("./data/elpris.csv")

        # Get prices as a pandas Series
        price_data = self.price_loader.get_prices()

        # stores all the simulation results
        all_data = []

        for _ in range(samples):
            # Reset the cooling room for each sample 
            cooling_room = CoolingRoom(
                thermostat=thermostat, 
                food=Food(), 
                price_data=price_data
            )
            
            simulation = CoolerSimulation(cooling_room)
            
            # Runs the simulation and store the result
            sample_data = simulation.run_simulation()
            # adds new data to all_data list
            all_data.append(sample_data)

        # Calculate the average of all samples
        all_data_df = pd.concat(all_data, axis=0)
        average_data_df = all_data_df.groupby(all_data_df.index).mean()

        #print(average_data_df)
        
        return average_data_df