import os
import dj_database_url
from pathlib import Path


# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Security Settings
# Render-এ SECRET_KEY এনভায়রনমেন্ট ভ্যারিয়েবল থাকলে সেটা নেবে, না থাকলে ডিফল্টটি ব্যবহার করবে
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-later')

# Render-এ DEBUG মোড অটোমেটিক কন্ট্রোল করার ব্যবস্থা
DEBUG = os.environ.get('DEBUG', 'True') == 'True'


# Allowed Hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',  # Render-এর সকল সাব-ডোমেইন অ্যালাউ করবে
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
    'students',
    'courses',
    'enrollments',
]


# Middleware Configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for serving static files efficiently on Render
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL configuration
ROOT_URLCONF = 'config.urls'


# Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates',
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI Server Application
WSGI_APPLICATION = 'config.wsgi.application'


# Database Configuration
# Render-এ DATABASE_URL থাকলে PostgreSQL সংযোগ করবে, লোকাল পরিবেশে SQLite3 ব্যবহার করবে
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# Password validation
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


# Internationalization & Timezone
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Render-এ `python manage.py collectstatic` কমান্ডের মাধ্যমে ফাইল জমা হওয়ার ডিরেক্টরি
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise storage optimization
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication URLs
LOGIN_URL = '/admin/login/'