from .thermostat import Thermostat
import pandas as pd

class SmartThermostat(Thermostat):
    def __init__(self) -> None:
        super().__init__()
    """
    A Smart thermostat that turns the compressor on/off based on temperature target.
    """
    def compressor_decide(self, interval: int) -> bool:
        """
        This function decides whether the compressor should be on or off based on current temp
        :param interval 
        :return: Bool if True then turn on and False then turn off 
        """
        # Get the current price and temperature
        price = float(self.cooling_room.price_data.iloc[interval])
        current_temp = self.cooling_room.temperature

        price_threshold = 2  # Adjust this threshold based on desired behavior
        temperature_threshold = 6  # Critical temperature threshold
        lowest_temp = 3.5 # Critical Low temperature threshold
        
        if current_temp >= temperature_threshold or price < price_threshold and current_temp > lowest_temp:
            return True  # Turn compressor on
        else:
            return False  # Turn compressor off