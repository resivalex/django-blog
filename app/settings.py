from app.dev_settings import *
import random
import string

DEBUG = False
SECRET_KEY = "".join(random.choices(string.ascii_uppercase + string.digits, k=32))


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
