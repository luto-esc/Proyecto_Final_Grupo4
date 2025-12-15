from .base import *

#Todos lo de abajo es de base.py
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5r7m&ohp$rsbo%u$)ryckka#c!yd_ja(_wn3h1wdt!32se22_7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['chacoverde-9mg6.onrender.com']

#Esto es de base.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}