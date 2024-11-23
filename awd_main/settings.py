from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# The value of the config are stored 
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG', cast=bool) # the cast=bool, will change the 'True' -> string to True -> bool

# The * added to the list below is to enable domain work for the app
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    "crispy_bootstrap5", # installed: pip install crispy-bootstrap5
    'crispy_forms', # installed: pip install django-crispy-forms
    'dataentry',
    'emails',
    'uploads',
    'image_compression',
    'stockscrapper', # Adding the stockscrapping app
    'anymail' # this is used to add ESP like sendgrid API. pip install django-anymail
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'awd_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # templates for the apps
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

WSGI_APPLICATION = 'awd_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
    'awd_main/static',
] # this is useful during deployment

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# media files configuration 
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media' # then we go to the urls.py file to register it


# Setting for message in django
from django.contrib.messages import constants as messages

# Optional: You can customize message tags like this:
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# setting up the celery url
CELERY_BROKER_URL = 'redis://localhost:6379'  
# celery -A awd_main worker --loglevel=info --pool=solo 
# and use 'redis-server' to activate the redis


#  Email configuration in django
#  we could use Brevo API as shown below 

# EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
# ANYMAIL = {
#     "SENDINBLUE_API_KEY": config("SENDINBLUE_API_KEY"),
    
# }

# OR USE GMAIL SMTP BELOW
# The settings below is for the gmail smtp 
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD') # this will be the 16 digit APP password
EMAIL_USE_TLS = True


DEFAULT_FROM_EMAIL = 'olatunjiayomi18@gmail.com'
DEFAULT_TO_EMAIL = 'graciousfx@gmail.com'


# We cant just expose our email credetials to the world. We need to use
# the python-decouple package

# Django Cripsy form setting
CRISPY_TEMPLATE_PACK = 'bootstrap5'


# Adding more features and setting for the ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'height': 300,
    },
}

# The line of code below are needed for the ngrok like domain to work well
CSRF_TRUSTED_ORIGINS = ['https://699a-129-205-124-224.ngrok-free.app']
BASE_URL = 'https://699a-129-205-124-224.ngrok-free.app'
