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
    if request.method == "POST":
        # First check if the provided username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # If the username already exists,
        # a flash message appears
        # and the user is redirected to the sign up page.
        if existing_user:
            flash("That username is taken. Please try another.")
            return redirect(url_for("sign_up"))
        # create a dictionary, containing username and a password hash
        # that's generated from the password provided by the user.

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # insert dictionary sign_up to the Users collection.
        mongo.db.users.insert_one(sign_up)

        # put users into 'session' cookie and flash message
        # to let the new user know that registration was successful.
        session["user"] = request.form.get("username").lower()
        flash("Thank you for signing up! Welcome!")
    return render_template("sign_up.html")


# Log In
@app.route("/log_in", methods=["POST", "GET"])
def log_in():
    if request.method == "POST":
        # First check if the provided username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If the username exists,
        if existing_user:
            # then check if the hased password matches the password the user
            # provided
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            # if the hashed password doesn't match the provided password,
            # a flash message appears and the user is redirected
            # to the log in page.
            else:
                flash("Incorrect username and/or password. Please try again.")
                return redirect(url_for("log_in"))

        # if username doesn't exist, a flash message appears
        # and the user is redirected to the log in page.
        else:
            flash("Incorrect username and/or password. Please try again.")
            return redirect(url_for("log_in"))

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
