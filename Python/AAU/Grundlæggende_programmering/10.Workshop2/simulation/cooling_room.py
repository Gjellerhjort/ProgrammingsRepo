import random
import pandas as pd


class Door:
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


class Food:
    def __init__(self) -> None:
        self.losses = 0.0  # Initialize food losses as a floating-point number.


class Compressor:
    def __init__(
        self, temp: float = -5, is_on: bool = False, electric_prices: pd.Series = None
    ) -> None:
        self.temp = temp
        self.is_on = is_on
        self.cost = 0
        self._off_factor = 0
        self._on_factor = 8e-6
        self._electric_prices = electric_prices  # This should be a pandas Series.

    def consume_electricity(self, i: int) -> None:
        """
        Consume electricity and update the total cost, if the compressor is on.
        :param i: The current iteration step (index in the electric prices series).
        """
        if self.is_on:
            try:
                price = float(self._electric_prices.iloc[i])
                self.cost += price
            except IndexError:
                print(f"Error: Index {i} is out of bounds in the electric price series.")
            except ValueError:
                print(f"Error: Invalid price data at index {i}.")


    def consume_electricity(self, i: int) -> None:
        """
        Consume electricity and update the total cost if the compressor is on.

        Parameters:
        ----------
        i : int
            The current iteration step.

        Raises:
        ------
        ValueError
            If electricity prices are not set.
        """
        if self._electric_prices is None:
            raise ValueError("Electric prices not set")

        if self.is_on:
            self.cost += float(self._electric_prices.iloc[i])

    @property
    def temp_factor(self) -> float:
        """
        Return the cooling factor based on whether the compressor is on or off.

        Returns:
        -------
        float
            The cooling factor.
        """
        return self._on_factor if self.is_on else self._off_factor


class CoolingRoom:
    """
    Simulates the cooler room dynamics and thermostat behavior.
    """

    def __init__(
        self,
        compressor: Compressor,
        thermostat: "Thermostat",
        food: Food,
        door: Door,
        price_data: pd.Series,
        door_probability: float = 0.1,
    ) -> None:
        """
        Initialize the CoolingRoom simulation.

        Parameters:
        ----------
        compressor : Compressor
            The compressor responsible for cooling.

        thermostat : Thermostat
            The thermostat to control the compressor.

        food : Food
            The food object to monitor deterioration.

        door : Door
            The door object to simulate door events.

        price_data : pd.Series
            Series of electricity prices.

        door_probability : float
            The probability that the door is open.
        """
        self.thermostat = thermostat
        self.compressor = compressor
        self.food = food
        self.door = door
        self.price_data = price_data
        self.door_probability = door_probability
        self.temperature = 5.0  # Start temperature of T[0].
        self.room_temperature = 20.0  # The temperature outside the cooler.
        self.C1_closed = 5e-7  # Rate of temperature loss when the door is closed.
        self.C1_open = 3e-5  # Rate of temperature loss when the door is open.
        self.C2 = 8e-6  # Cooling rate when the compressor is on.
        self.compressor_cooling_temperature = -5.0
        self.compressor_power_usage = 1.0  # This is measured in watts.
        self.target_temp = 5.0

    def run(self, interval: int) -> None:
        """
        Run the simulation for a specified number of intervals.

        Parameters:
        ----------
        intervals : int
            Total number of 5-minute intervals.
        """

        door_open = self.door.random_door_event(self.door_probability)
        self.calculate_temperature(door_open, self.compressor.is_on)

        self.compressor.is_on = self.thermostat.compressor_decide(self,self.temperature)
        self.compressor.consume_electricity(interval)

        print(
                f"Interval {interval}, Temp: {self.temperature:.2f}°C, "
                f"Compressor: {'On' if self.compressor.is_on else 'Off'}, "
                f"Total Cost: {self.compressor.cost:.2f}"
            )

    def calculate_temperature(self, door_open: bool, compressor_on: bool) -> float:
        """
        Update temperature based on whether the door is open and if the compressor is on.

        Parameters:
        ----------
        door_open : bool
            Whether the door is open.

        compressor_on : bool
            Whether the compressor is on.

        Returns:
        -------
        float
            The updated temperature.
        """
        delta_t = 300  # Time step in seconds.

        # Door effect: Different rates depending on door state.
        C1_effect = self.C1_open if door_open else self.C1_closed
        door_temperature_effect = C1_effect * (self.room_temperature - self.temperature)

        # Compressor effect: Only applies if the compressor is on.
        compressor_temperature_effect = (
            self.C2 * (self.compressor_cooling_temperature - self.temperature)
            if compressor_on
            else 0.0
        )

        # Update temperature.
        self.temperature = self.temperature + (door_temperature_effect + compressor_temperature_effect) * delta_t
