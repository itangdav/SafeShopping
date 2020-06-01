import populartimes
from queue import PriorityQueue
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
import geocoder

# Global Variables Set To Defaults
API_KEY = "AIzaSyD1K9pwhTtcTS7yidUdNRSHfTxT-0AsK8c"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# This class defines what a store is
class store:
    def __init__(self, name, address, lat, long, store_id, popularity, score, WEIGHT_DISTANCE, WEIGHT_POPULARITY, LAT,
                 LONG):
        self.name = name
        self.address = address
        self.lat = lat
        self.long = long
        self.id = store_id
        self.popularity = int(popularity)
        self.score = score
        self.weight_distance = WEIGHT_DISTANCE
        self.weight_popularity = WEIGHT_POPULARITY
        self.setSafetyScore(LAT, LONG)

    def setSafetyScore(self, LAT, LONG):
        self.score = self.weight_popularity * self.popularity + self.weight_distance * self.distance(LAT, LONG)

    def __cmp__(self, other):
        return self.score - other.score

    def __lt__(self, other):
        return (self.score - other.score) < 0

    def __str__(self):
        return self.name + ": " + str(self.score)

    # Returns distance in km
    def distance(self, LAT, LONG):
        long1 = radians(self.long)
        long2 = radians(LONG)
        lat1 = radians(self.lat)
        lat2 = radians(LAT)

        dlong = long2 - long1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2

        c = 2 * asin(sqrt(a))
        r = 6371
        return (c * r)


def getResults(LAT, LONG, RADIUS, WEIGHT_DISTANCE, WEIGHT_POPULARITY, type_of_place):
    # Get Date
    NOW = datetime.now()
    DAY_OF_WEEK = WEEKDAYS[datetime.today().weekday()]
    HOUR_OF_DAY = int(NOW.strftime("%H"))

    # Gets set of nearby stores
    nearby_store_data = populartimes.get(API_KEY, type_of_place, (LAT - RADIUS, LONG - RADIUS),
                                         (LAT + RADIUS, LONG + RADIUS))

    Place_IDs = []

    for place in nearby_store_data:
        Place_IDs.append(place['id'])

    processed_data = []

    for curr_id in Place_IDs:

        store_data = populartimes.get_populartimes(API_KEY, curr_id)
        if 'populartimes' in store_data:
            if 'current_popularity' in store_data:
                isClosed = store_data['current_popularity'] == "0"
                if not isClosed:
                    processed_data.append(
                        store(store_data['name'], store_data['address'], store_data['coordinates']['lat'],
                              store_data['coordinates']['lng'],
                              store_data['id'], store_data['current_popularity'], 0, WEIGHT_DISTANCE, WEIGHT_POPULARITY,
                              LAT, LONG))
            else:
                for date in store_data['populartimes']:
                    if date['name'] == DAY_OF_WEEK:
                        isClosed = str(date['data'][HOUR_OF_DAY]) == "0"
                        if not isClosed:
                            processed_data.append(
                                store(store_data['name'], store_data['address'], store_data['coordinates']['lat'],
                                      store_data['coordinates']['lng'],
                                      store_data['id'], str(int(date['data'][HOUR_OF_DAY])), 0, WEIGHT_DISTANCE,
                                      WEIGHT_POPULARITY, LAT, LONG))
                            break
                        else:
                            break

    # fake_store_tester_data_1 = store("Metro", '735 College St, Toronto, ON M6G 1C5, Canada', 43.6541827, -79.4194143,
    #                                  'ChIJ7fBhKPE0K4gRLDLhCYYsWVk', "3", 0, WEIGHT_DISTANCE, WEIGHT_POPULARITY, LAT, LONG)
    # fake_store_tester_data_2 = store("Metro2", '123 Somewhere St, Toronto, ON M6G 1C5, Canada', 43.0541827, -78.4194143,
    #                                  'FakeID', "10", 0, WEIGHT_DISTANCE, WEIGHT_POPULARITY, LAT, LONG)
    # processed_data.append(fake_store_tester_data_1)
    # processed_data.append(fake_store_tester_data_2)

    sorted_data_queue = PriorityQueue()
    for curr_store in processed_data:
        sorted_data_queue.put(curr_store)
    sorted_data = []

    while sorted_data_queue:
        if not sorted_data_queue.empty():
            temp = sorted_data_queue.get()
            sorted_data.append(temp)
        else:
            break

    # Convert to dictionary

    sorted_data_dictionary_form = []

    for curr_store in sorted_data:
        curr_dict = {
            "name": curr_store.name,
            "address": curr_store.address,
            "lat": curr_store.lat,
            "long": curr_store.long,
            "id": curr_store.id,
            "popularity": curr_store.popularity,
            "score": curr_store.score,
        }
        sorted_data_dictionary_form.append(curr_dict)

    return sorted_data_dictionary_form


# main
g = geocoder.ip('me')
lat = g.latlng[0]
long = g.latlng[1]
radius = 0.016  # Radius is in latitude or longitude angles
weight_distance = 5.0
weight_popularity = 1.0
type_of_place = ['grocery_or_supermarket']

#print(getResults(lat, long, radius, weight_distance, weight_popularity, type_of_place))