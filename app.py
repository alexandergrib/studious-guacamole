import os
from datetime import datetime

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


# Home Page
@app.route("/")
@app.route("/home")
def home():
    if "user" in session:
        user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
        return render_template("index.html", index_page=True, user=user,
                               current_page="home")
    else:
        return render_template("index.html", index_page=True, user="",
                               current_page="home")


@app.route("/blog", methods=['GET', 'POST'])
def blog():
    if "user" in session:
        user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    else:
        user = ""
    all_users = list(mongo.db.users.find())
    posts = list(mongo.db.posts.find())
    comments = list(mongo.db.comments.find({'deleted': {"$ne": True}}))

    # print(comments)
    return render_template("blog.html",
                           posts=posts,
                           user=user,
                           all_users=all_users,
                           comments=comments,
                           current_page="blog")


@app.route("/blog/post/<post_id>", methods=['GET', 'POST'])
def single_post(post_id):
    if "user" in session:
        user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    else:
        user = ""
    individual_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    comments = list(
        mongo.db.comments.find({"$and": [{"post": {'$eq': post_id}}]}))

    if len(comments) > 1:
        for i in range(len(comments)):
            comments[i]['username'] = mongo.db.users.find_one(
                {"_id": ObjectId(comments[i]['username'])})
            del comments[i]['username']['password']
            # del comments[i]['username']['_id']
    else:
        if comments:
            comments[0]['username'] = mongo.db.users.find_one(
                {"_id": ObjectId(comments[0]['username'])})
            del comments[0]['username']['password']
            # del comments[0]['username']['_id']
    # print(comments)
    return render_template("single_post.html", user=user,
                           single_post=individual_post,
                           comments=comments, current_page="single_post",
                           amount_of_comments=len(comments))


@app.route("/blog/add", methods=["GET", "POST"])
def add_post():
    # print(request.form)
    user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    if request.method == "POST":
        submit = {
            "nickname": request.form.get('nickname'),
            "title": request.form.get('title'),
            "body": request.form.get('post_body'),
            "created_by": session["user"],
            "created_date": datetime.now().strftime("%d/%m/%Y"),
            "img_url": "",
            "modify_date": "",
            "deleted": False,
            "anonymous": False
        }
        if request.form.get("anonymous"):
            submit['anonymous'] = True
            nickname = request.form.get('nickname')
            if nickname == "":
                submit['nickname'] = 'anonymous'
        # if user not anonymous then query user db and use their f_name l_name and if form fields are not the same from what saved in the db update user db with new l_name f_name
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        if f_name != '' or l_name != "":
            if user["f_name"] != f_name or user["l_name"] != l_name:
                user["f_name"] = f_name
                user["l_name"] = l_name
                mongo.db.users.update_one(
                    {"_id": ObjectId(session["user"])},
                    {"$set": {"f_name": f_name, "l_name": l_name}}
                )
        mongo.db.posts.insert_one(submit)
        return redirect(url_for("blog"))
    return render_template("add_new_post.html", user=user)


@app.route("/blog/edit/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if "user" in session:
        user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    else:
        return redirect(url_for("blog"))
    single_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    if request.method == "POST":
        if request.form.get("anonymous"):
            single_post['anonymous'] = True
            nickname = request.form.get('nickname')
            if nickname == "":
                single_post['nickname'] = 'anonymous'
        single_post["body"] = request.form.get('post_body')
        single_post["title"] = request.form.get('title')
        single_post["modify_date"] = datetime.now().strftime("%d/%m/%Y")
        mongo.db.posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$set": single_post}
        )
        return redirect(url_for("blog"))
    return render_template("edit_post.html", user=user,
                           single_post=single_post)


@app.route("/blog/delete/<post_id>")
def delete_post(post_id):
    single_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    single_post["deleted"] = True
    mongo.db.posts.update_one(
        {"_id": ObjectId(post_id)},
        {"$set": single_post}
    )
    return redirect(url_for("blog"))


@app.route("/blog/restore/<post_id>")
def restore_post(post_id):
    single_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    single_post["deleted"] = False
    mongo.db.posts.update_one(
        {"_id": ObjectId(post_id)},
        {"$set": single_post}
    )
    return redirect(url_for("blog"))


# ============search===================
@app.route("/blog/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search")
    if query:
        print(query)
        comments = list(mongo.db.comments.find({'deleted': {"$ne": True}}))
        all_users = list(mongo.db.users.find())
        posts = list(
            mongo.db.posts.find({"$text": {"$search": query}}))
        return render_template("blog.html",
                               posts=posts,
                               all_users=all_users,
                               comments=comments,
                               current_page="blog")
    else:
        print(query)
        all_users = list(mongo.db.users.find())
        posts = list(mongo.db.posts.find())
        comments = list(mongo.db.comments.find({'deleted': {"$ne": True}}))
        return render_template("blog.html",
                               posts=posts,
                               all_users=all_users,
                               comments=comments,
                               current_page="blog")


