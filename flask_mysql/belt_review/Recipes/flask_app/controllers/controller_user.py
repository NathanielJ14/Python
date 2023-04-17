from flask_app import app, bcrypt
from flask import render_template, session, request, redirect, flash
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
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
	return redirect("/recipes")


@app.route("/recipes")
def show_user():
	if 'uuid' not in session:
		return redirect('/')
	user = User.get_one({'id': session["uuid"]})
	recipes = Recipe.get_all()
	return render_template("recipes.html", user = user, recipes = recipes )

@app.route("/logout")
def log_out():
	session.clear()
	return redirect("/")


@app.route("/user/login", methods=["post"])
def user_login():
	if not User.validator_login(request.form):
		return redirect("/")

	return redirect("/recipes")


@app.route("/create/recipe/form")
def recipe_form():
	return render_template("createRecipe.html")


@app.route("/create/recipe", methods=["POST"])
def create_recipe():
	Recipe.save(request.form)
	return redirect('/recipes')