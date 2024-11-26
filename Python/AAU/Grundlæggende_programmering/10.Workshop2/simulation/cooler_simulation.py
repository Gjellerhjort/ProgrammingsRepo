import random
from math import exp
from data_loader import DataLoader


class Food:
    def __init__(self) -> None:
        self.losses = 0.0

    def deteriorate(self, temp: float, delta_t: int = 300) -> None:
        """
        Deteriorate the food based on the temperature.
        
        Parameters:
        - temp: float - The current temperature in the cooling room.
        - delta_t: int - The amount of time passed since the last update (in seconds).
        """
        if 3.5 <= temp < 6.5:
            # No deterioration between 3.5 and 6.5 degrees.
            return

        if temp < 3.5:
            self.losses += (4.39 * exp(-0.49 * temp) / 300) * delta_t
        elif temp >= 6.5:
            self.losses += (0.11 * exp(0.31 * temp) / 300) * delta_t


class CoolerSimulation:
    """
    Simulates the cooler room dynamics and thermostat behavior.
    """

    def __init__(
        self, 
        thermostat, 
        food: Food, 
        price_data, 
        door_probability: float = 0.1
    ) -> None:
        self.thermostat = thermostat
        self.food = food
        self.price_data = price_data
        self.door_probability = door_probability  # Probability that the door is open.
        self.temperature = 5.0  # Starting temperature of T[0].
        self.room_temperature = 20.0  # The temperature outside the cooler.
        self.C1_closed = 5e-7  # Heat transfer rate when the door is closed.
        self.C1_open = 3e-5  # Heat transfer rate when the door is open.
        self.C2 = 8e-6  # Cooling rate when the compressor is on.
        self.compressor_cooling_temperature = -5.0  # Compressor cooling temperature.
        self.compressor_power_usage = 1.0  # Power usage in watts.
        self.target_temp = 8.0  # Target temperature.

    def run(self, intervals: int) -> None:
        """
        Run the simulation for a specified number of intervals.
        
        Parameters:
        - intervals: int - Total number of 5-minute intervals.
        """
        compressor_on = False
        total_watt = 0.0
        power_price = 3.65
        loader = DataLoader()
        loader.load_data("../data/elpris.csv")
        for n in range(loader.row_count):
            power_price = loader.get_price_at_row(n)
            door_open = self.random_door_event(self.door_probability)
            self.temperature = self.calculate_temperature(door_open, compressor_on)

            compressor_on = self.thermostat.compressor_decide(self.temperature)
            if compressor_on:
                total_watt += power_price * self.compressor_power_usage

            self.food.deteriorate(self.temperature)

            total_price = total_watt + self.food.losses
            print(f"Interval {n}, Temp: {self.temperature:.2f}°C, Compressor: {compressor_on}, "
                  f"Power Cost: {total_watt:.2f}, Total Price: {total_price:.2f}")

    def calculate_temperature(self, door_open: bool, compressor_on: bool) -> float:
        """
        Update the temperature based on door status and compressor activity.
        
        Parameters:
        - door_open: bool - Whether the door is open.
        - compressor_on: bool - Whether the compressor is running.

        Returns:
        - float - The updated temperature.
        """
        delta_t = 300  # Time step in seconds.

        # Door effect: Different rates depending on door state.
        C1_effect = self.C1_open if door_open else self.C1_closed
        door_temperature_effect = C1_effect * (self.room_temperature - self.temperature)

        # Compressor effect: Only applies if the compressor is on.
        compressor_temperature_effect = (
            self.C2 * (self.compressor_cooling_temperature - self.temperature) if compressor_on else 0.0
        )

        # Update temperature.
        return self.temperature + (door_temperature_effect + compressor_temperature_effect) * delta_t

    @staticmethod
    def random_door_event(probability: float) -> bool:
        """
        Determine if the door opens based on probability.
        
        Parameters:
        - probability: float - The likelihood of the door being open.

        Returns:
        - bool - True if the door is open, False otherwise.
        """
        return random.random() < probability


if __name__ == "__main__":
    import sys
    sys.path.append('..') 
    from thermostat.simple_thermostat import SimpleThermostat

    sim = CoolerSimulation(
        thermostat=SimpleThermostat(5),
        food=Food(),
        price_data=None
    )
    sim.run(1000)
