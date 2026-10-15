"""Configuración WSGI del proyecto huertos."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'huertos.settings')

application = get_wsgi_application()
