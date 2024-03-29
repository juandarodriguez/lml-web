from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(h*5oz!c06tbf+++&*c-thxhna%+fk*y@a&o@8q!5h&_xnhv=_'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LEARNING_ML_URL = 'http://localhost:4200'


try:
    from .local import *
except ImportError:
    pass
