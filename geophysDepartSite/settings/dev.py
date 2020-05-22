from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gp$m9796!a33q=5um2^xrw(hmc424gmlcf+x#14fqhw)akv=*='

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# INSTALLED_APPS = INSTALLED_APPS + [
#     ,
# ]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


INTERNAL_IPS = [
    '127.0.0.1',
]


try:
    from .local import *
except ImportError:
    pass
