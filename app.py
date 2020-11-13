import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home
@app.route("/")
def index():
    return render_template("index.html")


# Gallery
@app.route("/get_images")
def get_images():
    images = list(mongo.db.images.find())
    return render_template("gallery.html", images=images)


# Sign Up
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")


# Log In
@app.route("/log_in")
def log_in():
    return render_template("log_in.html")


# Log Out
@app.route("/log_out")
def log_out():
    return redirect(url_for("log_in"))


# Add image to gallery
@app.route("/add_image")
def add_image():
    return render_template("add_image.html")


# Edit image from gallery
@app.route("/edit_image")
def edit_image():
    return render_template("edit_image.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
