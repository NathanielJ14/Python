from flask_app import app
from flask import render_template, session, request, redirect

#Must import model but make sure you change the name
from flask_app.models.models_dojo import Dojo
from flask_app.models.models_ninja import Ninja

#Display Route
@app.route("/")
def dojos():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=all_dojos)


@app.route('/create/dojo', methods=['POST'])
def dojo_create():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    dojo = Dojo.get_one({'id' :id})
    return render_template('showDojo.html', dojo = dojo)

@app.route('/new/ninja')
def ninja():
    all_dojos = Dojo.get_all()
    return render_template('ninja.html', all_dojos=all_dojos)


@app.route('/create/ninja', methods=['POST'])
def ninja_create():
    Ninja.save(request.form)
    return redirect('/')



    