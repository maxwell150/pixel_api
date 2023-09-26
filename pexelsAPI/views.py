from pexels_api import API
from django.shortcuts import render

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        query = request.POST['query']
        # Type your Pexels API
        PEXELS_API_KEY = ''
        # Create API object
        api = API(PEXELS_API_KEY)
        # Search photos
        api.search(f'{query}', page=1, results_per_page=5)
        # Get photo entries
        photos = api.get_entries()
    else:
        photos = ''

    return render(request, 'pexelsAPI/home/photos.html', {'photos': photos})

