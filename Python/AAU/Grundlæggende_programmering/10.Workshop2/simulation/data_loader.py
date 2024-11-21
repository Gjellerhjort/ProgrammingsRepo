import csv
from datetime import datetime

class DataLoader:
    def __init__(self) -> None:
        self.data = []
        self.row_count = 0

    def load_data(self, file_path: str):
        try:
            # Count the number of rows
            with open(file_path, mode='r', encoding='utf-8') as count_file:
                self.row_index = sum(1 for _ in count_file) - 1  # Subtract 1 for the header

            # Load the data
            with open(file_path, mode='r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                self.data = [
                    {"time": datetime.strptime(row["Tid"], "%Y-%m-%d %H:%M:%S"), 
                    "price": float(row["Pris"])}
                    for row in reader
                ]
            
            print(f"Loaded {self.row_index} rows of data.")


        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_prices(self):
        """
        Retrieve a list of all price values.

        Returns
        -------
        list[float]
            A list of prices.
        """
        return [entry["price"] for entry in self.data]

    def get_price_at_row(self, row_number: int) -> float:
        """
        gets price in certain row

        Parameters
        ----------
        row_number : int 
            Input value.

        Returns
        -------
        price : float
            Output value 
            
        """
        if self.row_count < 0 or self.row_count >= len(self.data):
           raise IndexError("Row index is out of range.")

        return self.data[row_number]['price']
    

if __name__ == "__main__":
    loader = DataLoader()
    loader.load_data("../data/elpris.csv")
    print(loader.get_price_at_row(0))