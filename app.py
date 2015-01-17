from flask import Flask, render_template 
from classes.blog import Blog

app = Flask(__name__)
blog = Blog()


@app.route("/")
def index():
	return render_template("index.html", blog=blog)

if __name__ == "__main__":
	app.run(debug=True)
