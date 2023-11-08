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
    elif session['username'] == 'admin': #if user is admin, render the user list and give admin client privileges
        return render_template('admin.html',
                               username=session['username'],
                               message='Welcome admin!',
                               result=fdb.db_get_user_list(db_file="./util/foods_db_file.json"))
    else: #otherwise, if user then render their favorite food and give user client privileges
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
        if not session.get("logged_in"): #if not logged in as admin, then redirect to login page
            return redirect(url_for('home'))
        else: #otherwise, use db_create_user function to add user and re-render admin page
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
    if request.method == "POST": #check if admin is logged in
        if not session.get("logged_in"):
            return redirect(url_for('home'))
        else: #use db_remove_user function to remove user and re-render admin page
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
        if not session.get("logged_in"): #check if user is logged in to be able to change food
            return redirect(url_for('home'))
        else: #if logged in, use db_set_food function to change food and re-render user page
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
    if request.method == "POST": #use db_check_creds function to ensure username and password key-value pair match
        if fdb.db_check_creds(fdb.load_json_file_to_dict('./util/creds_db_file.json'), request.form["username"], request.form["password"]):
            session["username"] = request.form["username"]
            session["logged_in"] = True
            return redirect(url_for('client'))
        else: #if not match, re-render login page
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
    if request.method == "POST": #to log out, reset session gobal variables and then redirect to login page
        session["logged_in"] = False
        session.pop("username", None)
    return redirect(url_for('home'))


# main entrypoint
# runs app
if __name__ == "__main__":

    # TODO: Unit test your other db_ functions here
    # relative paths did not work on Windows system; absolute paths used instead
    #Test json saving and loading functions
    foods_path = r"C:\Users\hosse\Desktop\Github\ITP216\Week10Flask\ITP216_HW10_Hosseini_Hirad\ITP-216 H10 Starter Code\util\foods_db_file.json"
    creds_path = r"C:\Users\hosse\Desktop\Github\ITP216\Week10Flask\ITP216_HW10_Hosseini_Hirad\ITP-216 H10 Starter Code\util\creds_db_file.json"
    foods_dict = {"newUser": "not set yet", "user1": "oreos", "user2": "popcorn", "janice": "boba", "joe": "ice cream", "james": "not set yet"}
    foods_json = fdb.save_dict_to_json_file(foods_dict, foods_path)
    foods_dict_loaded = fdb.load_json_file_to_dict(foods_path)
    assert foods_dict_loaded == foods_dict
    creds_dict = {"admin": "password","newUser": "newPassword", "user1": "pass1", "user2": "pass2", "janice": "pass3", "joe": "pass4", "james": "pass782"}
    creds_json = fdb.save_dict_to_json_file(creds_dict, creds_path)
    creds_dict_loaded = fdb.load_json_file_to_dict(creds_path)
    assert creds_dict_loaded == creds_dict
    #Test various user administration functions
    fdb.db_create_user("joseph", "pass2341234")
    fdb.db_set_food("joseph", "meatballs")
    print(fdb.db_get_user_list(creds_path))
    print(fdb.db_get_food("joseph"))
    fdb.db_remove_user("joseph")
    print(fdb.db_get_user_list(creds_path))
    assert fdb.db_check_creds(creds_dict, 'user1', 'pass1') is True


    app.secret_key = os.urandom(12)
    app.run(debug=True)

