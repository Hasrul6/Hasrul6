import os

class Config(object):
    environment = str(os.environ["FLASK_ENV"])
    if environment == 'development':
        ENGINE = str(os.environ["DB_ENGINE"])
        USERNAME = str(os.environ["DB_USERNAME"])
        PASSWORD = str(os.environ["DB_PASSWORD"])
        HOST = str(os.environ["DB_HOST"])
        PORT = str(os.environ["DB_PORT"])
        DATABASE = str(os.environ["DB_NAME"])
    else:
        ENGINE = str(os.environ["ENGINE"])
        USERNAME = str(os.environ["USERNAME"])
        PASSWORD = str(os.environ["PASSWORD"])
        HOST = str(os.environ["HOST"])
        PORT = str(os.environ["PORT"])
        DATABASE = str(os.environ["DATABASE"])
    SECRET_KEY = str(os.environ["SECRET_KEY"])
    SQLALCHEMY_DATABASE_URI = ENGINE + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    UPLOAD_FOLDER = str(os.environ["UPLOAD_FOLDER"])
    MAX_IMAGE_FILESIZE = int(os.environ["MAX_IMAGE_FILESIZE"]) * 1024 * 1024
