from Core.Settings.base import *

DEBUG = False

ALLOWED_HOSTS = list(os.getenv('ALLOWED_HOSTS', []).split(','))
