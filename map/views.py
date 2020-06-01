from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView



from bin import GetResultsMethod
from bin import getids
import geocoder


def home(request):
    g = geocoder.ip('me')
    lat = g.latlng[0]
    long = g.latlng[1]
    radius = 0.015  # Radius is in latitude or longitude angles
    weight_distance = 5.0
    weight_popularity = 1.0
    type_of_place = ['grocery_or_supermarket']
    address = request.POST['address']

    cords = getids.getLocation(address)
    lat = cords[0]
    long = cords[1]

    data = GetResultsMethod.getResults(lat, long, radius, weight_distance, weight_popularity, type_of_place)

    names = []
    lats = []
    longs = []
    scores = []
    for x in data:
        names.append(x["name"])
        lats.append(x["lat"])
        longs.append(x["long"])
        scores.append(x["score"])

    print(data)

    return render(request, 'map/index.html', {'lats': lats, "longs": longs, 'lat': lat, 'long': long, 'names': names, 'scores': scores})
