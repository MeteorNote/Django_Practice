
from .base import *

env = environ.Env(
	DEBUG=(bool, False)
)


# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', '0.0.0.0:8000', 'localhost', '127.0.0.1', '192.168.108.4']

def read_secret(secret_name):
  file = open('/run/secrets/' + secret_name)
  secret = file.read()
  secret = secret.rstrip().lstrip()
  file.close()
  return secret


SECRET_KEY = read_secret('DJANGO_SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": "django",
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}

