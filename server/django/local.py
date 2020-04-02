IS_SSL_SERVER = True
DOMAIN = 'https://ng-dating-test.webmonstr.com'
SOCKET_SERVER = 'https://dating-test.webmonstr.com:8888'
#EMAIL_HOST = 'dating-service.top'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'info@dating-service.top'
#EMAIL_HOST_PASSWORD = '0632291tom'
#EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'polikovskaaalina@gmail.com'
EMAIL_HOST_PASSWORD = '7q0ZoPa@A0Ic'
EMAIL_USE_TLS = True
FRONTEND_DOMAIN='http://dating-test.webmonstr.com'


'''
Host: dating-service.top | 185.235.130.153
Login: dating-service.top-vmta
Email: info@dating-service.top
Pass: 0632291tom
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dating',
        'USER': 'postgres',
        'PASSWORD': 'slavakpss1918',
        'HOST': 'localhost',
    }
}