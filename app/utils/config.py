import os
from dotenv import load_dotenv


load_dotenv(".env")

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MONGO_URI = os.environ.get("MONGO_URI")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    TESTING = False
    DEBUG = False

    # Create development config
    if FLASK_ENV == "development":
        DEBUG = True
        
    # Create the testing config
    if FLASK_ENV == "testing":
        DEBUG = False
        TESTING = True

    # create the production config
    if FLASK_ENV == "production":
        DEBUG = False
