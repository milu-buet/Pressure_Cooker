DEBUG = True
USE_TZ = True
TIME_ZONE = 'Asia/Dhaka'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pr',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'PressureCooker',
        'PASSWORD': 'root',
        'HOST': 'mysql.server',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


from settings import *