"""Entrypoints for Google App Engine and the command line."""

import os
import sys

from logging import Logger


logger = Logger(__name__)


if __name__ == "__main__":
    if os.environ.get("GAE_INSTANCE"):
        raise EnvironmentError(
            "GAE_INSTANCE is set. Refusing to run the development server in a "
            "possible production environment."
        )

    from django.core.management import execute_from_command_line

    logger.info("Running as a command line application")

    os.environ.setdefault("DJANGO_DEBUG", "true")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    execute_from_command_line(sys.argv)
else:
    from django.core.wsgi import get_wsgi_application

    logger.info("Running as a WSGI application")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    app = get_wsgi_application()  # Provides main.app for App Engine
