from django.test import SimpleTestCase
from django.urls import URLPattern
from django.views import View

from router import Router


class RouterTestCase(SimpleTestCase):
    def test_create_router(self):
        router = Router()
        self.assertListEqual(router.urlpatterns, [])

    def test_add_route_decorator(self):
        router = Router()

        @router.add_route("foo")
        def foo(request): pass

        self.assertIsInstance(router.urlpatterns[0], URLPattern)

    def test_add_route_decorator_with_keyword_arguments(self):
        router = Router()

        @router.add_route("bar", name="bar")
        def bar(request): pass

        self.assertEqual(router.urlpatterns[0].name, "bar")

    def test_add_route_wrap_view(self):
        router = Router()

        class Baz(View): pass

        router.add_route("baz")(Baz.as_view())

        self.assertEqual(len(router.urlpatterns), 1)
        self.assertIsInstance(router.urlpatterns[0], URLPattern)
