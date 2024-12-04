import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List

# Constants
BDR_BASE_URL = "https://repository.library.brown.edu"
COLLECTION_URL = f"{BDR_BASE_URL}/studio/collections/bdr:tkz6xrdc/"
COLLECTION_ID = "tkz6xrdc"

@dataclass
class BDRItem:
   # Dataclass for BDR items
   pass

def get_items_from_url(item_url: str) -> List[BeautifulSoup]:
   """
   Fetches items from the first collections page and returns a list of BeautifulSoup objects.

   :param item_url: URL of the item page
   :return: BeautifulSoup object of the item page
   """
   pass

# Paste the other functions here


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
   collection_pages = get_pages_from_id(COLLECTION_ID)
   item_pages = get_items_from_pages(collection_pages)
   for item in item_pages:
      bdritem = scrape_item(item)
      print(bdritem)

if __name__ == "__main__":
   run() 
   # main()
