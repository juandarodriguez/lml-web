from .base import *

DEBUG = False

LEARNING_ML_URL = 'http://learningml.org'

try:
    from .local import *
except ImportError:
    pass
