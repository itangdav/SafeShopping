from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post


from bin import GetResultsMethod
import geocoder


# Here is the code to get current location:
# g = geocoder.ip('me')
# lat = g.latlng[0]
# long = g.latlng[1]

# We can use the store class by calling
# GetResultsMethod.store

# We can run the getResults method by calling the following method:
# @returns a list of dictionaries sorted in increasing score order
# GetResultsMethod.getResults(lat, long, radius, weight_distance, weight_popularity)

def home(request):
    g = geocoder.ip('me')
    lat = g.latlng[0]
    long = g.latlng[1]
    radius = 0.015  # Radius is in latitude or longitude angles
    weight_distance = 5.0
    weight_popularity = 1.0

    type_of_place = ['grocery_or_supermarket']

    data = GetResultsMethod.getResults(lat, long, radius, weight_distance, weight_popularity)

    print(data)

    return render(request, 'map/home.html')

def addressPost(request):
    if request.method == 'POST':
        if request.POST.get('address'):
            print('TODO')



