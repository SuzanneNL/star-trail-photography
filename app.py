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


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    images = list(mongo.db.images.find({"$text": {"$search": query}}))
    result = mongo.db.images.count({"$text": {"$search": query}})
    return render_template("gallery.html", images=images, result=result)


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
            flash("That username is taken. Please try another.", "error")
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
        flash("Thank you for signing up! Welcome!", "success")
        return render_template("index.html")
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
                    flash("Welcome, {}!".format(request.form.get("username")), "success")
                    return redirect(url_for("profile_page"))
            # if the hashed password doesn't match the provided password,
            # a flash message appears and the user is redirected
            # to the log in page.
            else:
                flash("Incorrect username and/or password. Please try again.",
                      "error")
                return redirect(url_for("log_in"))

        # if username doesn't exist, a flash message appears
        # and the user is redirected to the log in page.
        else:
            flash("Incorrect username and/or password. Please try again.",
                  "error")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


# Log Out
@app.route("/log_out")
def log_out():
    # Remove the user from session cookies
    flash("You have been logged out", "success")
    session.pop("user")
    return redirect(url_for("log_in"))


# Personal profile page
@app.route("/profile_page", methods=["GET", "POST"])
def profile_page():
    images = list(mongo.db.images.find())

    # no other user than the logged in user can see his profile page
    if session["user"]:
        return render_template(
            "profile_page.html", username=session["user"], images=images)

    return redirect(url_for("login"))


# Change password
@app.route("/change_password/<username>", methods=["GET", "POST"])
def change_password(username):
    if request.method == "POST":
        submit = {
            "username": session["user"],
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.update({"username": username.lower()}, submit)
        flash("Your password has been updated!", "success")
        return redirect(url_for("profile_page", username=session["user"]))

    if session["user"]:
        return render_template("change_password.html", username=username)

    return redirect(url_for("log_in"))


# Delete account
@app.route("/delete_account/<username>")
def delete_account(username):
    mongo.db.users.remove({"username": username.lower()})
    session.pop("user")
    flash("Your account has been removed", "success")
    return redirect(url_for("sign_up"))


# Add image to gallery
@app.route("/add_image", methods=["GET", "POST"])
def add_image():
    if request.method == "POST":
        image = {
            "url": request.form.get("url"),
            "image_title": request.form.get("image_title"),
            "camera": request.form.get("camera"),
            "focal_length": request.form.get("focal_length"),
            "iso": request.form.get("iso"),
            "aperture": request.form.get("aperture"),
            "exposure": request.form.get("exposure"),
            "location": request.form.get("location"),
            "date": request.form.get("date"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }
        mongo.db.images.insert_one(image)
        flash("Thank you. Your image has been added to the gallery!",
              "success")
        return redirect(url_for("get_images"))
    return render_template("add_image.html")


# Edit image from gallery and profile
@app.route("/edit_image/<image_id>", methods=["GET", "POST"])
def edit_image(image_id):
    previous_page = request.referrer
    if request.method == "POST":
        previous_url = request.form.get("previous_url")
        submit = {
            "url": request.form.get("url"),
            "image_title": request.form.get("image_title"),
            "camera": request.form.get("camera"),
            "focal_length": request.form.get("focal_length"),
            "iso": request.form.get("iso"),
            "aperture": request.form.get("aperture"),
            "exposure": request.form.get("exposure"),
            "location": request.form.get("location"),
            "date": request.form.get("date"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }
        mongo.db.images.update({"_id": ObjectId(image_id)}, submit)
        flash("Your image has successfully been updated!", "success")
        return redirect(previous_url)

    image = mongo.db.images.find_one({"_id": ObjectId(image_id)})
    return render_template("edit_image.html", image=image,
                           previous_page=previous_page)


# Delete image from gallery and profile
@app.route("/delete_image/<image_id>")
def delete_image(image_id):
    url = request.referrer
    url_split = url.split('/')
    previous_page = url_split[-1]
    mongo.db.images.remove({"_id": ObjectId(image_id)})
    flash("Your image has been removed", "success")
    if previous_page == "profile_page":
        return redirect(url_for("profile_page"))
    return redirect(url_for("get_images"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)