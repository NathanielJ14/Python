from flask_app import app, bcrypt
from flask import render_template, session, request, redirect, flash
from flask_app.models.model_user import User
#Must import model but make sure you change the name


#Display Route
@app.route("/")
def main_page():
	return render_template("index.html")


@app.route("/process", methods=["POST"])
def save_info():
	if not User.validate_user(request.form):
		return redirect('/')

	hash_password = bcrypt.generate_password_hash(request.form['password'])

	data = {
		**request.form,
		'password': hash_password
	}

	id = User.save(data)
	session['uuid'] = id 
	return redirect("/success")


@app.route("/success")
def show_user():
	if 'uuid' not in session:
		return redirect('/')
	user = User.get_one({'id': session["uuid"]})
	return render_template("success.html", user = user)

@app.route("/logout")
def log_out():
	session.clear()
	return redirect("/")


@app.route("/user/login", methods=["post"])
def user_login():
	if not User.validator_login(request.form):
		return redirect("/")

	return redirect("/success")
