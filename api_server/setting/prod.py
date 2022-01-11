import os
import json
from .base import *

DEBUG = False

ALLOWED_HOSTS = "*"
DATABASES = {
  'default': secrets['DB_SETTINGS']
}
