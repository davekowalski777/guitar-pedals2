import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guitar_pedals.settings")

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from whitenoise import WhiteNoise

application = get_wsgi_application()
application = WhiteNoise(application)
application.add_files(settings.STATIC_ROOT, prefix="static/")

app = application
