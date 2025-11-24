"""
Django settings for app project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath
from datetime import datetime as expiry


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "cb480bd8-7abf-4e5c-ae8e-1bf07b298900")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Detect if running in production (Render/Vercel) or local development
IS_PRODUCTION = os.environ.get("RENDER", None) is not None or os.environ.get("VERCEL", None) is not None

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,case-detector-rl21.onrender.com,.onrender.com").split(",")

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""
CORS settings for Vercel frontend and localhost
"""
CORS_ALLOWED_ORIGINS = [origin for origin in os.environ.get("CORS_ALLOWED_ORIGINS", "https://case-detector.vercel.app,http://localhost:8000,http://127.0.0.1:8000").split(",") if origin]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False  # Only allow specific origins
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# CSRF Settings for cross-origin
CSRF_TRUSTED_ORIGINS = [
    'https://case-detector.vercel.app',
    'https://case-detector-rl21.onrender.com',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Session settings for cross-origin
# Use secure cookies only in production (HTTPS), allow HTTP for local development
SESSION_COOKIE_SAMESITE = 'None' if IS_PRODUCTION else 'Lax'
SESSION_COOKIE_SECURE = IS_PRODUCTION  # True only on Render/Vercel
CSRF_COOKIE_SAMESITE = 'None' if IS_PRODUCTION else 'Lax'
CSRF_COOKIE_SECURE = IS_PRODUCTION  # True only on Render/Vercel

ROOT_URLCONF = 'app.urls'


# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '..', 'frontend', 'public'),      # Static HTML files
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,  # Disable template caching in debug mode
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

# Additional locations of static files for development
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'frontend', 'static'),   # Static assets (CSS, JS, images)
    os.path.join(BASE_DIR, '..', 'frontend', 'public'),   # Static HTML files
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


EXPIRY_DATE = None