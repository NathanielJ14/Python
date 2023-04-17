from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def display_read():
    users = User.get_all()
    print(users)
    return render_template("read.html", users = users)

@app.route('/user_form')
def user_form():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "eml": request.form["eml"]
    }
    User.save(data)
    return redirect('/')

@app.route('/show_user/<int:user_id>')
def show_user(user_id):
    user = User.get_one(user_id)
    return render_template("show_user.html", user = user )


@app.route('/user/delete/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/')


@app.route('/update/<int:user_id>')
def update_form(user_id):
    user = User.get_one(user_id)
    return render_template("edit.html", user = user)


@app.route('/edit/<int:user_id>', methods=["POST"])
def edit_user(user_id):
    data = {
        "id": user_id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "eml": request.form["eml"]
    }
    User.update(data)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
