from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['coming soon']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PROD_DB_NAME'),
        'USER': os.environ.get('PROD_DB_USER'),
        'PASSWORD': os.environ.get('PROD_DB_PASSWORD'),
        'HOST': os.environ.get('PROD_DB_HOST'),
        'PORT': os.environ.get('PROD_DB_PORT'),
    }
}
