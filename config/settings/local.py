from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': get_secret("DB_NAME"),
    'USER': get_secret("DB_USER"),
    'PASSWORD': get_secret("DB_PASSWORD"),
    'HOST': '127.0.0.1',
    'PORT': '5432', }

}

ACCOUNT_EMAIL_VERIFICATION = 'optional'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')