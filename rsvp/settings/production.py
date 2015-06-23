from rsvp.settings.base import *


SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

X_FRAME_OPTIONS = 'ALLOW-FROM sunahandlaura.com'

import dj_database_url
DATABASES['default'] = dj_database_url.config()

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
