import os

from environs import Env

env = Env()
env.read_env()
host = env('DB_HOST')
port = env.int('DB_PORT')
name = env('DB_NAME')
user = env('DB_USERNAME')
password = env('DB_PASSWORD')
secret_key = env('SECRET_KEY', 'SECRET_KEY')
debug = env.bool('DEBUG', False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = debug

ROOT_URLCONF = 'project.urls'

allowed_hosts = env.list('ALLOWED_HOSTS', [])
ALLOWED_HOSTS = [allowed_hosts]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
