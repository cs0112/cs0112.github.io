import requests
from bs4 import BeautifulSoup
from common import BDRItem

COLLECTIONS = {
    "Africana Studies" : "gwy9dgfq", # 20
    "Center for Computational Molecular Biology" : "t9tw3bx7" , # 19
    "Center for Contemporary South Asia" : "mwp8qugm" , # 1
    "Center for Latin American and Caribbean Studies" : "8nzjmxz2" , # 19
    "Contemplative Studies Initiative" : "yxf89249" , # 2
    "Hispanic Studies" : "f5387375", # 41
    # "Egyptology and Assyriology" : "x7w6jvzn" , # 17
    # "French Studies" : "gfb24rk4" , # 24
    # "German Studies" : "4sd4vdnx", # 14 
    # "Institute at Brown for Environment & Society" : "2jxekvjb", # 4
    # "Integrative Studies" : "cemrxyw7", # 2
    # "International and Public Affairs" : "vy5eytxy", # 13
    # 'Italian Studies': "qwq8pmv2", # 33 
    # 'Middle East Studies': "c4tsruap", # 4
    # 'Pembroke Center for Teaching and Research on Women': "v7g9533y", # 2 
    # 'Portuguese and Brazilian Studies': "eb3recv7", # 29 
    # 'Program in Medieval Studies': "fzfkfz8c", # 1 
    # 'Slavic Studies': "hvuyvxt2", # 20 
    # 'The Watson Institute for International and Public Affairs': "ncjsg24k", # 22 
    # 'Theatre Arts and Performance Studies': "dya6rpsh", # 31 
    # 'Urban Studies': "k88kegfh" # 3 
}

##################### FROM LAB 5 #######################

def get_pages_from_url(collection_id: str, num_pages: int = 1) -> list[BeautifulSoup]:
    """
    Retrieves and parses the specified number of pages from a collection.
    
    :param collection_id: ID (7 character string, ex: gwy9dgfq) of the collection
    :param num_pages: Number of pages to retrieve (default is 1)
    :return: List of BeautifulSoup objects, one for each page
    """
    soups = []
    for page_number in range(1, num_pages + 1):
        url = f"https://repository.library.brown.edu/studio/collections/bdr:{collection_id}/?page={page_number}"
        url_content = requests.get(url).content
        page = BeautifulSoup(url_content, features='html.parser')
        results = page.find_all("h2")
        if results[0].text == "Not Found":
            break
        soups.append(page)
    return soups


def get_items_from_pages(collection_pages: list[BeautifulSoup]) -> list[BeautifulSoup]:
    """
    Extracts individual item pages from the collection pages.
    
    :param collection_pages: List of BeautifulSoup objects representing collection pages
    :return: List of BeautifulSoup objects, one for each item page
    """    
    soups = []
    for page in collection_pages:
        panel_results = page.find_all(class_="panel-body")
        for panel in panel_results:
            if not panel.find_all(class_="text-info"):
                href = panel.find_all('a')[0].attrs['href']
                url = f"https://repository.library.brown.edu{href}"
                url_content = requests.get(url).content
                page = BeautifulSoup(url_content, features='html.parser')
                soups.append(page)
    return soups


def scrape_item(item_page: BeautifulSoup) -> BDRItem:
    """
    Extracts relevant information from an item page and returns an Item object.
    
    :param item_page: BeautifulSoup object of the item page
    :return: BDRItem object containing the scraped information
    """
    title = get_title(item_page)
    year = get_year(item_page)
    contributor = get_contributor(item_page)
    subject = get_subject(item_page)
    abstract = get_abstract(item_page)
    notes = get_notes(item_page)
    return BDRItem(title, year, contributor, subject, abstract, notes)

##################### SCRAPER IMPLEMENTATION #######################

def get_collection_dictionary(collection: dict[str: str]) -> dict[str:list[BeautifulSoup]]:
    """
    Retrieves all item pages from a collection and returns a dictionary of collection names to lists of item pages.

    :param collection: Dictionary of collection names (ex: "Africana Studies") to collection ids (7 character string, ex: gwy9dgfq) 
    :return: Dictionary of collection names to list of item pages
    """
    pass


def scrape_data(collection_pages: dict[str:list[BeautifulSoup]]) -> dict[str:list[BDRItem]]:
    """
    Scrapes data from a collection of pages.

    :param collection_pages: Dictionary of collection names to lists of BeautifulSoup objects, the individual item pages of the collection
    :return: Dictionary of collection names to lists of BDRItem objects
    """
    pass


###### SOUP->ITEM INTERACTION IMPLEMENTATION ######

def get_title(page: BeautifulSoup) -> str:
    title = page.find_all("h1")[0].text.strip()
    return title

def get_year(page: BeautifulSoup) -> int:
    a_list = page.find_all("a")
    for a in a_list:
        href = a.attrs['href']
        if "?selected_facets=mods_dateAll_year_ssim" in href:
            return int(a.text)
    return -1

def get_contributor(page: BeautifulSoup) -> list[str]:
    contributors = []
    a_list = page.find_all("a")
    for a in a_list:
        href = a.attrs['href']
        if "?selected_facets=contributor_display" in href:
            contributors.append(a.text)
    return contributors

def get_subject(page: BeautifulSoup):
    subjects = []
    a_list = page.find_all("a")
    for a in a_list:
        href = a.attrs['href']
        if "?selected_facets=mods_subject_joined_ssim" in href:
            subjects.append(a.text)
    return subjects

def get_abstract(page: BeautifulSoup):
    abstract = ""
    description_panel = page.find_all(id="description")[0].find_all(class_="panel-body")[0].contents
    description_panel = [content for content in description_panel if content.name != None]
    for idcontent, content in enumerate(description_panel):
        if content.name == "dt" and content.text.strip() == "Abstract:":
            abstract = description_panel[idcontent+1].text.strip()
            break
    return abstract

def get_notes(page: BeautifulSoup):
    notes = ""
    description_panel = page.find_all(id="description")[0].find_all(class_="panel-body")[0].contents
    description_panel = [content for content in description_panel if content.name != None]
    for idcontent, content in enumerate(description_panel):
        if content.name == "dt" and content.text.strip() == "Notes:":
            notes = description_panel[idcontent+1].text.strip()
            break
    return notes

##################### RUN FUNCTIONS #######################

def run_scrape():
    """
    Runs the scraping process.
    """
    data = scrape_data(get_collection_dictionary(COLLECTIONS))
    return data
