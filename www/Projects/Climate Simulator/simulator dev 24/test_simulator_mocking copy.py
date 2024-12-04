### Imports ###
import pygame
from unittest.mock import patch, MagicMock
from protosimulator import *
from protosdisplay import *
import protopolicies
from pytest import approx

### Initalizes the simulator to reflect how we initalize it in main ###
def sim_init(sim : Simulator): 
    sim.add_country('United States', protopolicies.Baseline(6.5), 10)
    sim.add_country('China', protopolicies.TaxEmissions(14, 0.05), 8)
    sim.add_country('Colombia', protopolicies.Deforestation(0.07, 50, 0.03), 24)
    sim.add_country('Libya', protopolicies.MatchLowest(0.06), 23)
    sim.add_country('United Kingdom', protopolicies.Reducing(4.5, 0.5), 9)

def test_step_button_click():
    #### Setting up the Simiulator ####
    simulator = Simulator()
    sim_init(simulator)
    display = Display(simulator)
    pygame.init()

    #### Creating a mock event #### 
    with patch('pygame.event.get') as mock_get:
        # Create a mock event for the step button click
        mock_event = pygame.event.Event(pygame."Insert Event", {
            'button': 1, ### (Right click)###
            'pos': (60, 540)
        })
        
        #### Setting the return value of mock_get as the mock_event that we've created and quitting
        ### This sets a lsit of the events the program should run
        mock_get.return_value = [mock_event, pygame.event.Event(pygame.QUIT)]
        
        #### Run the display #### 
        display.run()
        
        #### Test that the mock_event correctly changed the enviroment #### 
        "Insert here"
        
        ### Quit Pygame ###
        pygame.quit()

def test_step_advance_year():
    simulator = Simulator()
    display = Display(simulator)
    pygame.init()

    with patch('pygame.event.get') as mock_get, \
         patch.object(Simulator, 'advance_year') as mock_advance_year:
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event.button = 1
        mock_event.pos = step_pos
        
        mock_get.return_value = [mock_event, pygame.event.Event(pygame.QUIT)]
        
        display.run()
        
        mock_advance_year.assert_called_once()
    pygame.quit()


