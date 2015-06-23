from rsvp.settings.base import *


SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

X_FRAME_OPTIONS = 'ALLOW-FROM sunahandlaura.com'

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
)
