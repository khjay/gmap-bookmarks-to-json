import os, sys

from lxml.html import parse

import urllib.parse as urlparse

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

class Bookmark:
    def __init__(self, path, disable_firestore = False):
        self.path = path
        self.disable_firestore = disable_firestore
        self.restaurants = self.convert_restaurants()

        self.db_client = None if disable_firestore else self.init_db_client()

    def init_db_client(self):
        if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
            sys.exit('env: GOOGLE_APPLICATION_CREDENTIALS is invalid')

        cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
        firebase_admin.initialize_app(cred)

        return firestore.client()

    def convert_restaurants(self):
        restaurants = []
        page = parse(self.path).getroot()

        for tag in page.xpath('//dt/a'):
            url = tag.attrib['href']

            if 'cid' not in url:
                continue

            parsed = urlparse.urlparse(url)
            cid = urlparse.parse_qs(parsed.query)['cid'][0]

            restaurant = {
                'name': tag.text, 
                'url': url,
                'cid': cid,
                'add_date': int(tag.attrib['add_date'][:-6]),
            }

            restaurants.append(restaurant)

        return restaurants

    def sync_db(self):
        if self.disable_firestore:
            return

        doc_ref = self.db_client.collection('restaurants')

        restaurants = self.restaurants[:]

        for restaurant in restaurants:
            restaurant['created_at'] = firestore.SERVER_TIMESTAMP
            doc_ref.document(restaurant['cid']).set(restaurant)
