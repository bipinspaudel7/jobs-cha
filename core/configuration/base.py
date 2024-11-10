from decouple import config

SECRET_KEY = config('SECRET_KEY', default='')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ["*"]

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"


