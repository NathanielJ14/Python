from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.model_email import Email

#Display Route
@app.route("/")
def user_new():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def save_info():
    if not Email.validate_user(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')


@app.route('/success')
def result():
    all_emails = Email.get_all()
    return render_template("success.html", all_emails = all_emails)




