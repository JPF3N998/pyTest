from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
		print("Hello World!")
		exit(0)

hello()
