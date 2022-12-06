from bs4 import BeautifulSoup
import requests

calendar_url = "https://www.brown.edu/about/administration/registrar/academic-calendar"
calendar_page = BeautifulSoup(
   requests.get(calendar_url).content, features="html.parser"
)


def scrape_events(page: BeautifulSoup) -> dict:
   # TODO: Write function that creates a dict (key is date and value is event name)
   events_dict = {}
   all_uls = page.find_all("ul", "lw_widget_results_events")
   for ul in all_uls:
      ul_events = ul.find_all("li")
      for e in ul_events:
         e_date = e.find("div", "lw_compact_date").text.strip()
         e_name = e.find("div", "lw_compact_info").find("p", "lw_events_title").text.strip()
         events_dict[e_date] = e_name
   return events_dict

if __name__ == '__main__':
   print(scrape_events(calendar_page))
