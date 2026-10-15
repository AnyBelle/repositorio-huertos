"""Configuración ASGI del proyecto huertos."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'huertos.settings')

application = get_asgi_application()
