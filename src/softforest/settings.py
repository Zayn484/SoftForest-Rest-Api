

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hd_+ioog^9rv3jdzqd3wq&8=a6pm%mu=@x+fmg49is0r5ut7(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['ec2-3-19-73-166.us-east-2.compute.amazonaws.com']

# User model
AUTH_USER_MODEL = 'accounts.User'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    # 'allauth',
    # 'allauth.socialaccount',
    # 'rest_auth.registration',
    # 'rest_auth',
    # 'notifications',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_multiple_model',
    'corsheaders',
    'channels',
    'django_filters',
    'import_export',
    'django_extensions',

    # Our apps
    'accounts',
    'chat',
    'carts',
    'comments',
    'earnings',
    'modificationrequests',
    'projects',
    'orders',
    'tags',
    'teams'

]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'softforest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'mathtags': 'earnings.templatetags.mathtags',

            }
        },
    },
]

WSGI_APPLICATION = 'softforest.wsgi.application'
ASGI_APPLICATION = "softforest.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

STATICFILES_DIR = [
    os.path.join(BASE_DIR, "static_my_proj")

]

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "static_cdn", "static_root")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "static_cdn", "media_root")

PROTECTED_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "static_cdn", "protected_media")

DATA_UPLOAD_MAX_MEMORY_SIZE = 150000000  # 150 MB

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.AllowAny',
    ]
}

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'accounts.serializers.TokenSerializer',
}

CORS_ORIGIN_ALLOW_ALL = True


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'softforest484@gmail.com'
EMAIL_HOST_PASSWORD = 'Nnnnn90@'
EMAIL_PORT = 587 # Tried 465 as mentioned in;
EMAIL_USE_TLS = True
EMAIL_BACKENDS = 'django.core.mail.backends.smtp.EmailBackend'
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True

