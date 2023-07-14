from django.test import SimpleTestCase


class IndexRouteTestCase(SimpleTestCase):
    def test_index_route(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)


class FooRouteTestCase(SimpleTestCase):
    def test_foo_route_with_default_name(self):
        response = self.client.get("/foo")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["name"], "foo")
        self.assertContains(response, "Hello, foo")

    def test_foo_route_with_custom_name(self):
        response = self.client.get("/foo?name=blah")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["name"], "blah")
        self.assertContains(response, "Hello, blah")

        response = self.client.get("/foo?name=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["name"], "")
        self.assertContains(response, "Hello, ")
