import geocoder
import googlemaps
from bin.GetResultsMethod import API_KEY


def getLocation(address):
    try:
        gmaps = googlemaps.Client(key=API_KEY)
        result = gmaps.geocode(address)
        location = result[0]
        lat =location['access_points'][0]['location']['latitude']
        long =location['access_points'][0]['location']['longitude']
        return [lat,long]
    except:
        g = geocoder.ip('me')
        lat = g.latlng[0]
        long = g.latlng[1]
        return [lat, long]


#print(getLocation("123 Front Street Toronto"))