from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


from bin import GetResultsMethod
import geocoder


def home(request):
    g = geocoder.ip('me')
    lat = g.latlng[0]
    long = g.latlng[1]
    radius = 0.015  # Radius is in latitude or longitude angles
    weight_distance = 5.0
    weight_popularity = 1.0

    type_of_place = ['grocery_or_supermarket']

    data = GetResultsMethod.getResults(lat, long, radius, weight_distance, weight_popularity, type_of_place)

    #print(data)

    # , 'lat': data["lat"], 'long': data["long"], 'score': data["score"]

    return render(request, 'map/index.html', data)
