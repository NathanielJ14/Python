from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def save_info():
    print('getting post info')
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    session['game'] = request.form['game']
    session['device'] = request.form['device']
    session['why'] = request.form['why']
    print(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")



    
if __name__=="__main__":
    app.run(debug=True)