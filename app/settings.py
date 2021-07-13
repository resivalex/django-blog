from app.dev_settings import *
import random
import string

DEBUG = False
ALLOWED_HOSTS = ['resivalex.com']
SECRET_KEY = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
