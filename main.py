import json
import os, sys
from argparse import ArgumentParser

from lxml.html import parse

import urllib.parse as urlparse

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
    sys.exit('env: GOOGLE_APPLICATION_CREDENTIALS is invalid')

parser = ArgumentParser()
parser.add_argument('path', help='bookmark html file download from: https://www.google.com/bookmarks/')

args = parser.parse_args()

page = parse(args.path).getroot()

cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection('restaurants')

restaurants = []

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
        'created_at': int(tag.attrib['add_date'][:-6])
    }

    restaurants.append(restaurant)

    doc_ref.document(cid).set(restaurant)

print (json.dumps(restaurants, ensure_ascii=False))