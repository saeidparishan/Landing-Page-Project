# flake8: noqa

import os
from dotenv import load_dotenv
from .base import *

DEBUG = False
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost").split(",")

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
# Static & Media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            'format': '{"time":"{asctime}", "level":"{levelname}", "logger":"{name}", "msg":{message}}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/landing/requests.log',
            'maxBytes': 10 * 1024 * 1024,  # 10MB per file
            'backupCount': 5,
            'formatter': 'json',
        },
    },
    'loggers': {
        'landing.requests': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
