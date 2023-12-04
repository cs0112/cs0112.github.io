from bs4 import BeautifulSoup 
from requests import get

assignments_url = "https://cs0112.github.io/Pages/assignments.html"
assignments_response = get(assignments_url)
assignments_text = assignments_response.content
assignments_page = BeautifulSoup(assignments_text, features='html.parser')
first_table = assignments_page.find_all('table')[0]
homework_rows = first_table.find_all('tbody')[0].find_all('tr')
hw1_cols = homework_rows[0].find_all('td')
for col in hw1_cols:
    print(f'Column: {col}')
    print()

