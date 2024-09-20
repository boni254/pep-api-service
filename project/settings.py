from pathlib import Path

import dj_database_url
from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

BASE_DIR = Path(__file__).resolve().parent.parent

config_loaders = [Environment(), EnvFile()]

config = Configuration(loaders=config_loaders)

SECRET_KEY = config("DJANGO_SECRET_KEY")

DEBUG = config("DJANGO_DEBUG", default=False, cast=config.boolean)

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="*", cast=config.list)
CSRF_TRUSTED_ORIGINS = config("DJANGO_CSRF_TRUSTED_ORIGINS", default=[], cast=config.list)

AUTH_TOKEN = config("AUTH_TOKEN")

ENVIRONMENT = config("DJANGO_ENVIRONMENT", default="local")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "rest_framework",
    "app.anamnese",
    "app.core",
    "app.evolucao",
    "app.receituario",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {
    "default": dj_database_url.parse(config("DJANGO_DATABASE_URL"), conn_max_age=60),
}


LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / Path("static")
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}

LOGGER_LOG_LEVEL = config("DJANGO_LOGGER_LOG_LEVEL", default="INFO")

LOGGING_DICT = None

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": LOGGER_LOG_LEVEL,
            "propagate": False,
        },
    },
}

# Django REST Framework settings: https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "app.core.authentication.AuthToken",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

# API docs settings: https://drf-spectacular.readthedocs.io/en/latest/settings.html

SPECTACULAR_SETTINGS = {
    "TITLE": "PEP API Service",
    "DESCRIPTION": open(BASE_DIR / "docs/README_API.md").read(),
    "VERSION": "0.1.0",
    "SWAGGER_UI_SETTINGS": {
        "defaultModelsExpandDepth": 5,
        "defaultModelExpandDepth": 5,
        "persistAuthorization": True,
    },
}

RABBITMQ_HOST = config("RABBITMQ_HOST", default="localhost")
RABBITMQ_QUEUE = config("RABBITMQ_QUEUE", default="clinic")
