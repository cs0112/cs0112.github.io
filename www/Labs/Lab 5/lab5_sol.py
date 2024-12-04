import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List

BDR_BASE_URL = "https://repository.library.brown.edu"
COLLECTION_URL = f"{BDR_BASE_URL}/studio/collections/bdr:tkz6xrdc/"
COLLECTION_ID = "tkz6xrdc"

@dataclass
class BDRItem:
   # Dataclass for BDR items
    title: str
    year: int
    contributor: list[str]
    subject: list[str]
    abstract: str
    notes: str


def get_items_from_url(item_url: str) -> List[BeautifulSoup]:
   """
   Fetches items from the first collections page and returns a list of BeautifulSoup objects.

   :param item_url: URL of the item page
   :return: BeautifulSoup object of the item page
   """
   response = requests.get(item_url)
   soup = BeautifulSoup(response.text, "html.parser") # gets the BS of the collection page
   panels = soup.find_all("div", class_="panel-body") # gets all the panel bodies

   soups = []

   for panel in panels:
       # This is to make sure we only get public items
       if not panel.find_all(class_="text-info"):
          href = panel.find("a")["href"] # finds the "a" tag (the thumbnail) which has the link to the item page
          url = f"{BDR_BASE_URL}{href}" 
          response = requests.get(url) 
          page = BeautifulSoup(response.text, "html.parser") # gets the BS of the item page
          soups.append(page)
   return soups

# run the run() function now to print your soups!

# Paste the other functions here

def get_title(page: BeautifulSoup) -> str:
    title = page.find_all("h1")[0].text.strip() # find the h1, make sure to strip because of whitespace
    return title

def get_year(page: BeautifulSoup) -> int:
    a_list = page.find_all("a") # finds all the links
    for a in a_list:
        href = a.attrs['href'] # gets the href
        if "?selected_facets=mods_dateAll_year_ssim" in href: # if there is this str in the href, it is the year
            return int(a.text)
    return -1

def get_contributor(page: BeautifulSoup) -> list[str]:
    contributors = []
    a_list = page.find_all("a")
    for a in a_list:
        href = a.attrs['href']
        if "?selected_facets=contributor_display" in href: # same for contributors
            contributors.append(a.text)
    return contributors

def get_subject(page: BeautifulSoup):
    subjects = []
    a_list = page.find_all("a")
    for a in a_list:
        href = a.attrs['href']
        if "?selected_facets=mods_subject_joined_ssim" in href: # and subjects
            subjects.append(a.text)
    return subjects

def get_abstract(page: BeautifulSoup):
    abstract = ""
    description_panel = page.find_all(id="description")[0].find_all(class_="panel-body")[0].contents # gets the description and then gets the panel body from that
    description_panel = [content for content in description_panel if content.name != None] # filters the panel body to remove any nonimportant items
    for idcontent, content in enumerate(description_panel): # enumerate makes a tuple (ex. (0, item0), (1, item1),...) so we can keep track of the index while still iterating thru description panel
        if content.name == "dt" and content.text.strip() == "Abstract:": # since both abstract and notes are in dd tags, there's not really any unique identifying html we can .find for, but we can identify the abstract by using the contex. we know that if theres a <dt>Abstract:<dt> whatever follows after it will be the actual abstract, so we can get the next index
            abstract = description_panel[idcontent+1].text.strip()
            break
    return abstract

def get_notes(page: BeautifulSoup):
    notes = ""
    description_panel = page.find_all(id="description")[0].find_all(class_="panel-body")[0].contents
    description_panel = [content for content in description_panel if content.name != None]
    for idcontent, content in enumerate(description_panel):
        if content.name == "dt" and content.text.strip() == "Notes:": # same as abstract
            notes = description_panel[idcontent+1].text.strip()
            break
    return notes

def scrape_item(page: BeautifulSoup) -> BDRItem:
    """
    Extracts relevant information from an item page and returns an Item object.
    
    :param page: BeautifulSoup object of the item page
    :return: BDRItem object containing the scraped information
    """
    # TODO: Implement this function
    title = get_title(page)
    year = get_year(page)
    contributor = get_contributor(page)
    subject = get_subject(page)
    abstract = get_abstract(page)
    notes = get_notes(page)
    return BDRItem(title, year, contributor, subject, abstract, notes)

# in run(), comment out print(soup) and uncomment the other lines to print out your items and info abt your items

def get_pages_from_id(collection_id: str, num_pages: int = 1) -> list[BeautifulSoup]:
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
            # This is to make sure we only get public items
            if not panel.find_all(class_="text-info"):
                href = panel.find_all('a')[0].attrs['href']
                url = f"https://repository.library.brown.edu{href}"
                url_content = requests.get(url).content
                page = BeautifulSoup(url_content, features='html.parser')
                soups.append(page)
    return soups

# in if __name__, comment out run() and uncomment main()

## RUN THIS FUNCTION
def run():
    soups = get_items_from_url(COLLECTION_URL)
    for soup in soups:
        print(soup)
        # item = scrape_item(soup)
        # print(item)
        # print(item.title)
        # print(item.year)
        # print(item.contributor)

def main():
    collection_pages = get_pages_from_id(COLLECTION_ID) # note that we're only scraping the first page here since the default num pages = 1. you can pass in a diff number if you want.
    item_pages = get_items_from_pages(collection_pages)

    for item in item_pages:
       bdritem = scrape_item(item)
       print(bdritem)


if __name__ == "__main__":
    run()
    # main()