#  python
# from app import mongo
# mongo.db.posts.create_index([("body", "text"),("title", "text")])

# ------------comments----------------
@app.route("/blog/post/add/comment", methods=['GET', 'POST'])
def add_comment():
    if request.method == "POST":
        single_post_id = request.form.get('single_post_id')

        save_comment = {
            'username': session['user'],
            'comment': request.form.get('comment_body'),
            'post': single_post_id,
            'deleted': False,
            'anonymous': False,
            'nickname': '',
            'created_date': datetime.now().strftime("%d/%m/%Y")
        }

        if request.form.get("anonymous"):
            save_comment['anonymous'] = True
            nickname = request.form.get('nickname')
            save_comment['nickname'] = nickname
            if nickname == "":
                save_comment['nickname'] = 'anonymous'
        mongo.db.comments.insert_one(save_comment)
        print(save_comment)
        return redirect(url_for('single_post', post_id=single_post_id))


@app.route("/blog/post/edit/comment/<comment_id>", methods=['GET', 'POST'])
def edit_comment(comment_id):
    single_comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    comment_username = mongo.db.users.find_one(
        {"_id": ObjectId(single_comment["username"])})
    del comment_username['password']
    del comment_username['_id']
    # print(comment_username)
    if request.method == 'POST':
        single_comment["comment"] = request.form.get('comment_body')

        if request.form.get("anonymous"):
            single_comment["anonymous"] = True
            single_comment["nickname"] = request.form.get("nickname")
        else:
            single_comment["anonymous"] = False
        print(request.form.get("anonymous"))
        mongo.db.comments.update_one(
            {"_id": ObjectId(comment_id)},
            {"$set": single_comment}
        )
        return redirect(url_for("single_post", post_id=single_comment["post"]))
    return render_template("edit_comment.html", comment=single_comment,
                           comment_username=comment_username,
                           comment_id=comment_id)


@app.route("/blog/post/delete/comment/<comment_id>")
def delete_comment(comment_id):
    single_comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    # Uncomment for soft delete
    single_comment["deleted"] = True
    mongo.db.comments.update_one(
        {"_id": ObjectId(comment_id)},
        {"$set": single_comment}
    )
    # Uncomment to  delete permanently
    # mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    # print('comment deleted')
    return redirect(url_for("single_post", post_id=single_comment["post"]))


# ==========handle login logout register======================================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # flash("Username already exists")
            return redirect(url_for("register"))
        if request.form.get("password") == request.form.get(
                "confirm-password"):
            register_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "email": request.form.get("email").lower(),
                "f_name": request.form.get("f_name") if request.form.get(
                    "f_name") != "" else "",
                # fill DB with blank if no name provided
                "l_name": request.form.get("l_name") if request.form.get(
                    "l_name") != "" else "",
                # fill DB with blank if no name provided
            }
            user_id = mongo.db.users.insert_one(register_user)

            # put the new user id into 'session' cookie
            session["user"] = str(user_id.inserted_id)
            # flash("Registration Successful!")
            return redirect(url_for("home"))
        else:
            # flash message to user to saying their passwords are not identical
            # print('password mismatch')
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
                # print(existing_user["_id"])
                session["user"] = str(existing_user["_id"])
                return redirect(url_for("home"))
            else:
                # invalid password match
                # flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            # flash("Incorrect Username and/or Password")
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

        posts_by_user = list(mongo.db.posts.find(
            {"$and": [{"created_by": {'$eq': session["user"]}}]}).sort(
            "created_date", -1))

        # user_history = list(
        #     mongo.db.user_profile.find({"username": {"$eq": session["user"]}}))
        return render_template("profile.html", user=user, posts=posts_by_user)
    else:
        return redirect(url_for("home"))
    # return redirect(url_for("index"))


@app.route("/profile/edit<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    if request.method == "POST":
        if request.form.get('username'):
            user['username'] = request.form.get('username')
        if request.form.get('email'):
            user['email'] = request.form.get('email')
        if request.form.get('f_name'):
            user['f_name'] = request.form.get('f_name')
        if request.form.get('l_name'):
            user['l_name'] = request.form.get('l_name')
        if request.form.get('password'):
            if check_password_hash(
                    user["password"], request.form.get("old_password")):
                user['password'] = generate_password_hash(
                    request.form.get("password"))
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user}
        )
    return redirect(url_for('profile'))


"""user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    single_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    if request.method == "POST":
        if request.form.get("anonymous"):
            single_post['anonymous'] = True
            nickname = request.form.get('nickname')
            if nickname == "":
                single_post['nickname'] = 'anonymous'
        single_post["body"] = request.form.get('post_body')
        single_post["title"] = request.form.get('title')
        single_post["modify_date"] = datetime.now().strftime("%d/%m/%Y")
        mongo.db.posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$set": single_post}
        )
        return redirect(url_for("blog"))
    return render_template("edit_post.html", user=user,
                           single_post=single_post)"""


@app.route("/health_check")
def health_check():
    """
    Health check page
    """
    return render_template("health_check.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    # flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
