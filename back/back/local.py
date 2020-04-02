IS_SSL_SERVER = False
DOMAIN='http://localhost:8001'
import os
from .settings import BASE_DIR

POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.getenv('POSSTGRES_DB', 'neuro')
POSTGRES_PASSWORD = os.getenv('POSSTGRES_PASSWORD', '1q2w3e')
POSTGRES_USER = os.getenv('POSSTGRES_USER', 'postgres')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
    }
}

EMAIL_HOST_USER = 'admin@localhost'