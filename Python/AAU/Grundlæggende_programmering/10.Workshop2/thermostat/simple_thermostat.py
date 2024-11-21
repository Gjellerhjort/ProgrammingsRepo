from .thermostat import Thermostat

class SimpleThermostat(Thermostat):
    """
    A simple thermostat that turns the compressor on/off based on temperature target.
    """
    def compressor_decide(self, current_temp):
        """
        This function decides whether the compressor should be on or off based on current temp
        :param current_temp: Current room temperature
        :return: Bool if True then turn on and False then turn off 
        """
        return current_temp > self.target_temp