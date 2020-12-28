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


@app.route("/")
def index():
    """
    This function renders the home page.
    """
    return render_template("index.html")


@app.route("/get_images")
def get_images():
    """
    This function displays all images that exist in the database. It renders
    the gallery page.
    """
    images = list(mongo.db.images.find().sort('_id', -1))
    return render_template("gallery.html", images=images)


@app.route('/get_images_sorted', methods=['GET', 'POST'])
def get_images_sorted():
    """
    This function sorts all images that exist in the database, based on the
    users' selected choice. It renders the gallery page.
    """
    sort_selection = request.form.get('sort-selection')
    if sort_selection == 'uploaddateascending':
        images = list(mongo.db.images.find().sort('_id', -1))
    elif sort_selection == 'uploaddatedescending':
        images = list(mongo.db.images.find())
    elif sort_selection == 'takendateascending':
        images = list(mongo.db.images.find().sort("date", -1))
    else:
        images = list(mongo.db.images.find().sort("date", 1))
    return render_template("gallery.html", images=images)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    This function allows users to search the fields title, user and
    description. It displays the images that contain the searched word and the
    number of images that contain this word.
    Source: https://github.com/gaspar91/FeedMe
    """
    query = request.form.get("query")
    images = list(mongo.db.images.find({"$text": {"$search": query}}))
    result = mongo.db.images.count({"$text": {"$search": query}})
    return render_template("gallery.html", images=images, result=result)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    This function first checks if the provided username exists in the database.
    If so, the user is redirected to the sign up page, where an error flash
    message is shown. If not, a dictionary is created, containing the username
    and a hashed password. The dictionary is inserted into the Users collection
    in the database. A session cookie is added. The user is redirected to the
    home page and a success flash message is shown.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("That username is taken. Please try another.", "error")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username").lower()
        flash("Thank you for signing up! Welcome!", "success")
        return render_template("index.html")
    return render_template("sign_up.html")


@app.route("/log_in", methods=["POST", "GET"])
def log_in():
    """
    This function renders the log in page. It first checks if the provided
    username exists in the database. If not, the user is redirected to the log
    in page, where an error flash message appears. If it does, it checks if the
    hashed password matches the password the user provided. If the passwords
    don't match, the user is redirected to the login page, where an error flash
    message appears. If the passwords do match, a session cookie is added. The
    user is redirected to the profile page and a success flash message is
    shown.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(request.form.get("username")),
                      "success")
                return redirect(url_for("profile_page"))
            else:
                flash("Incorrect username and/or password. Please try again.",
                      "error")
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect username and/or password. Please try again.",
                  "error")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/log_out")
def log_out():
    """
    This function removes the user from session cookies and redirects the user
    to the login page. A success flash message is shown.
    """
    flash("You have been logged out", "success")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/profile_page", methods=["GET", "POST"])
def profile_page():
    """
    This function renders the profile page. It displays the images uploaded by
    the currently logged in user. This page is only visible for the user.
    """
    images = list(mongo.db.images.find().sort('_id', -1))
    if session["user"]:
        return render_template(
            "profile_page.html", username=session["user"], images=images)

    return redirect(url_for("login"))


@app.route("/change_password/<username>", methods=["GET", "POST"])
def change_password(username):
    """
    This function renders the change password page. It is only visible for the
    currently logged in user. The password provided by the user is hashed and
    then updated in the database. After that, the user is directed to the
    profile page. A success flash message is displayed.
    Source: https://github.com/gaspar91/FeedMe
    """
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


@app.route("/delete_account/<username>")
def delete_account(username):
    """
    This function removes a user from the Users collection in the database. It
    removes the user from session cookies and redirects the user to the sign up
    page. A success flash message is shown.
    """
    mongo.db.users.remove({"username": username.lower()})
    session.pop("user")
    flash("Your account has been removed", "success")
    return redirect(url_for("sign_up"))


@app.route("/add_image", methods=["GET", "POST"])
def add_image():
    """
    This function renders the add image page. From the information provided in
    the add image form fields a dictionary is created called 'image'. The
    dictionary is inserted into the Images collection in the database. The user
    is redirected to the gallery. A success flash message is visible.
    """
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


@app.route("/edit_image/<image_id>", methods=["GET", "POST"])
def edit_image(image_id):
    """
    This function renders the edit image page. It retrieves the previous URL,
    which is stored in a hidden field on the edit image page. The information
    provided in the edit image form fields by the user, is updated in the
    database. The user is redirected to the URL that was stored in the hidden
    field. There, a success flash message is visible.
    """
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


@app.route("/delete_image/<image_id>")
def delete_image(image_id):
    """
    This function deletes an image from the database. It retrieves the previous
    URL, which is split at the slash. It checks if the final part matches
    profile_page. If so, the user is redirected back to the profile page. If
    not, he is redirected to the gallery. A success flash message is visible.
    Source: Stack Overflow, see README file under 'Sources'.
    """
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
