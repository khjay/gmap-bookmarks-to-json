# Google Bookmarks to Json

This project can convert bookmarks from: [https://www.google.com/bookmarks/](https://www.google.com/bookmarks/) to json format and ignore url which without `cid` parameter.

## Install Dependencies:

``` bash
$ pipenv install
```


## How to run

Make sure you enter python environment shell already.

``` bash
$ pipenv shell
```

Then run it.

```
python main.py ~/GoogleBookmarks.html
```

## Json Format

```
[{
    'name': '王記北京爆烤鴨', 
    'url': 'http://maps.google.com/?cid=9484141642952184264', 'created_at': 1568358485
}]
```
