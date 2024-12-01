from abc import ABC, abstractmethod
from simulation.cooling_room import CoolingRoom
class Thermostat(ABC):
    """
    This is Base Thermostat class for managing temperature control
    """
    def __init__(self):
        """
        Initialize the thermostat with a target temperature. 
        """
        self.cooling_room: CoolingRoom | None = None


    def register(self, room: "CoolingRoom") -> None:
        """
        Register the thermostat in the room
        :param room: CoolingRoom to register the thermostat
        :return: None
        """
        assert isinstance(
            room, CoolingRoom
        ), "The thermostat can only be registered in a CoolingRoom"
        self.cooling_room = room

    @abstractmethod
    def compressor_decide(self, current_temp):
        """
        This function decides whether the compressor should be on or off
        :param current_temp: Current room temperature
        :return: Bool if True then turn on and False then turn off 
        """
        raise NotImplementedError("This method should be overridden by subclasses to decide state of compressor")