from .base import *


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': conf('DJANGO_LOG_LEVEL', default='ERROR'),
        },
    },
}

DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = conf('ALLOWED_HOSTS').split(',')

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(
    conn_max_age=500, ssl_require=True))
