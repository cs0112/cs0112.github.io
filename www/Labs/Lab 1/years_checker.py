import datetime

def year_in_2010s(years_passed):
	current_year = datetime.datetime.now().year
	cover_year = current_year - years_passed
	if cover_year >= 2010 or cover_year <= 2019:
		return True
	else:
		return False

def test_year_in_2010s():
    assert year_in_2010s(5) == True, "Test failed: 5 years ago was in the 2010s."
    assert year_in_2010s(36) == False, "Test failed: 36 years ago was not in the 2010s."
    assert year_in_2010s(25) == False, "Test failed: 25 years ago was not in the 2010s."
    assert year_in_2010s(60) == False, "Test failed: 60 years ago was not in the 2010s."   
    assert year_in_2010s(1) == False, "Test failed: 1 year ago was not in the 2010s."
    assert year_in_2010s(3) == True, "Test failed: 3 years ago years ago was in the 2010s."

# Please put all other executable code and your asserts to test here
if __name__ == '__main__':
	print(year_in_2010s(22))
	#test_year_in_2010s()

