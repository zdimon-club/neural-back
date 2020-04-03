IS_SSL_SERVER = False
DOMAIN='http://localhost:8085'
SOCKET_SERVER='http://localhost:8888'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
import os
from .settings import BASE_DIR
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/mail')
FRONTEND_DOMAIN='http://localhost:4200'



"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alexdating',
        'USER': 'postgres',
        'PASSWORD': '1234567',
        'HOST': 'localhost',
    }
}


