import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List

# Constants
BDR_BASE_URL = "https://repository.library.brown.edu"
COLLECTION_URL = f"{BDR_BASE_URL}/studio/collections/bdr:bfttpwkj/"

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
   soup = BeautifulSoup(response.text, "html.parser")
   panels = soup.find_all("div", class_="panel-body")

   soups = []

   for panel in panels:
       # print(panel)
       if not panel.find_all("div", class_="text-info"):
          # print(panel)
          href = panel.find("a")["href"] 
          url = f"{BDR_BASE_URL}{href}"
          response = requests.get(url)
          page = BeautifulSoup(response.text, "html.parser")
          soups.append(page)
   return soups


# Paste the other functions here

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
        print(content.name)
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


def main():
   soups = get_items_from_url(COLLECTION_URL)

   for soup in soups:
      item = scrape_item(soup)
      print(soup)
      print(item)

if __name__ == "__main__":
    main()

