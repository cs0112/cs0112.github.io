from simulator import *
from pytest import approx
import policies
from pytest import approx

"""
Tests for our Simulator class.
Feel free to add tests for any helper methods you create as you see fit.
"""

s = Simulator()
s.add_country('United States', policies.Baseline(6.5), 10)
s.add_country('China', policies.Reducing(14, 0.5), 8)
s.add_country('United Kingdom', policies.TaxEmissions(4.5, 0.05), 9)
s.add_country('Colombia', policies.Deforestation(4.5, 1, 0.03), 9)
s.add_country('Libya', policies.MatchLowest(1), 5)

s2 = Simulator()
s2.add_country('United States', policies.Baseline(1), 5)

s3 = Simulator()
s3.add_country('United States', policies.Baseline(4000), 5)

s4 = Simulator()

def test_year():
    #This tests that the intial time of the simulator is corrext
    assert s.time == 2010
    #This tests that advance_year() increases the time by one year when called
    s.advance_year()
    assert s.time == 2011 
    #This tests that advance_year() still functions when called continuously
    s.advance_year()
    assert s.time == 2012

def test_advance_year():
    #This is a basic test, not using an edge case, but using all policies
    s.advance_year()
    assert s.prior_emissions == {'United States' : 6.5, 'China' : 14, 'United Kingdom' : 4.5, 'Colombia' : 4.5,
                                 'Libya' : 1}
    assert s.cumulative_co2_emissions == 2324.5
    assert s.global_surface_temp_inc == 1.16225
    assert s.country_temperatures == {'United States' : 12.3245, 'China' : 9.16225, 'United Kingdom' : 11.3245, 
                               'Colombia' : 11.16225, 'Libya' : approx(7.3245)}
    assert s.time == 2011
    #This is to test that the function still works when advance_year() is used twice
    s.advance_year()
    assert s.prior_emissions == {'United States' : 6.5, 'China' : 13.5, 'United Kingdom' : approx(4.275), 
                                 'Colombia' : 4.635, 'Libya' : 1}
    assert s.cumulative_co2_emissions == 2348.41
    assert s.global_surface_temp_inc == 1.174205
    assert s.country_temperatures == {'United States' : 14.67291, 'China' : 10.336455, 'United Kingdom' : 13.67291, 
                                      'Colombia' : 12.336455, 'Libya' : approx(9.67291)}
    assert s.time == 2012
    #This is to test that the function still works when advance_year() is used continuously
    s.advance_year()
    assert s.prior_emissions == {'United States' : 6.5, 'China' : 13.0, 'United Kingdom' : approx(4.06125), 
                                 'Colombia' : 4.635, 'Libya' : 1}
    assert s.cumulative_co2_emissions == 2371.60625
    assert s.global_surface_temp_inc == approx(1.18580312)
    assert s.country_temperatures == {'United States' : approx(17.04451624), 'China' : approx(11.52225812), 
                                      'United Kingdom' : approx(16.04451624), 
                                      'Colombia' : approx(13.52225812), 'Libya' : approx(12.04451624)}
    assert s.time == 2013
    #This is to test that the function still works properly when the calculation for cumulative_co2_emissions is found
    #to be below 2300
    s2.advance_year()
    assert s2.prior_emissions == {'United States' : 1}
    assert s2.cumulative_co2_emissions == 2300
    assert s2.global_surface_temp_inc == approx(1.15)
    assert s2.country_temperatures == {'United States' : approx(7.3)}
    assert s2.time == 2011
    #This is to test that the function still works properly when the calculation for cumulative_co2_emissions is found
    #to be below 2300 and advance_year() is used multiple times
    s2.advance_year()
    assert s2.prior_emissions == {'United States' : 1}
    assert s2.cumulative_co2_emissions == 2300
    assert s2.global_surface_temp_inc == approx(1.15)
    assert s2.country_temperatures == {'United States' : approx(9.6)}
    assert s2.time == 2012
    #This is to test that the function still works properly when the cumulative_co2_emissions * 0.005 is greater than
    #the max_temperature_inc
    s3.advance_year()
    assert s3.prior_emissions == {'United States' : 4000}
    assert s3.cumulative_co2_emissions == 6294
    assert s3.global_surface_temp_inc == 3.0
    assert s3.country_temperatures == {'United States' : 11}
    assert s3.time == 2011
    #This is to test that the function still works properly when the cumulative_co2_emissions * 0.005 is greater than
    #the max_temperature_inc and advance_year() is used multiple times
    s3.advance_year()
    assert s3.prior_emissions == {'United States' : 4000}
    assert s3.cumulative_co2_emissions == 10288
    assert s3.global_surface_temp_inc == 3.0
    assert s3.country_temperatures == {'United States' : 17}
    assert s3.time == 2012

def test_report():
    #This tests the inital state of s. 
    initial_report = s.report()
    assert initial_report == [{'name': 'United States', 'temperature': 10}, {'name': 'China', 'temperature': 8}, 
                              {'name': 'United Kingdom', 'temperature': 9}, {'name' : 'Colombia', 'temperature' : 9},
                              {'name' : 'Libya', 'temperature' : 5}]
    #This is to test that the function still works properly when advance_year() is used once
    s.advance_year()
    report_after_one_year = s.report()
    assert report_after_one_year == [{'name': 'United States', 'temperature': 12.3245}, 
                                     {'name': 'China', 'temperature': 9.16225}, 
                                     {'name': 'United Kingdom', 'temperature': 11.3245}, 
                                     {'name' : 'Colombia', 'temperature' : 11.16225}, 
                                     {'name' : 'Libya', 'temperature' : approx(7.3245)}]
    #This is to test that the function still works properly when advance_year() is used multiple times
    s.advance_year()
    report_after_two_years = s.report()
    assert report_after_two_years == [{'name': 'United States', 'temperature': 14.67291}, 
                                      {'name': 'China', 'temperature': 10.336455}, 
                                      {'name': 'United Kingdom', 'temperature': 13.67291}, 
                                      {'name' : 'Colombia', 'temperature' : 12.336455}, 
                                      {'name' : 'Libya', 'temperature' : approx(9.67291)}]
    #This is to test that the function still works properly when a simulator has had no countries added to it
    initial_report = s4.report()
    assert initial_report == []