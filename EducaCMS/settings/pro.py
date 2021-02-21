"""Настройки, специфичные для продакшена"""

from .base import *

DEBUG = True

ADMINS = (
    ('Roman S', 'speccy.rom@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'EducaCMS',
        'USER': 'EducaCMS',
        'PASSWORD': '123266',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
