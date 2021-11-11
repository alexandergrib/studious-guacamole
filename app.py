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

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

mongo = PyMongo(app)


@app.route("/")
def index():
    test = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    return render_template("index.html", index_page=True, test=test)


# ==========handle login logout register======================================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        if request.form.get("password") == request.form.get("confirm-password"):
            register_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
                "email": request.form.get("email").lower(),
                "f_name": request.form.get("f_name") if request.form.get("f_name") != "" else "",  # fill DB with blank if no name provided
                "l_name": request.form.get("l_name") if request.form.get("l_name") != "" else "",  # fill DB with blank if no name provided
            }
            user_id = mongo.db.users.insert_one(register_user)

            # put the new user id into 'session' cookie
            session["user"] = str(user_id.inserted_id)
            # flash("Registration Successful!")
            return redirect(url_for("index"))
        else:
            # flash message to user to saying their passwords are not identical
            print('password mismatch')
            return render_template("register.html")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                print(existing_user["_id"])
                session["user"] = str(existing_user["_id"])
                # flash("Welcome, {}".format(
                    # request.form.get("username")))
                return redirect(url_for("index"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    """
    User profile check if user exists, if not redirects to home page
    """
    # grab the session user's username from db
    # if request.method == "POST":
    #     pass


    if "user" in session:
        # mongo.db.users.find_one({"_id": ObjectId(session["user"])})

        user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
        print(user)
        # user_history = list(
        #     mongo.db.user_profile.find({"username": {"$eq": session["user"]}}))
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for("index"))
    # return redirect(url_for("index"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    # flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
