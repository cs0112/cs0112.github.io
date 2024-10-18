from bs4 import BeautifulSoup
import requests
from dataclass import dataclass

COLLECTIONS = {
    "AFRI" : "gwy9dgfq",
    "AMST" : "tkz6xrdc" ,
    "ANTH" : "n9pjv5jn" ,
    "APMA" : "8jst2uj2" ,
    "CHEM" : "2j3zgur5" ,
    "CLAS" : "yjdg7res" ,
    "CLPS" :  "znu9pkpc",
    "COLT" : "zwcrk24q" ,
    "CSCI" : "bfttpwkj",
    "EEPS" : "ktkks679" ,
    "ECON" : "w3sazjd2"
}

@dataclass
class BDRItem:
   #TODO: Fill this dataclass out

##################### FROM LAB 5 #######################

def get_pages_from_url(collection_url: str, num_pages: int = 1) -> list[BeautifulSoup]:
    """
    Retrieves and parses the specified number of pages from a collection.
    
    :param url: URL of the collection
    :param num_pages: Number of pages to retrieve (default is 1)
    :return: List of BeautifulSoup objects, one for each page
    """
    # TODO: Copy and paste your implementation from lab5.py
    pass


def get_items_from_pages(collection_pages: list[BeautifulSoup]) -> list[BeautifulSoup]:
    """
    Extracts individual item pages from the collection pages.
    
    :param collection_pages: List of BeautifulSoup objects representing collection pages
    :return: List of BeautifulSoup objects, one for each item page
    """
    # TODO: Copy and paste your implementation from lab5.py
    pass


def scrape_item(item_page: BeautifulSoup) -> BDRItem:
    """
    Extracts relevant information from an item page and returns an Item object.
    
    :param item_page: BeautifulSoup object of the item page
    :return: BDRItem object containing the scraped information
    """
    # TODO: Copy paste your helper functions from lab5.py
    title = get_title(page)
    year = get_year(page)
    contributor = get_contributor(page)
    subject = get_subject(page)
    abstract = get_abstract(page)
    notes = get_notes(page)
    return BDRItem(title, year, contributor, subject, abstract, notes)


##################### SCRAPER IMPLEMENTATION #######################

def get_collection_dictionary() -> dict[str:list[BeautifulSoup]]:
   """
   Retrieves all item pages from a collection and returns a dictionary of collection names to lists of item pages.
   """
   pass


def scrape_data(collection_pages: dict[str:list[BeautifulSoup]]) -> dict[str:list[BDRItem]]:
   """
   Scrapes data from a collection of pages.

   : param collection_pages: Dictionary of collection names to lists of BeautifulSoup objects, the individual item pages of the collection
   : return: Dictionary of collection names to lists of BDRItem objects
   """
   pass


##################### QUERY FUNCTIONS #######################

def most_common_subject(data: dict[str:list[BDRItem]],, collection: str):
   """
   Returns the most common subject in the data.
   """
   pass


def year_after(data: dict[str:list[BDRItem]],, collection: str, year: int):
   """
   Returns the number of items published after the given year.
   """
   pass


def top_contributor(data: dict[str:list[BDRItem]],, collection: str, position: str):
   """
   Returns the top contributor in the data.
   """
   pass
