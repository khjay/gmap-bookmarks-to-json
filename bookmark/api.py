import os, json
import requests

class GooglePlace:
    def __init__(self):
        self.key = os.environ['GOOGLE_KEY']
        self.fields = 'name,rating,opening_hours,geometry,photo,place_id'
        self.HOST = 'https://maps.googleapis.com/maps/api/place/details/json'

    def find(self, cid):
        params = {'cid': cid, 'fields': self.fields, 'key': self.key}
        response = requests.get(self.HOST, params = params)

        place = json.loads(response.text)['result']

        restaurant = {
            'name': place['name'],
            'cid': cid,
            'location': place['geometry']['location'],
            'place_id': place['place_id'],
            'opening_hours': {}
        }

        for period in place['opening_hours']['periods']:
            day = period['close']['day']
            restaurant['opening_hours'][day] = {
                'close': period['close']['time'],
                'open': period['open']['time']
            }

        return restaurant
