# Google Bookmarks to Json

This project can convert bookmarks from: [https://www.google.com/bookmarks/](https://www.google.com/bookmarks/) to json format and ignore url which without `cid` parameter.

## Install Dependencies:

``` bash
$ pipenv install
```

## How to run

1. Set your [Cloud Firestore Admin SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk)

``` bash
$ export GOOGLE_APPLICATION_CREDENTIALS=project-admin-sdk.json
```

2. Make sure execute main.py under pipenv shell environment

``` bash
$ pipenv shell
$ python main.py ~/GoogleBookmarks.html
```

## Json Format

```
[
    {
        "name": "王記北京爆烤鴨",
        "url": "http://maps.google.com/?cid=9484141642952184264",
        "cid": "9484141642952184264",
        "created_at": 1568358485
    }
]
```
