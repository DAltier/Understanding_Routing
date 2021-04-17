from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!!!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def name(name):
    return "Hello " + name.capitalize() + "!"

@app.route('/repeat/<int:number>/<word>')
def repeat(number, word):
    if number==0:
        return "end"
    return word + " " + repeat(number-1, word)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, no response. Try again."


if __name__=="__main__":
    app.run(debug=True)