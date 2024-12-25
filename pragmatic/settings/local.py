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
DEBUG = True

ALLOWED_HOSTS = ['*', '0.0.0.0:8000', 'localhost', '127.0.0.1', '192.168.108.4']



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.mysql",
#        "NAME": "BASE_DIR / kdlee",
#        "USER": "kdlee",
#        'PASSWORD': 6570,
#        "HOST": "mariadb",
#        "PORT": "3306",
#    }
#}