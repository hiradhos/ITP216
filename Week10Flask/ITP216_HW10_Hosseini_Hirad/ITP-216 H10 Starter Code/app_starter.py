from flask import Flask, redirect, render_template, request, session, url_for
import os

from util import FileDBHelper as fdb

app = Flask(__name__)

# root end point
# routes to login unless client has already logged in
@app.route("/")
def home():

    """
    Checks whether the user is logged in and returns appropriately.

    :return: renders login.html if not logged in,
                redirects to client otherwise.
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return redirect(url_for('client'))


# client endpoint
# renders appropriate template (admin or user)
@app.route("/client")
def client():
    """
    Renders appropriate template (admin or user)
    NOTE: Should only come to /client if /login'ed successfully, i.e. (db_check_creds() returned True)

    :return: redirects home if not logged in,
                renders admin.html if logged in as admin,
                user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below

    # Here is an example render template call for admin.html
    # TODO: Uncomment below when you're ready
    if not session.get("logged_in"):
        return redirect(url_for('home'))
    elif session['username'] == 'admin':
        return render_template('admin.html',
                               username=session['username'],
                               message='Welcome admin!',
                               result=fdb.db_get_user_list(db_file="./util/foods_db_file.json"))
    else:
        return render_template('user.html',
                               username=session['username'],
                               fav_food= fdb.db_get_food(session['username']))


# create user endpoint (admin only)
# adds new user to db, then re-renders admin template
@app.route("/action/createuser", methods=["POST", "GET"])
def create_user():
    """
    Gets called from admin.html form submit
    Adds a new user to db by calling db_create_user, then re-renders admin template

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        if not session.get("logged_in"):
            return redirect(url_for('home'))
        else:
            fdb.db_create_user(request.form["username"], request.form["password"])
            return render_template('admin.html',
                            username=session['username'],
                            message='New user has been added. Welcome back, admin!',
                            result=fdb.db_get_user_list(db_file="./util/foods_db_file.json"))


# remove user endpoint (admin only)
# removes user from db, then re-renders admin template
@app.route("/action/removeuser", methods=["POST", "GET"])
def remove_user():
    """
    Gets called from admin.html form submit
    Removes user from the db by calling db_remove_user, then re-renders admin template.

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        if not session.get("logged_in"):
            return redirect(url_for('home'))
        else:
            fdb.db_remove_user(request.form["username"])
            return render_template('admin.html',
                            username=session['username'],
                            message='Existing user has been removed. Welcome back, admin!',
                            result=fdb.db_get_user_list(db_file="./util/foods_db_file.json"))


# set food endpoint (user only)
# updates user food, then re-renders user template
@app.route("/action/setfood", methods=["POST", "GET"])
def set_food():
    """
    Gets called from user.html form submit
    Updates user food by calling db_set_food, then re-renders user template

    :return: redirects to home if user not logged in,
                re-renders user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        if not session.get("logged_in"):
            return redirect(url_for('home'))
        else:
            fdb.db_set_food(session["username"], request.form["set_fav_food"])
            return render_template('user.html',
                                   username=session['username'],
                                   fav_food=fdb.db_get_food(session['username']))


# login endpoint
# allows client to log in (checks creds)
@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Allows client to log in
    Calls db_check_creds to see if supplied username and password are correct

    :return: redirects to client if login correct,
                redirects back to home otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "pass":
            session["username"] = request.form["username"]
            session["logged_in"] = True
            return redirect(url_for('client'))
        elif fdb.db_check_creds(fdb.load_json_file_to_dict('./util/creds_db_file.json'), request.form["username"], request.form["password"]):
            session["username"] = request.form["username"]
            session["logged_in"] = True
            return redirect(url_for('client'))
        else:
            return redirect(url_for('home'))


# logout endpoint
@app.route("/logout", methods=["POST", "GET"])
def logout():
    """
    Logs client out, then routes to login
    Remove the user from the session
    :return: redirects back to home
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        session["logged_in"] = False
        session.pop("username", None)
    return redirect(url_for('home'))


# main entrypoint
# runs app
if __name__ == "__main__":

    # TODO: Unit test your other db_ functions here

    app.secret_key = os.urandom(12)
    app.run(debug=True)

