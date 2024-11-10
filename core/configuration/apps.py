from core.configuration.base import DEBUG

PRELOADED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',  # https://django-extensions.readthedocs.io/en/latest/
    'fsm_admin',  # https://django-fsm.readthedocs.io/en/latest/
    'django_filters',
    'django_fsm',
    'import_export',
    'fcm_django',
    'django_celery_results',
    'django_celery_beat',
    'reversion',
    'django_object_actions',
    'translation_manager',
    'ckeditor',
    'drf_spectacular',
   
    
]

LOCAL_APPS = [    

   
    
]

THEMES = [
    "baton",
]

LAST_APPS = [
    "baton.autodiscover",
]