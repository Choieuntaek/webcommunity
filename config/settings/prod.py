from .base import *

ALLOWED_HOSTS = ['x.xx.xxx.xx']
DEBUG = False
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': get_secret("DB_NAME"),
    'USER': get_secret("DB_USER"),
    'PASSWORD': get_secret("DB_PASSWORD"),
    'HOST': '127.0.0.1',
    'PORT': '5432', }

}

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE =True

AWS_ACCESS_KEY_ID = get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_secret("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_secret("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = get_secret("AWS_S3_REGION_NAME")
AWS_S3_HOST = get_secret("AWS_S3_HOST")
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}
DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'
MEDIA_URL = 'https://%s/%s/media/' % (AWS_S3_HOST, AWS_STORAGE_BUCKET_NAME)
AWS_QUERYSTRING_AUTH = False