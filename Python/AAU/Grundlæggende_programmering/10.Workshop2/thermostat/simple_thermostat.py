from .thermostat import Thermostat

class SimpleThermostat(Thermostat):
    def __init__(self, target_temp: int = 5) -> None:
        super().__init__()
        self.target_temp = target_temp
    """
    A simple thermostat that turns the compressor on/off based on temperature target.
    """
    def compressor_decide(self, interval: int) -> bool:
        """
        This function decides whether the compressor should be on or off based on current temp
        :param current_temp: Current room temperature
        :return: Bool if True then turn on and False then turn off 
        """
        return self.cooling_room.temperature > self.target_temp