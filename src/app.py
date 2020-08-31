from flask import Flask

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
# Home page to choose the model type, upload original file and choose whatever we want to generate
def home():
    return "Hello world <h1>Flask<h1>"


@app.route("/tag_info_eg")
# Page to enter essential information for Egypt tags generation
def tag_eg():
    return "Egypt Tags information"


@app.route("/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("tag_eg"))
