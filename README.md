# URL Reader

## installation and Startup

1. Get API key from "Google CloudVision".

2. rename file.

```
$ cd urlreader/results
$ mv sample_APIkey.json APIkey.json
```

3. write on the file for "urlreader/results/APIkey.json".

```
{
    "APIkey": "insert your API key"
}
```

4. comment out config.

`$ $EDITOR urlreader/settings.py`

```
ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["insert your domain or address."]
~ ~ ~
# STATIC_ROOT = "static"
STATIC_ROOT = "static"
```

5. run your terminal command.

```
$ pip install -r requirements.txt
$ cd urlreader ; python manage.py collectstatic
$ uwsgi --http :8000 --wsgi-file urlreader/wsgi.py
```

6. test server. (optional)

**Do not use when releasing.**

`$ python manage.py runserver`

## development environmental

* Python 3
* Django 2.2.7
* uWSGI

