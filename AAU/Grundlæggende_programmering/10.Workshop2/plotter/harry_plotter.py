import matplotlib.pyplot as plt
import pandas as pd

class SimulationPlotter:
    def __init__(self) -> None:
        pass

    def _get_data_interval(self, data: pd.DataFrame, time: int) -> pd.DataFrame:
        if time > 0:
            return data.iloc[:time]
        else:
            raise ValueError("Time must be a positive integer.")

    def plot_total_cost_over_time(self, data: pd.DataFrame, time: int = 8640) -> None:
        """
        Plots the Total Cost over Time from the given DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame containing 'Time' and 'Total Cost' columns.
        """
        # Ensure 'Time' and 'Total Cost' columns exist
        if 'Total Cost' not in data.columns:
            raise ValueError("The provided DataFrame must include 'Total Cost' column.")
        
        # Extract 'Time' (first column) and 'Total Cost' (assumed column)
        total_cost_column = 'Total Cost'  # Adjust if needed

        filtered_data = self._get_data_interval(data, time)

        # Plot Total Cost over Time
        plt.figure(figsize=(10, 6))
        plt.plot(filtered_data.index, filtered_data[total_cost_column], label='Total Cost', color='blue')
        plt.title("Total Cost Over Time")
        plt.xlabel("Time")
        plt.ylabel("Total Cost")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_tempature_over_time(self, data: pd.DataFrame, time: int = 8640) -> None:
        # Plot Temperature over Time
        # Filter data for the specified time range
        filtered_data = self._get_data_interval(data, time)

        plt.figure(figsize=(10, 6))
        plt.plot(filtered_data.index, filtered_data['Temperature (°C)'], label='Temperature (°C)', color='red')
        plt.title("Temperature Over Time")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


    def plot_diffrent_costs_over_time(self, data: pd.DataFrame, time: int = 8640) -> None:
        filtered_data = self._get_data_interval(data, time)
         
        plt.figure(figsize=(10, 6))
        plt.plot(filtered_data.index, filtered_data['Food Losses'], label='Food Losses', color='green')
        plt.plot(filtered_data.index, filtered_data["Power Cost"], label="Power Cost", color="yellow")
        plt.title("Different costs over time")
        plt.xlabel("Time")
        plt.ylabel("Total Costs")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()