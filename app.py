from flask import Flask, render_template 
from classes.blog import Blog
import mistune

app = Flask(__name__)
blog = Blog()
f = open('README.md', 'r')
text = ""

for line in f:
	text = text + line
f.close()
data = mistune.markdown(text)

@app.route("/")
def index():
	return render_template("index.html", blog=blog, postContent=data)

if __name__ == "__main__":
	app.run(debug=True)
