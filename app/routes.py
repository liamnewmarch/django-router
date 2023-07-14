from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from router import Router


urlpatterns = Router()


@urlpatterns.add_route("")
def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse("<p>This is the index</p>"
                        '<p><a href="/foo">Visit page foo</a></p>')


@urlpatterns.add_route("foo")
def foo(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name", "foo")
    return render(request, "index.html", {"name": name})
