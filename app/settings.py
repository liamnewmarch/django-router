import os

from django.core.management.utils import get_random_secret_key


DEBUG = os.environ.get("DJANGO_DEBUG") is not None
if not DEBUG:
    ALLOWED_HOSTS = ("*",)
ROOT_URLCONF = "app.routes"
SECRET_KEY = get_random_secret_key()
TEMPLATES = (
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ("templates",),
    },
)
