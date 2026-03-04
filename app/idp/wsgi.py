"""
WSGI config for idp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from sys import stdout
from logging import basicConfig, DEBUG, StreamHandler

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idp.settings')

basicConfig(
    level=DEBUG,
    format='%(asctime)s - %(name)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s',
    handlers=[StreamHandler(stdout)],
)

application = get_wsgi_application()
