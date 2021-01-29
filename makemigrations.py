#!/usr/bin/env python
import os
import sys

import django

from django.conf import settings


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "zerxis_account",
        "zerxis.invitations",
        "zerxis.invitations.tests"
    ],
    MIDDLEWARE_CLASSES=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    SITE_ID=1,
    ROOT_URLCONF="zerxis.invitations.tests.urls",
    SECRET_KEY="notasecret",
)


def run(*args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    django.core.management.call_command(
        "makemigrations",
        "zerxis_invitations",
        *args
    )


if __name__ == "__main__":
    run(*sys.argv[1:])
