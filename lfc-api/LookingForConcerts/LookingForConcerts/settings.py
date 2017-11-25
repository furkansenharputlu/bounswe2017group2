"""
Django settings for LookingForConcerts project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
import datetime
from datetime import timedelta
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL  = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_07*1$$@eyr(7e-my8phay&th0hgdzx=syk6#dh&f%epga9sjn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

'''
WE ADDED THESE
'''

ALLOWED_HOSTS = ['*']

# our customized user model
AUTH_USER_MODEL = "lfc_backend.RegisteredUser"

# Authentication backends
AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        #"allauth.account.auth_backends.AuthenticationBackend", # for login with social accounts
    )

# We are using token authentication (instead of session)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication', # for JWT auth
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

BASE_URL = '127.0.0.1:8000/'
LOGIN_URL = BASE_URL + 'login/'
#LOGIN_REDIRECT_URL = LOGIN_URL
#SOCIALACCOUNT_QUERY_EMAIL = True
#SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'SCOPE': ['email'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'METHOD': 'oauth2',
#         'VERIFIED_EMAIL': False
#     },
#     'spotify': {
#         'SCOPE': ['email'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'METHOD': 'oauth2',
#         'VERIFIED_EMAIL': False
#     }
# }


'''
WE ADDED THESE
'''
ADMIN_ENABLED = True

ADMINS = [('Kemal Berk Kocabagli', 'kberkkocabagli@gmail.com'),
          ('Haluk Alper Karaevli', 'hakaraevli@gmail.com'),
          ('Enes Hecan', 'eneshecan@gmail.com'),
         ]

# Application definition
SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # added
    # REST framework
    'rest_framework',
    #'rest_framework.authtoken',
    #'rest_auth',
    #'rest_auth.registration',
    'lfc_backend.apps.LfcBackendConfig', # our app!
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist', # for JWT tracking and blacklisting
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook', # authentication with Facebook account
    # 'allauth.socialaccount.providers.spotify', # authentication with Spotify account
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LookingForConcerts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.contrib.auth.context_processors.auth',
                # 'django.template.context_processors.debug',
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
                # 'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

WSGI_APPLICATION = 'LookingForConcerts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# we are using sqllite
# might change in the future if concurrent access or more scalability is required
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Update database configuration with $DATABASE_URL
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

CORS_ORIGIN_ALLOW_ALL = True

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
