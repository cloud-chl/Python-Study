

class BaseConfiguration():
    DEBUG = True

    # sqlite
    # DB_URI = 'sqlite:///sqlite3.db'
    # SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mysql
    USERNAME = 'root'
    PASSWORD = 'admin@123'
    HOSTNAME = 'localhost'
    PORT = '3306'
    DATABASE = 'flask-demo1'
    # mysql+pymysql://USERNAME:PASSWORD@HOSTNAME:PORT/DATABASE
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        USERNAME,
        PASSWORD,
        HOSTNAME,
        PORT,
        DATABASE
    )

