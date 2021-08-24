from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'u551789018_relevamiento',
        'USER': 'u551789018_agus_fer',
        'PASSWORD': 'Chizzo1991',
        'HOST': '185.201.11.212',   
        'PORT': '3306',
    }    
}

