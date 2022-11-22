"""
WSGI config for django_web_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

#!/usr/bin/env python
try:
    import tracepointdebug
    tracepointdebug.start()
except ImportError as e:
    pass
    
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web_app.settings')

application = get_wsgi_application()
