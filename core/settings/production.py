# flake8: noqa

import os

from .base import *

DEBUG = False
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost").split(",")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'landing_prod'),
        'USER': os.getenv('POSTGRES_USER', 'landing_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'landing_pass'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
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
