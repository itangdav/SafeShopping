import googlemaps
from bin.GetResultsMethod import API_KEY


def getLocation(address):
    gmaps = googlemaps.Client(key=API_KEY)
    result = gmaps.geocode(address)
    location = result[0]
    lat =location['access_points'][0]['location']['latitude']
    long =location['access_points'][0]['location']['longitude']
    return [lat,long]


#print(getLocation("123 Front Street Toronto"))