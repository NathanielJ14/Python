from flask import Flask
app = Flask(__name__)

#This will move locations later

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name}"


@app.route('/repeat/<int:num>/<string:word>')
def multiply_word(num, word):
    return f"{word * num}"

    #must be at the bottom
    
if __name__=="__main__":
    app.run(debug=True)