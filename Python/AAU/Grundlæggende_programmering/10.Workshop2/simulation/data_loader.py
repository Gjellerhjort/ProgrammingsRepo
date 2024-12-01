import pandas as pd

class DataLoader:
    def __init__(self) -> None:
        self.data = pd.DataFrame()  # This will store the entire CSV as a DataFrame.
        self.row_count = 0

    def load_data(self, file_path: str) -> None:
        try:
            # Load the data using pandas
            self.data = pd.read_csv(file_path, parse_dates=["Tid"])  # Ensure 'Tid' is parsed as datetime
            self.row_count = len(self.data)  # Number of rows in the DataFrame
            
            print(f"Loaded {self.row_count} rows of data.")

        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_prices(self) -> pd.Series:
        """
        Retrieve a pandas Series of all price values.
        """
        return self.data["Pris"]

    def get_price_at_row(self, row_number: int) -> float:
        """
        Gets the price in a specific row by index.
        :param row_number: The row index.
        :return: Price as a float.
        """
        try:
            return float(self.data.iloc[row_number]["Pris"])
        except IndexError:
            print(f"Error: Row {row_number} is out of bounds.")
            return None
