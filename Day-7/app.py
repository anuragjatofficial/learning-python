from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcomeMessage():
    return "welcome to flask application"

@app.route('/greet/<username>')
def greetUser(username):
    return 'Hello '+username

@app.route('/fairwell/<username>')
def fairwellUser(username):
    return 'Goodbye '+ username +'!'


if __name__ == '__main__':
    app.run()