import os
from .base import *

DEBUG = TRUE

ALLOWED_HOSTS = ['*']

DATABASES = {
  'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ph2020",
        "USER": "root",
        "PASSWORD": "theo93",
        "HOST" : "localhost",
        "PORT": "3306"
    }
}
