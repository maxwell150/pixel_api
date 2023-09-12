# Import API class from pexels_api package
from pexels_api import API
# Type your Pexels API
PEXELS_API_KEY = '82MKDwe99byKk9TX2DUk7RYUSJrvGnNgIUHGHb7nr3zPf3msdQxfuUeJ'
# Create API object
api = API(PEXELS_API_KEY)

# Search five 'kitten' photos
api.search('cat', page=1, results_per_page=1)
# Get photo entries
photos = api.get_entries()
# Loop the five photos
for photo in photos:
  # Print photographer
  print('Photographer: ', photo.photographer)
  # Print url
  print('Photo url: ', photo.url)
  # Print original size url
  print('Photo original size: ', photo.original)
  print('extension', photo.medium)
  print('portrait', photo.portrait)
  print('original', photo.original)