from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<a href="/zal">To the zals</a>'
    return render_template("index.html")

app.run(debug=True)
@app.route('/zal')
def zal():
    return 'go to zal'

@app.route('/licei')
def licei():
    return 'go to licei'

if __name__ == '__main__':
    app.run()