# Django Router

Inspired by [Minimal Django](https://olifante.blogs.com/covil/2010/04/minimal-django.html), this simple Django project contains the bare minimum settings needed to render a few views and templates. No database backend is configured.

The project also takes inspiration from the article and provides a simple Flask-like decorator for routes, where a view function is tightly coupled to a URL path. Use it like so:

```py
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from router import Router

urlpatterns = Router()

@urlpatterns.add_route("hello-world")
def hello_world(request: HttpRequest) -> HttpResponse:
    return render("hello_world.html")
```

It’s not going to set the world on fire, but it was fun to setup and I learned some things along the way.

## Running the project

Django Router was written to use Python 3.11, but it may be compatible with other versions with a bit of tweaking. Assuming `python3.11` is available in your `$PATH`:

```sh
# Clone the repo
git clone git@github.com:liamnewmarch/django-router.git
cd django-router

# Create a virtual environment
python3.11 -m venv venv
. venv/bin/activate

# Install the dependencies (Django)
pip install -r requirements.txt
```

You might notice there’s no `manage.py`. I wrote the project with the intention of running it on Google App Engine and decided to combine the CLI and WSGI entrypoints into `main.py`. To run the project, pass `main` as a module:

```sh
python -m main runserver
```

## Running the tests

There are also some basic tests. These can be run with:

```sh
python -m main test
```
