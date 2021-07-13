from app.dev_settings import *
import random
import string

DEBUG = False
SECRET_KEY = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
