    
class CoolerSimulation:
    """
    Simulates the cooler room dynamics and thermostat
    """
    def __init__(self, thermostat, price_data, door_probability=0.1) -> None:
        self.thermostat = thermostat
        self.price_data = price_data
        self.door_probability = door_probability # the probability that door is open
        self.temperature = 5  # start temperature of T[0]
        self.room_temperature = 20 # The temperature outside the cooler
        self.C1_closed = 5e-7  # Rate of temperature loss when door closed
        self.C1_open = 3e-5 # Rate of temperature loss when door open
        self.C2 = 8e-6  # Cooling rate when compressor is on
        self.compressor_cooling_temperature = -5
        self.compressor_power_usage = 1 # this is measured in watt
        self.target_temp = 5

    def run(self, intervals: int):
        """
        Run the simulations for a number of intervals with is T[n].
        :param intervals: Total number of 5-minute intervals
        """
        compressor_on = False
        total_watt = 0
        power_price = 3.65
        for n in range(intervals):

            door_open = self.random_door_event(self.door_probability)
            self.temperature = self.calculate_temperature(door_open, compressor_on)

            compressor_on = self.thermostat.compressor_decide(self, self.temperature)
            if compressor_on:
                total_watt += power_price * self.compressor_power_usage
            print(f"Interval {n}, Temp: {self.temperature}, Compressor: {compressor_on}, Price {total_watt}")

    def calculate_temperature(self, door_open: bool, compressor_on: bool):
        """
        Update temperature based on whether the door is open and if the compressor is on or off.
        The calculation follows the equation:
            T[n] = T[n - 1] + (C1(T_room - T[n - 1]) + C2(T_compressor - T[n - 1])) * ∆t

        Parameters
        ----------
        door_open : bool
            Whether the door is open (True) or closed (False).

        compressor_on : bool
            Whether the compressor is running (True) or off (False).

        Returns
        -------
        float
            The updated temperature T[n].

        """
        delta_t: int = 300 # time 
        
        # Door effect: Use different rates depending on whether the door is open or closed
        C1_effect = self.C1_open if door_open else self.C1_closed
        door_temperature_effect =  C1_effect*(self.room_temperature - self.temperature)
        #print(f"Door temperature effect: {door_temperature_effect}")
        
        compressor_temperature_effect =  self.C2*(self.compressor_cooling_temperature - self.temperature) if compressor_on else 0
        #print(f"Compressor temperature effect: {compressor_temperature_effect}")

        
        # calculate the new temp
        return self.temperature + (compressor_temperature_effect + door_temperature_effect)* delta_t
    
    @staticmethod
    def random_door_event(probability) -> bool: 
        import random
        return random.random() < probability
    
if __name__ == "__main__":
    import sys
    sys.path.append('..') 
    from thermostat.simple_thermostat import Simple_thermostat
    sim1 = CoolerSimulation(Simple_thermostat, None)
    sim1.run(100)
    #temp = sim1.calculate_temperature(False, True)
    #print(f"The new temperature is: {temp}°C")