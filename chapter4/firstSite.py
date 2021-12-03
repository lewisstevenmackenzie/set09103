from flask import Flask
app = Flask(__name__)

@app.route('/')
def first_Site():
    number=35
    output = 'hello world! this is a random number:' + str(number)
    return output

@app.route("/hello/")
def hello():
    return "Hello Napier! :D"

@app.route("/goodbye/")
def goodbye():
    return "goodbye web server!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=true)
