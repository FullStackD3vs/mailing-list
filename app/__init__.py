from flask import Flask
from flask_mail import Mail
from flask_pymongo import PyMongo
from flask_cors import CORS
from app.utils.config import Config

mail = Mail()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    mongo.init_app(app)
    
    # initialize flask mail extension 
    mail.init_app(app)
    mail.app = app

    
    # register blueprints
    from app.views.index import index
    from app.views.admin import admin

    app.register_blueprint(admin)
    app.register_blueprint(index)

    return app


