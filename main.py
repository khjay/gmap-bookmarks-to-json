import json
from argparse import ArgumentParser
from bookmark import bookmark as bk

def main():
    args = load_argvs()

    db_disable = True if args.disable_db else False
    
    bookmark = bk.Bookmark(args.path, db_disable)
    bookmark.sync_db()

    print (json.dumps(bookmark.restaurants, ensure_ascii=False, indent=4))

def load_argvs():
    parser = ArgumentParser()
    parser.add_argument('path', help='bookmark html file download from: https://www.google.com/bookmarks/')
    parser.add_argument("--disable-db", help="disable firestore db connect.", dest="disable_db", default=True, action='store_false')

    return parser.parse_args()

if __name__ == '__main__':
    main()
