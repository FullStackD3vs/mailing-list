
from flask import current_app
from app import mongo

db = mongo.db

def get_email_list():
    mail_list = db.subscribers.find()
    return list(map(lambda user: {**user, "_id": str(user["_id"])}, list(mail_list)))

def subscribe(name , email):
    new_user = { 'name' : name, 'email' : email }
    response = db.subscribers.insert_one(new_user)
    return str(response.inserted_id)


def unsubscribe(user_email):
    response = db.subscribers.delete_one({ "email": user_email })
    return response.deleted_count
