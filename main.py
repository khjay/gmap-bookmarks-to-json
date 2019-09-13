import json
from lxml.html import parse
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('path', help='bookmark html file download from: https://www.google.com/bookmarks/')

args = parser.parse_args()

page = parse(args.path).getroot()

tags = []
for tag in page.xpath('//dt/a'):
    url = tag.attrib['href']

    if 'cid' not in url:
        continue

    tags.append({
        'name': tag.text, 
        'url': url,
        'created_at': int(tag.attrib['add_date'][:-6])
    })

print (json.dumps(tags, ensure_ascii=False))