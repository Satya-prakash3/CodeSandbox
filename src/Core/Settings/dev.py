from Core.Settings.base import *

DEBUG = True
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="*").split(",")


# Application definition
LOCAL_APPS = []

THIRD_PARTY_APPS = [
]

INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS


