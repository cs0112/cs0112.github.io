from bs4 import BeautifulSoup 
from requests import get

# pip3 install bs4
# pip3 install requests

# I like to have a variable name for the URL, because otherwise the code below can get verbose.
assignments_url = "https://cs0112.github.io/Pages/assignments.html"
# "http://cs.brown.edu/courses/csci0112/fall-2021/assignments.html"
staff_url       = "https://cs0112.github.io/Pages/staff.html" 
# "http://cs.brown.edu/courses/csci0112/fall-2021/staff.html"

# send a GET request and obtain the response (we imported this function)
assignments_response = get(assignments_url)
# get the HTML content of the response as text
assignments_text = assignments_response.content
# create a BeautifulSoup object tree that we can easily explore
# the 'html.parser' parameter says what language we're parsing. This parser
# is much more sophisticated than the toy one we used a few weeks ago. 
assignments_page = BeautifulSoup(assignments_text, features='html.parser')

# By default, this only prints a response code; 200 means successful for us
# print(f'assignments_response: {assignments_response}')
# But the content of the reply contains more info: the HTML as a raw string 
# print(f'assignments_text: {assignments_text}')
# Finally, the object containing the explorable tree
#   (This class has a very nice __repr__ method! Note the indentation.)
print(f'assignments_page: {assignments_page}')

def scrape_homeworks(page: BeautifulSoup) -> dict:
    '''Accepts a BeautifulSoup tree of the 0112 homeworks page, and returns a homework dictionary'''
    # We noticed that the homeworks were in the _first_ HTML Table
    first_table = page.find_all('table')[0]
    # We noticed that the table body contained rows, one row per homework
    homework_rows = first_table.find_all('tbody')[0].find_all('tr')
    print(f'Found {len(homework_rows)} rows.')

    def scrape_homework_row_name(row):
        '''Nested helper to processes a table row and return a _key_ to place in our dictionary'''
        # Eliding type hints for some of this, because they get difficult. the .text field of 
        #   an element returns its text, and then we use Python's string.strip() method to remove
        #   blank spaces, etc.
        cells = row.find_all('td')
        print(cells)
        print()
        return cells[1].text.strip()
    def scrape_homework_row_due(row):
        '''Nested helper to processes a table row and return a _value_ to place in our dictionary'''
        return row.find_all('td')[3].text.strip()
    
    homework_assignments = {scrape_homework_row_name(row): scrape_homework_row_due(row) 
                            for row in homework_rows}
    return homework_assignments

print(f'scraped homeworks: {scrape_homeworks(assignments_page)}')

########################################################
## staff names

staff_page = BeautifulSoup(get(staff_url).content, features='html.parser')

def scrape_staff_names(page: BeautifulSoup) -> list:
    # Doesn't deliver anything
    # names = [name.find('span').strip() for name in page.find_all('staff-name')]
    # Look for a header-3 element with "class name" 
    names = [name.text.strip() for name in page.find_all('h3', class_='staff-name')]
    return names

print(f'scraped staff names: {scrape_staff_names(staff_page)}')

###################################################
### How can I test this with a local HTML file? ###

# test_file = open('downloaded.html', 'r')
# test_text = test_file.read()
# test_file.close()
# test_page = BeautifulSoup(test_text, features='html.parser')
# Now use test_page as you would something you scraped from the web

