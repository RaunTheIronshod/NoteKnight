from pathlib import Path
import os
import dj_database_url
from decouple import config
import sys

# ---------------------------------------------------------
# CORE PATHS
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------
# SECURITY SETTINGS
# ---------------------------------------------------------
SECRET_KEY = config('SECRET_KEY')

ADMIN_REGISTRATION_KEY = config("ADMIN_REGISTRATION_KEY")

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "noteknight-1e2cee381e80.herokuapp.com",
    "noteknight.herokuapp.com",
    ".herokuapp.com",
]

# ---------------------------------------------------------
# CSRF TRUSTED ORIGINS
# ---------------------------------------------------------

CSRF_TRUSTED_ORIGINS = [
    "https://noteknight-1e2cee381e80.herokuapp.com",
    "https://noteknight.herokuapp.com",
    "https://*.herokuapp.com",
]


# ---------------------------------------------------------
# APPLICATIONS
# ---------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',

    # my apps
    'notes',
]

# ---------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for static file handling
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------------------------------------
# URLS / WSGI
# ---------------------------------------------------------
ROOT_URLCONF = 'noteknight.urls'
WSGI_APPLICATION = 'noteknight.wsgi.application'

# ---------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# ---------------------------------------------------------
# DATABASE CONFIGURATION
# ---------------------------------------------------------

# Default local development DB (NO SSL)
LOCAL_DB = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'noteknight_db',
    'USER': 'postgres',
    'PASSWORD': config('DB_PASSWORD', default='District9'),
    'HOST': 'localhost',
    'PORT': '5432',
}

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default=os.environ.get('DATABASE_URL')),
        conn_max_age=600,
        ssl_require=True
    )
}


# ---------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# INTERNATIONAL SETTINGS
# ---------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise for serving static files in production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---------------------------------------------------------
# AUTH REDIRECTS
# ---------------------------------------------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# ---------------------------------------------------------
# DEFAULT PK
# ---------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ---------------------------------------------------------
# LOGGING CONFIGURATION
# ---------------------------------------------------------
LOGGING = {
    'version': 1,  # Required: specifies the logging schema version

    # HANDLERS: define where log messages go
    'handlers': {
        'console': {  # This handler sends log messages to the console (stdout)
            'class': 'logging.StreamHandler',  # Uses Python's standard StreamHandler
        },
    },

    # ROOT LOGGER: the default logger for the project
    'root': {
        'handlers': ['console'],  # Sends all root logger messages to console
        'level': 'INFO',          # Minimum log level to handle
                                  
    },
}

if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',  # in-memory database for fast tests
        }
    }
