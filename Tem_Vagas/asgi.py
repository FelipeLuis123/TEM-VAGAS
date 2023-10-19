"""
ASGI config for Tem_Vagas project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""


import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tem_Vagas.settings')

application = Cling(MediaCling(get_wsgi_application()))
