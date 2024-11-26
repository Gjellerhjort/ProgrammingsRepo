from simulation.cooling_room import CoolingRoom, Food, Compressor, Door
from simulation.data_loader import DataLoader
from simulation.simulation import CoolerSimulation
from thermostat.simple_thermostat import SimpleThermostat

def main():
    loader = DataLoader()
    loader.load_data("./data/elpris.csv")

    # Get prices as a pandas Series
    price_data = loader.get_prices()

    # Create instances of Compressor and CoolingRoom with price data
    compressor = Compressor(electric_prices=price_data)
    cooling_room = CoolingRoom(compressor=compressor, thermostat=SimpleThermostat, food=Food, door=Door, price_data=price_data)
    simulation = CoolerSimulation(cooling_room)
    simulation.run_simulation(100)


if __name__ == "__main__":
    main()