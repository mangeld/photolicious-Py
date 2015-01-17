from flask import Flask, render_template 
from classes.blog import Blog
import mistune

app = Flask(__name__)
blog = Blog()

data = mistune.markdown('This is an _h1_ ')

@app.route("/")
def index():
	return render_template("index.html", blog=blog, postContent=data)

if __name__ == "__main__":
	app.run(debug=True)
