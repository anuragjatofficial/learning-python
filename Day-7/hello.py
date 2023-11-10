from flask import Flask

app = Flask(__name__)

# my 1st flask app 

@app.route('/')
def hello_world():
	return 'Hello, world !'

if __name__ == '__main__':
	app.run()