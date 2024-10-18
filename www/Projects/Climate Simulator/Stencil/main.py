import policies
from display import Display
from simulator import Simulator

if __name__ == '__main__':
    # Create a simulator object
    sim = Simulator()

    # Add countries to the simulator
    sim.add_country('United States', policies.Baseline(6.5), 10)
    sim.add_country('China', policies.TaxEmissions(14, 0.05), 8)
    sim.add_country('Colombia', policies.Deforestation(0.07, 50, 0.03), 24)
    sim.add_country('Libya', policies.MatchLowest(0.06), 23)
    sim.add_country('United Kingdom', policies.Reducing(4.5, 0.5), 9)    

    # Create a display object and run the simulation
    display = Display(sim)

    # Run the simulation
    display.run()
