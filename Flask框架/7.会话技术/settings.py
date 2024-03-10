import datetime

class BaseConfigure():
    DEBUG = True
    SECRET_KEY = 'qweasd'
    SESSION_EXPRIES = datetime.datetime(2024, 4, 10)
    # SESSION_MAX_AGE = 3600 * 7 * 30