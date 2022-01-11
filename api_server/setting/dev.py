import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
  'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ph2020",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3306"
    }
}
