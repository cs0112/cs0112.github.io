from bs4 import BeautifulSoup 
from requests import get

assignments_url = "https://cs0112.github.io/Pages/assignments.html"
staff_url       = "https://cs0112.github.io/Pages/staff.html" 

assignments_response = get(assignments_url)
print(assignments_response)
assignments_text = assignments_response.content
print(assignments_text)
assignments_page = BeautifulSoup(assignments_text, features='html.parser')
print(assignments_page)

# Find all subtrees rooted in an element with the <table> tag
assignments_tables = assignments_page.find_all('table')
print(len(assignments_tables))
# get the homework table in isolation
hw_table = assignments_tables[0]
print(hw_table)
print(type(assignments_tables)) # basically a list
hw_rows = hw_table.find_all('tr')

# where is that 7th row coming from?
# hard to read print(hw_rows) sometimes, so...
for row in hw_rows: 
    print(f'**** row: {row}')
    print()
# It is the header row! We got the table, not the table _body_ only

# cleanest approach is maybe to find the 'tbody' within the table
# to demo BS4 features though, we'll do something a bit less clean:
#   keep only the rows with some <td> in them
cleaned_hw_rows = [r for r in hw_rows if len(r.find_all('td')) > 0]
print(f'cleaned_hw_rows={cleaned_hw_rows}')

#   *** Discussion in near future ***
# Notice: if we named the variable something like 'trow', we'd _still be able_
#   to use "row", but the behavior would become buggy. What's going on?
def clean_nth_column(row, n):
    return row.find_all('td')[n].text.strip()
    
hw_due = {clean_nth_column(row, 1): clean_nth_column(row, 3) for row in cleaned_hw_rows}
print(hw_due)
