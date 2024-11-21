from abc import ABC, abstractmethod

class Thermostat(ABC):
    """
    This is Base Thermostat class for managing temperature control
    """
    def __init__(self, target_temp=5):
        """
        Initialize the thermostat with a target temperature. 
        """
        self.target_temp = target_temp
    @abstractmethod
    def compressor_decide(self, current_temp):
        """
        This function decides whether the compressor should be on or off
        :param current_temp: Current room temperature
        :return: Bool if True then turn on and False then turn off 
        """
        raise NotImplementedError("This method should be overridden by subclasses to decide state of compressor")