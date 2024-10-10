from bs4 import BeautifulSoup  # parse the request contents
from requests import get   # send a web request

# Step 1: identify the pages you want to scrape
assignments_url = 'https://cs0112.github.io/Pages/assignments.html'
staff_url = 'https://cs0112.github.io/Pages/staff.html'

# Step 2: get the response text! 
assignments_response = get(assignments_url)
print(assignments_response)
assignments_text = assignments_response.content
print(assignments_text)

# Step 3: parse the response
assignments_page = BeautifulSoup(assignments_text, features='html.parser')
print(f'assignments_page: {assignments_page}')

# Step 4: process the parsed response
def scrape_homeworks(page: BeautifulSoup) -> dict:
    tables = page.find_all('table')
    homework_table = tables[0]
    homework_rows = homework_table.find('tbody').find_all('tr')
    # for row in homework_rows: 
    #     name = row.find_all('td')[1].text.strip()
    #     due = row.find_all('td')[3].text.strip()
    #     print(f'assignment {name} is due {due}')
    def assign_name(row):
        return row.find_all('td')[1].text.strip()
    def assign_due(row): 
        return row.find_all('td')[3].text.strip()

    return {assign_name(row):assign_due(row) for row in homework_rows} 
print(scrape_homeworks(assignments_page))