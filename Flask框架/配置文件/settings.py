class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "qweasdzxc"


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True