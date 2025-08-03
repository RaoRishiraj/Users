"""
WSGI config for user_api_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJ_REST_AUTH_TOKEN_MODEL', 'None')  # Add this line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_api_project.settings')

application = get_wsgi_application()
