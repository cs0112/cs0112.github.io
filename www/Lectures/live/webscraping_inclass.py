from bs4 import BeautifulSoup  # parse the request contents
from requests import get   # send a web request

# Step 1a: Make a web request for the desired page

assignments_url = 'https://cs0112.github.io/Pages/assignments.html'
assignments_response = get(assignments_url)
# note: ideally, we'd look at response or ok, and do some error behavior
assignments_content = assignments_response.content

# Step 1b: Parse the content of the reply into a `BeautifulSoup` object
assignments_page = BeautifulSoup(assignments_content, features='html.parser')

# Step 2: Extract the information we want into a reasonable data structure.
assignments_tables = assignments_page.find_all('table')
homework_table = assignments_tables[0]
project_table = assignments_tables[1]
homework_rows = homework_table.find('tbody').find_all('tr')

# for-loop version
due_dates = {}
for hw_row in homework_rows: 
    cells = hw_row.find_all('td')
    hw_name_cell = cells[1]
    hw_name_link = hw_name_cell.find('a')
    hw_due_str = cells[3].text.strip()
    if hw_name_link: 
        # If the HW is released, there is a link which contains the name
        # print(f'{hw_name_link.text.strip()} : {hw_due_str}')
        due_dates[hw_name_link.text.strip()] = hw_due_str
    else:
        # If the HW is not released, the cell just contains the name, no link
        # print(f'{hw_name_cell.text.strip()} : {hw_due_str}')
        due_dates[hw_name_cell.text.strip()] = hw_due_str
print(due_dates)
    


#print(len(assignments_tables))
#print(assignments_tables[0])
#print(assignments_tables[1])

# Step 3: Use that data structure for the computation we desire. 