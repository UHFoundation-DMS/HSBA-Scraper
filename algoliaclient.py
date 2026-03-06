from algoliasearch.search.client import SearchClientSync


def sync_search():
    # Initialize the client
    # In an asynchronous context, you can use SearchClient instead, which exposes the exact same methods.
    client = SearchClientSync('PE7QKUXU6Z', '85d207fc72186c8a29100d3da19b9519')

    # Call the API
    response = client.search_single_index(
        index_name="production-hsba-insta-search",
    )

    print(response.to_json())

#def async_search():