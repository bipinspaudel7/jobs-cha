import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR / 'core'
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(str(BASE_DIR), 'apps'))
from core.configuration.apps import (
    LOCAL_APPS,
    PRELOADED_APPS,
    THIRD_PARTY_APPS,
    THEMES,
    LAST_APPS,
)

import firebase_admin
from firebase_admin import credentials
from core.configuration.auth import *  # noqa F403
from core.configuration.base import *  # noqa F403
from core.configuration.celery import *  # noqa F403
from core.configuration.email import *  # noqa F403
from core.configuration.rest import *  # noqa F403
from core.configuration.translation import *  # noqa F403
from core.configuration.firebase import *  # noqa F403
from core.configuration.baton import *  # noqa F403
# added for otp 
from core.configuration.otp import *


# Application definition
INSTALLED_APPS = THEMES + PRELOADED_APPS + THIRD_PARTY_APPS + LOCAL_APPS + LAST_APPS
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hijack.middleware.HijackUserMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
SQLITE_DB_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}
# POSTGRES_DB_CONFIG = {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': config('POSTGRES_DB', cast=str),
#     'USER': config('POSTGRES_USER', cast=str),
#     'PASSWORD': config('POSTGRES_PASSWORD', cast=str),
#     # https://stackoverflow.com/a/70633902
#     # Why db is kept instead of localhost ?
#     'HOST': 'localhost',
#     'PORT': 5432,
# }
DATABASES = {'default': SQLITE_DB_CONFIG}
if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {'default': SQLITE_DB_CONFIG}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kathmandu'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'assets' / 'static_serve'

MEDIA_ROOT = BASE_DIR / 'assets' / 'media_serve'
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Cors
CORS_ALLOW_ALL_ORIGINS = True

# # firebase admin
# FIREBASE_CONFIG = BASE_DIR / 'firebase.json'
# cred = credentials.Certificate(FIREBASE_CONFIG)
# firebase_admin.initialize_app(cred)
