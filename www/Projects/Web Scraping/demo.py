from bdrscrape import run_scrape, COLLECTIONS
from bdrapi import run_api
from common import most_common_subject, year_after, top_contributor

def run_queries_on_web_data():
    print("Running queries on web-scraped data:")
    
    # Web scrape
    web_data = run_scrape()
    
    if web_data:
        for collection in COLLECTIONS.keys():
            print(f"\nResults for {collection} collection:")

            # You can call your functions here to test them
            
            # TODO: Call most_common_subject and print the result
            # Hint: subject = most_common_subject(web_data, collection)
            # print(f"Most common subject: {subject}")
            
            # TODO: Call year_after for items after 2010 and print the count
            # Hint: items_after_2010 = year_after(web_data, collection, 2010)
            # print(f"Number of items after 2010: {len(items_after_2010)}")
            
            # TODO: Call top_contributor and print the result
            # Hint: contributor = top_contributor(web_data, collection)
            # print(f"Top contributor: {contributor}")
    else:
        print("Failed to retrieve web data.")


def run_queries_on_api_data():
    print("\nRunning queries on API data:")
    
    # API data
    api_data_result = run_api()
    
    if api_data_result:
        for collection in COLLECTIONS.keys():
            print(f"\nResults for {collection} collection:")

            # You can call your functions here to test them
            
            # TODO: Call most_common_subject and print the result
            # Hint: subject = most_common_subject(api_data_result, collection)
            # print(f"Most common subject: {subject}")
            
            # TODO: Call year_after for items after 2010 and print the count
            # Hint: items_after_2010 = year_after(api_data_result, collection, 2010)
            # print(f"Number of items after 2010: {len(items_after_2010)}")
            
            # TODO: Call top_contributor and print the result
            # Hint: contributor = top_contributor(api_data_result, collection)
            # print(f"Top contributor: {contributor}")
    else:
        print("Failed to retrieve API data.")


if __name__ == "__main__":
    # Uncomment the following lines to run the queries
    # run_queries_on_web_data()
    # run_queries_on_api_data()
