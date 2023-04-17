from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.model_user import User


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def save_info():
    print('getting post info')
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    session['game'] = request.form['game']
    session['why'] = request.form['why']
    print(request.form)

    if not User.validate_user(request.form):
        return redirect('/')
    return redirect("/result")

@app.route('/result')
def result():
    return render_template("result.html")

    
if __name__=="__main__":
    app.run(debug=True)