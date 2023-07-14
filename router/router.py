from django.urls import path


class Router:
    urlpatterns: list

    def add_route(self, route: str, *args, **kwargs):
        """Wraps or decorates a view, adding it to urlpatterns."""

        def view_wrapper(view):
            self.urlpatterns.append(path(route, view, *args, **kwargs))

        return view_wrapper

    def __init__(self):
        self.urlpatterns = []

    def __iter__(self):
        yield from self.urlpatterns
