import json
from argparse import ArgumentParser
from bookmark import bookmark as bk

def main():
    args = load_argvs()
    
    bookmark = bk.Bookmark(args.path)
    bookmark.sync_db()

    print (json.dumps(bookmark.restaurants, ensure_ascii=False, indent=4))

def load_argvs():
    parser = ArgumentParser()
    parser.add_argument('path', help='bookmark html file download from: https://www.google.com/bookmarks/')

    return parser.parse_args()

if __name__ == '__main__':
    main()