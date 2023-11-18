# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# HW 11
# Description:
# Describe what this program does in your own words such as:
'''
This program constructs a Flask app which allows the user to either add or

remove users along with modifying their favorite foods (if admin) or to log-in

to an account and view their favorite food (if regular user). User credentials and

favorite foods are stored in a SQL database which is accessed using sqlite3 to

be displayed on the front-end.
'''

from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sl
db = 'favouriteFoods.db' #dynamic path to allow for changing DB

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
        return render_template("login.html", message='Please login to continue')
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
                               message='Welcome back.',
                               result=db_get_user_list())
    else: #otherwise, if user then render their favorite food and give user client privileges
        return render_template('user.html',
                               username=session['username'],
                               fav_food=db_get_food(session['username']))


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
            db_create_user(request.form["username"], request.form["password"])
            return render_template('admin.html',
                            username=session['username'],
                            message='New user has been added. Welcome back, admin!',
                            result=db_get_user_list())


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
            db_remove_user(request.form["username"])
            return render_template('admin.html',
                            username=session['username'],
                            message='Existing user has been removed. Welcome back, admin!',
                            result=db_get_user_list())


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
            db_set_food(session["username"], request.form["set_fav_food"])
            return render_template('user.html',
                                   username=session['username'],
                                   fav_food=db_get_food(session['username']))


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
        if db_check_creds(request.form["username"], request.form["password"]):
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

def db_get_user_list() -> dict:
    """
    Queries the DB's userfoods table to get a list
    of all the user and their corresponding favorite food for display on admin.html.
    Called to render admin.html template.

    :return: a dictionary with username as key and their favorite food as value
                this is what populates the 'result' variable in the admin.html template
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    stmt = "SELECT * from userfoods;"
    #store the user and food data in a list so they can be zipped into a dict
    user_data_list = []
    food_data_list = []
    #execute statement and manipulate output data to create desired output dict
    data = curs.execute(stmt)
    for entity in data:
        user_data_list.append(entity[0])
        food_data_list.append(entity[1])
    data = dict(zip(user_data_list, food_data_list))
    conn.close()
    return data


def db_create_user(un: str, pw: str) -> None:
    """
    Add provided user and password to the credentials table
    Add provided user to the userfoods table
    and sets their favorite food to "not set yet".
    Called from create_user() view function.

    :param un: username to create
    :param pw: password to create
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    #create tables in case they have been entirely erased
    userfoods_construct_stmt = "CREATE TABLE IF NOT EXISTS userfoods('username' type UNIQUE, 'food')"
    credentials_construct_stmt = "CREATE TABLE IF NOT EXISTS credentials('username' type UNIQUE, 'password')"
    curs.execute(userfoods_construct_stmt)
    curs.execute(credentials_construct_stmt)
    #IGNORE INTO ensures we don't add duplicate credentials
    stmt1 = "INSERT OR IGNORE INTO credentials (username,password) VALUES (?,?);"
    stmt2 = "INSERT OR IGNORE INTO userfoods (username, food) VALUES (?,?)"
    v1 = (un, pw,)
    v2 = (un, 'not set yet',) #sets food as "not set yet" to allow for user to change at their will
    curs.execute(stmt1, v1)
    curs.execute(stmt2, v2)
    conn.commit()
    conn.close()
    return


def db_remove_user(un: str) -> None:
    """
    Removes provided user from all DB tables.
    Called from remove_user() view function.

    :param un: username to remove from DB
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    stmt1 = "DELETE FROM credentials WHERE username = ?;"
    stmt2 = "DELETE FROM userfoods WHERE username = ?;"
    v = (un,)
    curs.execute(stmt1, v)
    curs.execute(stmt2, v)
    conn.commit()
    conn.close()
    return


def db_get_food(un: str) -> str:
    """
    Gets the provided user's favorite food from the DB.
    Called to render user.html fav_food template variable.

    :param un: username to get favorite food of
    :return: the favorite food of the provided user as a string
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    stmt = "SELECT food FROM userfoods WHERE username = ?;"
    v = (un,)
    data = curs.execute(stmt, v)
    #extracts string from cursor object for output
    for food in data:
        food_val = food[0]
    conn.close()
    return food_val


def db_set_food(un: str, ff: str) -> None:
    """
    Sets the favorite food of user, un param, to new incoming ff (favorite food) param.
    Called from set_food() view function.

    :param un: username to update favorite food of
    :param ff: user's new favorite food
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()
    stmt = "UPDATE userfoods SET food = ? WHERE username = ?;"
    v = (ff, un,)
    curs.execute(stmt, v)
    conn.commit()
    conn.close()
    return


# database function
# connects to db and checks cred param (all clients)
def db_check_creds(un, pw):
    """
    Checks to see if supplied username and password are in the DB's credentials table.
    Called from login() view function.

    :param un: username to check
    :param pw: password to check
    :return: True if both username and password are correct, False otherwise.
    """
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un,)
    stmt = "SELECT password FROM credentials WHERE username=?"
    results = curs.execute(stmt, v)  # results is an iterable cursor of tuples (result set)
    correct_pw = ''
    for result in results:
        correct_pw = result[0]  # each result is a tuple of 1, so grab the first thing in it
    conn.close()
    if correct_pw == pw:
        return True
    return False


# main entrypoint
# runs app
if __name__ == "__main__":
    # DB function unit testing:
    assert db_check_creds('alice', 'alicesSecurePassWord') == True
    assert db_check_creds('wrongUser', 'alicesSecurePassWord') == False
    assert db_check_creds('alice', 'wrongPassword') == False

    # TODO: Unit test your other db_ functions here
    #assert that admin can check all users in db
    assert db_get_user_list() == {'alice': 'pecan pie', 'bob': 'oreos', 'greg': 'pizza'}

    #ensure that admin can create a user
    db_create_user("test user", "test pass")
    assert db_check_creds("test user", "test pass") == True

    #ensure that given user's favorite food can be accessed
    assert db_get_food("test user") == "not set yet"

    #ensure that given user's favorite food can be changed
    db_set_food("test user", "noodles")
    assert db_get_food("test user") == "noodles"

    #ensure that admin can remove a user
    db_remove_user("test user")
    assert db_check_creds("test user", "test pass") == False

    app.secret_key = os.urandom(12)
    app.run(debug=True)

