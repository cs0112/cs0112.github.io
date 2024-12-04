import pytest
from bdrscrape import scrape_data as web_scrape_data
from bdrapi import api_data

@pytest.fixture
def sample_collection():
    return {
        "CSCI": "bfttpwkj"  # Replace with an actual collection ID
    }

def test_web_scrape_vs_api(sample_collection):
    # Get data using web scraping
    web_data = web_scrape_data(sample_collection)
    
    # Get data using API
    api_data_result = api_data(sample_collection)
    
    # Compare the results
    for collection, items in web_data.items():
        assert collection in api_data_result, f"Collection {collection} missing from API results"
        
        web_items = sorted(items, key=lambda x: x.title)
        api_items = sorted(api_data_result[collection], key=lambda x: x.title)
        
        assert len(web_items) == len(api_items), f"Number of items mismatch for collection {collection}"
        
        for web_item, api_item in zip(web_items, api_items):
            assert web_item.title == api_item.title, f"Title mismatch: {web_item.title} vs {api_item.title}"
            assert web_item.year == api_item.year, f"Year mismatch for {web_item.title}"
            assert web_item.contributor == api_item.contributor, f"Contributor mismatch for {web_item.title}"
            assert set(web_item.subject) == set(api_item.subject), f"Subject mismatch for {web_item.title}"
            
            # Note: We're using a less strict comparison for abstract and notes
            # as there might be slight differences in formatting
            assert web_item.abstract.strip() == api_item.abstract.strip(), f"Abstract mismatch for {web_item.title}"
            assert web_item.notes.strip() == api_item.notes.strip(), f"Notes mismatch for {web_item.title}"
