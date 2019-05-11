from flask import Flask

app = Flask("pyTest")

@app.route('/')
def hello():
	print("Hello World!")

hello()
