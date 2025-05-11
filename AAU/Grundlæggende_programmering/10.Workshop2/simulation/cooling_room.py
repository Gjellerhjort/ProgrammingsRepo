import random
import pandas as pd
import numpy as np

class Food:
    def __init__(self) -> None:
        self.food_losses = 0.0  # Initialize food losses.

    def deteriorate(self, temp: float, delta_t: int = 300) -> None:
        """
        Update the food losses based on the current temperature and time interval.

        This method calculates the deterioration of food over a time interval (`delta_t`)
        based on the temperature (`temp`). The rate of deterioration depends on whether 
        the temperature is below 3.5°C, between 3.5°C and 6.5°C, or above 6.5°C.

        Args:
            temp (float): The current temperature in degrees Celsius.
            delta_t (int, optional): The time interval over which deterioration occurs, 
                                     in seconds. Default is 300 seconds (5 minutes).

        Example:
            >>> import numpy as np
            >>> food = Food()
            >>> food.deteriorate(2.0, delta_t=600)
            >>> round(food.food_losses, 4)
            np.float64(3.2952)

            >>> food.deteriorate(7.0, delta_t=600)
            >>> round(food.food_losses, 4)
            np.float64(5.2221)

            >>> food.deteriorate(4.0, delta_t=600)
            >>> food.food_losses
            np.float64(5.222053936878272)
        """
        if 3.5 <= temp < 6.5:
            return
        if temp < 3.5:
            self.food_losses += (4.39 * np.exp(-0.49 * temp) / 300) * delta_t
            return
        if temp >= 6.5:
            self.food_losses += (0.11 * np.exp(0.31 * temp) / 300) * delta_t

class CoolingRoom:
    """
    Simulates the cooler room dynamics and thermostat behavior.
    """

    def __init__(
        self,
        thermostat: "Thermostat",
        food: Food,
        price_data: pd.Series,
        door_probability: float = 0.1,
    ) -> None:
        """
        Initialize the CoolingRoom simulation.

        Parameters:
        ----------
        thermostat : Thermostat
            The thermostat to control the compressor.

        food : Food
            The food class to monitor deterioration.

        price_data : pd.Series
            Series of electricity prices.
        """
        self.thermostat = thermostat
        self.thermostat.register(self)
        self.food = food
        self.price_data = price_data
        self.door_probability = door_probability
        self.temperature = 5.0  # Start temperature of T[0].
        self.room_temperature = 20.0  # The temperature outside the cooler.
        self.C1_closed = 5e-7  # Rate of temperature loss when the door is closed.
        self.C1_open = 3e-5  # Rate of temperature loss when the door is open.
        self.C2 = 8e-6  # Cooling rate when the compressor is on.
        self.compressor_cooling_temperature = -5.0
        self.power_cost = 0.0
        self.target_temp = 5.0
        self.door_open: bool = False

    def get_total_cost(self) -> float:
        return self.power_cost + self.food.food_losses

    def run(self, interval: int) -> None:
        """
        Run the simulation for a specified number of intervals.

        Parameters:
        ----------
        intervals : int
            Total number of 5-minute intervals.
        """
        #print(self.power_cost)

        self.door_open = self.random_door_event(self.door_probability)

        self.compressor_on = self.thermostat.compressor_decide(interval)
        self.calculate_temperature()
        self.electricity_cost(interval)

        self.food.deteriorate(self.temperature)

        """
        print(
            f"Interval {interval + 1}, Temp: {self.temperature:.2f}°C, "
            f"Compressor: {'On' if self.compressor_on else 'Off'}, "
            f"Door: {'Open' if self.door_open else 'Closed'}, "
            f"Total Cost: {self.power_cost:.2f}"
        )
        """

    def calculate_temperature(self, delta_t: int = 300) -> None:
        """
        Update temperature based on whether the door is open and if the compressor is on.

        Parameters:
        ----------
        door_open : bool
            Whether the door is open.

        compressor_on : bool
            Whether the compressor is on.
        """
        # Door effect: Different rates depending on door state.
        C1_effect = self.C1_open if self.door_open else self.C1_closed
        door_temperature_effect = C1_effect * (self.room_temperature - self.temperature)

        # Compressor effect: Only applies if the compressor is on.
        compressor_temperature_effect = (
            self.C2 * (self.compressor_cooling_temperature - self.temperature)
            if self.compressor_on
            else 0.0
        )

        # Update temperature.
        self.temperature += (door_temperature_effect + compressor_temperature_effect) * delta_t

    def electricity_cost(self, interval: int) -> None:
        """
        Consume electricity and update the total cost, if the compressor is on.
        :param i: The current iteration step (index in the electric prices series).
        """
        if self.compressor_on:
            try:
                price = float(self.price_data.iloc[interval])
                self.power_cost += price
            except IndexError:
                print(f"Error: Index {interval} is out of bounds in the electric price series.")
            except ValueError:
                print(f"Error: Invalid price data at index {interval}.")


    @staticmethod
    def random_door_event(probability: float) -> bool:
        """
        Determine if the door is open based on the given probability.

        Parameters:
        ----------
        probability : float
            The likelihood of the door being open.

        Returns:
        -------
        bool
            True if the door is open, False otherwise.
        """
        return random.random() < probability


if __name__ == "__main__":
    print("test")
    import doctest
    doctest.testmod()