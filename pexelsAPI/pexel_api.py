from pexels_api import API


# Type your Pexels API
PEXELS_API_KEY = ''

def fetch_data(query):
    # Create API object
    api = API(PEXELS_API_KEY)
    # Search photos
    api.search(f'{query}', page=1, results_per_page=12)
    # Get photo entries
    photos = api.get_entries()

    return photos