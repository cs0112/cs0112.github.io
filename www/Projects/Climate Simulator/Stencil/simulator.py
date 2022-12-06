class Simulator:
    def __init__(self):
        # Our simulation starts in year 2010
        self.time = 2010                     
        # Countries added so far (by name)
        self.country_names = []
        # Maps country names to their policy object
        self.country_policies = {}
        # Maps country names to their current temperature
        self.country_temperatures = {}
        # Maps country names to their initial temperature in year 0
        self.initial_country_temps = {}
    
        # Tracks the total global surface temperature increase (in Celcius) since 1850-1900
        # In 2010, the global surface temperature had increased by approx. 1 degree Celcius
        self.global_surface_temp_inc = 1
        
        # The global surface temperature increase should not go above this value
        self.max_temperature_inc = None # TODO: CHANGE THIS
        # Tracks total CO2 emissions over time
        self.cumulative_co2_emissions = None # TODO: CHANGE THIS
        # Amount by which atmospheric CO2 levels decrease per year
        self.annual_co2_decrement = None # TODO: CHANGE THIS

        ########################################
        # Simulator history, for use by policies
        # (In a real application, we might make this a separate class)
        
        # Prior emissions by country in the past year        
        self.prior_emissions = {} 
                
    def add_country(self, name, policy, average_temp):
        self.country_names.append(name)
        self.country_policies[name] = policy
        self.country_temperatures[name] = average_temp
        self.initial_country_temps[name] = average_temp

    def advance_year(self):
        """
        Advances the simulator by one year, updating all relevant information
        """
        # TODO: Fill in this method. Consider what helper functions you might use here.
        self.time += 1
        pass

    def report(self):
        # TODO: Modify this function to return a list of dictionaries, where each dictionary 
        # contains a particular country mapped to its current temperature. 
        return [{'name' : 'United States', 'temperature' : 10},
                {'name' : 'Libya', 'temperature' : 24}]
