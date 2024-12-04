import pygame
import policies
from pytest import approx
from display import Display
from simulator import Simulator
from unittest.mock import patch, MagicMock

# Coordinates of the step button in pygame
STEP_BUTTON_POS = (60, 540)

def initialize_simulator(sim: Simulator):
    """
    Initializes the simulator with the countries and their policies.
    Code taken from main.py.
    """
    sim.add_country('United States', policies.Baseline(6.5), 10)
    sim.add_country('China', policies.TaxEmissions(14, 0.05), 8)
    sim.add_country('Colombia', policies.Deforestation(0.07, 50, 0.03), 24)
    sim.add_country('Libya', policies.MatchLowest(0.06), 23)
    sim.add_country('United Kingdom', policies.Reducing(4.5, 0.5), 9)


def test_step_button_click():
    """
    Tests that the step button works correctly
    """
    #Initializing the simulator
    simulator = Simulator()
    initialize_simulator(simulator)
    display = Display(simulator)
    pygame.init()

    # Mocking the get function
    with patch('pygame.event.get') as mock_get:
        # TODO: Create the mock event for pressing the step button
        # Replace 'YOUR_ANSWER_HERE' with the correct pygame event type
        # Hint: Look up pygame event types for mouse button clicks. pygame._
        mock_event = pygame.event.Event(YOUR_ANSWER_HERE, {
            'button': 1,
            'pos': STEP_BUTTON_POS
            # 'pos' is the location where you will be mocking your click.
            #  We're providing the correct coordinates of the step button.
            #  Consider the implications if the coordinates were incorrect,
            #  accidentally or otherwise."
        })
        
        # Mocking the return value of the get function
        mock_get.return_value = [mock_event, pygame.event.Event(pygame.QUIT)]
        
        # Running the display
        display.run()

        # Examine the simulator state
        # We "pressed" the step button once, so the time should be 2011
        assert simulator.time == 2011

        # TODO: Write at least three more tests!


        # Can you mock more events to test the display?
        
        # Quitting Pygame
        pygame.quit()

