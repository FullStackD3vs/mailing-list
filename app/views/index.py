from flask import Blueprint, request, render_template
from app.db import subscribe, unsubscribe
from app.services.mail import send_welcome_mail

index = Blueprint("index", __name__, url_prefix="/")

@index.route("/", methods=['GET', 'POST'])
def get_index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            subscribe(name, email)
            send_welcome_mail(name, email)
            return render_template('success.html')
        except Exception as E:
            raise E
            return render_template('failure.html')

    return render_template('index.html')


@index.post("/unsubscribe")
def post_unsubscribe():
    body = request.get_json()
    email = body["email"]

    unsubscribe(email)
    return "", 204


@index.get("/unsubscribe")
def get_unsubscribe():
    args = request.args
    email = args.get("email")
    unsubscribe(email)
    return render_template("unsubscribe.html"), 200
