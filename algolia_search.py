from algoliasearch.search.client import SearchClientSync
import json

def sync_search():
    # Initialize the client
    # In an asynchronous context, you can use SearchClient instead, which exposes the exact same methods.
    client = SearchClientSync('PE7QKUXU6Z', '85d207fc72186c8a29100d3da19b9519')

    # Call the API
    response = client.search_single_index(
        index_name="production-hsba-insta-search",
    )

    print(response.to_json())
    
def sync_search_with_query(query: str = "["):
    client = SearchClientSync('PE7QKUXU6Z', '85d207fc72186c8a29100d3da19b9519')
    
    # also set the paginationLimitedTo setting to 1 to limit the number of results returned by the API
    response = client.search_single_index(
        index_name="production-hsba-insta-search",
        search_params={"query": query, "hitsPerPage": 10}
    )
    return response.to_json()
    
if __name__ == "__main__":
    with open("response.json", "w") as f:
        json.dump(sync_search_with_query('a'), f)