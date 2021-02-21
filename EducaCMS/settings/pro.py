"""Настройки, специфичные для продакшена"""

from .base import *

DEBUG = True

ADMINS = (
    ('Roman S', 'speccy.rom@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {'default': {}
             }
