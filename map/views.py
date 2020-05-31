from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

from bin import GetResultsMethod
import geocoder


def home(request):
    return render(request, 'map/home.html')


def getResults(request):
    g = geocoder.ip('me')
    lat = g.latlng[0]
    long = g.latlng[1]
    radius = 0.015  # Radius is in latitude or longitude angles
    weight_distance = 5.0
    weight_popularity = 1.0

    type_of_place = ['grocery_or_supermarket']

    data = GetResultsMethod.getResults(lat, long, radius, weight_distance, weight_popularity, type_of_place)

    return HttpResponse(data)


def addressPost(request):
    if request.method == 'POST':
        if request.POST.get('address'):
            temp = 'todo'
