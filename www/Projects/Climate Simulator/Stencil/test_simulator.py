import policies
from simulator import *

"""
Tests for our Simulator class.
Feel free to add tests for any helper methods you create as you see fit.
"""

def test_year():
    s = Simulator()
    assert s.time == 0
    s.advance_year()
    assert s.time == 1


def test_advance_year():
    # Fill me in!
    pass


def test_report():
    # Fill me in!
    pass
