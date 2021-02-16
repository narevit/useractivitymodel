"""
WSGI config for useractivitymodel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('home/narendrayalamanchi/useractivitymodel/useractivitymodel')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'useractivitymodel.settings')

application = get_wsgi_application()