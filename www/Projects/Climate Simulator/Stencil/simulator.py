# Description: This file contains the Simulator class, which is responsible for managing the simulation

class Simulator:
    def __init__(self):
        self.time = 2010                     
        self.country_names = []
        self.country_policies = {}
        self.country_temperatures = {}
        self.initial_country_temps = {} 
    
        # Tracks the total global surface temperature increase (in Celcius) since 1850-1900
        # In 2010, the global surface temperature had increased by approx. 1 degree Celcius
        self.global_surface_temp_inc = 1
        
        # TODO: Fill in the following values
        self.max_temperature_inc = None 
        self.cumulative_co2_emissions = None 
        self.annual_co2_decrement = None 

        # Prior emissions by country in the past year        
        # In a real application, we might make this a separate class
        self.prior_emissions = {} 
                

    def add_country(self, name, policy, average_temp):
        """
        Add a country to the simulation. Note that there is no Country class; countries
        are entities managed entirely by the Simulator class. If the same country is
        added twice, the simulator will use the _second_ addition's parameters.
        """
        self.country_names.append(name)
        self.country_policies[name] = policy
        self.country_temperatures[name] = average_temp
        self.initial_country_temps[name] = average_temp

    def advance_year(self):
        """
        Advances the simulator by one year, updating all relevant information
        """
        self.time += 1

        # TODO: Implement this function
        pass

    def report(self):
        # TODO: Implement this function
        return [{'name' : 'United States', 'temperature' : 10},
                {'name' : 'Libya', 'temperature' : 24}]
