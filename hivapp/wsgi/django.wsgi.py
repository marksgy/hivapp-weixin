"""
WSGI config for hivapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import django.core.handlers.wsgi

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hivapp.settings")
sys.stdout = sys.stderr

DEBUG = True
application = django.core.handlers.wsgi.WSGIHandler()
