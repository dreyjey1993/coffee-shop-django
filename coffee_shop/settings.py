import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY: Keep secret key in env var for production
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-only')

# DEBUG: false in production (PythonAnywhere sets DJANGO_SETTINGS_MODULE)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allowed hosts: PythonAnywhere domain
ALLOWED_HOSTS = ['.pythonanywhere.com']

# Database (SQLite on PythonAnywhere, can switch to Postgres later)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (collected to staticfiles dir)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Optional: Media files (if you upload images later)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
