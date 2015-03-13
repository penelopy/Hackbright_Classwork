from flask import Flask, render_template


app = Flask (__name__)

@app.route('/')
def home_page(): 
	return render_template("index.html")

@app.route('/wonderful')
def go_to_wonderful():
	return render_template("wonderful.html")

@app.route('/wonderful/hello')
def say_hello():
	#print "Hello world"
	return "What's up?"

if __name__ == "__main__": 
	app.run(debug = True)