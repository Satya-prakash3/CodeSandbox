"""
WSGI config for Core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from Core.Settings.base import DEBUG


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv('DJANGO_SETTINGS_MODULE', default="Core.Settings.dev"))

application = get_wsgi_application()
