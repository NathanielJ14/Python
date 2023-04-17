from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:amount>')
@app.route('/play/<int:amount>/<string:color>')
def amount_boxes(amount = 3, color = "lightblue"):
    return render_template("index.html", amount=amount, color=color)


    
if __name__=="__main__":
    app.run(debug=True)