from simulation.cooling_room import CoolingRoom, Food
from simulation.data_loader import DataLoader
from simulation.cooler_simulation import CoolerSimulation
from simulation.monte_carlo import MonteCarloSim
from plotter.harry_plotter import SimulationPlotter
from thermostat.simple_thermostat import SimpleThermostat
from thermostat.smart_thermostat import SmartThermostat
def main():
    sim = MonteCarloSim()
    plotter = SimulationPlotter()
    sim_data = sim.run_simulation(SmartThermostat(), 100)
    plotter.plot_diffrent_costs_over_time(sim_data)
    plotter.plot_tempature_over_time(sim_data)
    plotter.plot_total_cost_over_time(sim_data)


if __name__ == "__main__":
    main()