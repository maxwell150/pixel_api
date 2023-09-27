from django.shortcuts import render
from . import pexel_api

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        query = request.POST['query']
        photos = pexel_api.fetch_data(query)
    else:
        photos = ''

    return render(request, 'pexelsAPI/home/photos.html', {'photos': photos})

