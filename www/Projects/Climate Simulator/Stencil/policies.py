# Description: This file contains the Policy classes, which are responsible for managing the emissions policies of each country

class Baseline:
    """
    Emissions remain constant at ((baseline)).
    """
    def __init__(self, baseline):
        pass

    # TODO: add other necessary parameters
    def emit(self):
        pass

class Reducing:
    """
    Configurable version of the handout's policy. To use the default, provide 0.5 as the reduction.
    Emissions reduce by ((reduction_amount)) every year, starting from year 1. 
    Emissions cannot be reduced below 0.   
    """
    def __init__(self, baseline: float, reduction_amount: float):
        pass

    # TODO: add other necessary parameters
    def emit(self):        
        pass

class TaxEmissions:
    """
    Configurable version of the handout's policy. To use the default, provide a 0.05 factor.

    Emissions are multiplied by ((reduce_factor)) every year to yield 
    ((baseline))*((reduce_factor)), starting in year 1. In year 0, the emission amount is ((baseline)).
    Emissions cannot be reduced below zero.
    """
    def __init__(self, baseline: float, reduce_factor: float):
        pass

    # TODO: add other necessary parameters
    def emit(self):
        pass
       
class Deforestation:
    """
      Configurable version of the handout's policy. To use the default, provide 50 years and 
      a percent increase of 3.

      Decreases the amount of trees in a country. As a result, carbon emissions, which
      start at a baseline of ((baseline)), are multiplied by ((increase_ratio)) every year
      for ((duration_years)) consecutive years. After that year, the carbon 
      emissions for that country remain constant.
    """
    def __init__(self, baseline: float, duration_years: int, increase_ratio: float):
        pass

    # TODO: add other necessary parameters
    def emit(self):
        pass

class MatchLowest:
    """
    Match the prior-year emissions of the lowest-emitting country in the simulation.
    Note that this requires access to elements of the simulation's state. Start with
    ((baseline)), since there is no history available at the beginning of the simulation.    
    """
    def __init__(self, baseline: float):
        pass

    # TODO: add other necessary parameters
    def emit(self):
        pass
