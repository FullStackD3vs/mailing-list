from flask import Blueprint, request, render_template
from app.services.mail import send_batch_emails

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        subject = request.form.get('subject')
        textContent =  request.form.get('textContent')
        htmlContent = request.form.get('htmlContent')

        print(subject, textContent, htmlContent)
        
        emailcontent = {"subject": subject, "textContent": textContent, "htmlContent": htmlContent}
        send_batch_emails(emailcontent)
        pass
    return render_template("admin.html")
