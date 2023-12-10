# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# FINAL PROJECT
# Description:
# Describe what this program does in your own words such as:
'''
This program creates a Flask App which allows users to select a state and then either view the distribution of current insurance rates for that state 
or project the distribution of insurance rates for that state for a given age. The data is stored in a SQLite database and the plots are created using Matplotlib. 
The data is sourced from the Centers for Medicare and Medicaid Services (CMS) and is available at https://www.cms.gov/CCIIO/Resources/Data-Resources/marketplace-puf. 
Projections are done using a linear regression model from scikit-learn.
'''

import io
import os
import sqlite3 as sl
import pandas as pd
from flask import Flask, redirect, render_template, request, session, url_for, send_file
from matplotlib.figure import Figure
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
csv = 'csv/Rate_PUF.csv' # csv file from CMS
db = 'insurance.db' # sqlite database file created using csv_to_db.py script 


@app.route("/")
def home():
    return render_template("home.html", states=db_get_states(), message="Welcome to Insured.info!") #renders home page for root endpoint


@app.route("/submit_state", methods=["POST"])
def submit_state():
    print(request.form['state'])
    session.pop('age', None) #clears age session variable in orer to display current state-wide data
    session["state"] = request.form["state"] #updates session state variable based on user input
    if 'state' not in session or session["state"] == "": #redirects in case of faulty endpoint access
        return redirect(url_for("home"))
    return redirect(url_for("state_current", state=session["state"])) #navigates to state query results page


@app.route("/api/medicare/state:<state>")
def state_current(state):
    return render_template("state.html", state=state, project=False) #renders state query results page


@app.route("/submit_prediction", methods=["POST"])
def submit_prediction():
    if 'state' not in session: #redirects to home if no age value was selected for prediction by the user
        return redirect(url_for("home"))
    session["age"] = request.form["age"] #obtains age value from user input
    if session["state"] == "" or session["age"] == "": #ensures state and age values are not empty to allow for proper linear regression
        return redirect(url_for("home"))
    return redirect(url_for("state_prediction", state=session["state"], age=session["age"])) #navigates to age prediction results page


@app.route("/api/medicare/prediction/state:<state>age:<age>")
def state_prediction(state, age):
    return render_template("state.html", state=state, age=age, project=True) #renders age prediction results page


@app.route("/fig/<state>")
def fig(state): 
    fig = create_figure(state)
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype="image/png")


def create_figure(state): #creates a figure for either current and predicted query results
    print(session)
    if 'age' not in session: #if age is not in session, then current query results are displayed
        fig = Figure(figsize=(10, 7))
        fig.tight_layout()
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('Distribution of Current Medicare/Medicaid Insurance Rates for ' + state + ' Residents')
        state_data = db_create_state_dataframe(state)
        ax.hist(state_data['IndividualRate'], label= 'Current Insurance Rates per CMS Rate PUF Dataset (2023)')
        ax.set(xlabel="individual insurance rate (USD/month)", ylabel="frequency")  
        ax.legend()
        return fig
    else: #if age is in session, then predicted query results are displayed
        age = session['age']
        fig = Figure(figsize=(10, 7))
        fig.tight_layout()
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('Projected Distribution of Medicare/Medicaid Insurance Rates for ' + state + " Residents of Age " + age)
        state_age_data = db_create_state_age_dataframe(state, age)
        state_age_data = state_age_data[state_age_data['Age'] != 'Family Option']
        state_age_data['Age'] = state_age_data['Age'].replace('64 and over', '64')
        state_age_data['Age'] = state_age_data['Age'].replace('0-14', '14')
        state_age_data = state_age_data.dropna(subset=['Age'])
        state_age_data['IndividualRate'] = state_age_data['IndividualRate'].astype(float)
        y = state_age_data['IndividualRate']
        X = state_age_data.drop(['IndividualRate', 'StateCode', 'Tobacco'], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        regr = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=2)
        regr.fit(X_train, y_train)
        y_pred = regr.predict(X_test)
        ax.hist(y_pred, label= 'Projected Insurance Rates from Model Trained on CMS Rate PUF Dataset (2023)')
        ax.set_xlabel("individual insurance rate (USD/month)", labelpad=10)
        ax.set_ylabel("frequency", labelpad=10)
        ax.legend()
        return fig


def db_create_state_dataframe(state): #creates a dataframe for current query results based on state
    conn = sl.connect(db)
    curs = conn.cursor()
    df = pd.DataFrame()
    table = "insurance"
    print(f'{table=}')
    print(f'{state=}')
    stmt = "SELECT * from " + table + " where StateCode =?"
    data = curs.execute(stmt, (state,))
    items = curs.fetchall()
    df = pd.DataFrame(items, columns=[description[0] for description in curs.description])
    conn.close()
    return df

def db_create_state_age_dataframe(state, age): #creates a dataframe for predicted query results based on state and age
    conn = sl.connect(db)
    curs = conn.cursor()
    df = pd.DataFrame()
    table = "insurance"
    #we obtain an age range +- 5 years from the age value provided by the user to allow for adequate training data for our linear regression model
    stmt = "SELECT * from " + table + " where StateCode=? and Age between ? and ?"
    data = curs.execute(stmt, (state, int(age)-5, int(age)+5)) 
    items = curs.fetchall()    
    df = pd.DataFrame(items, columns=[description[0] for description in curs.description])
    conn.close()
    return df


def db_get_states(): #obtains a list of states from the database to populate the state dropdown menu
    conn = sl.connect(db)
    curs = conn.cursor()
    table = "insurance"
    state_stmt = "SELECT `StateCode` from " + table
    state_data = curs.execute(state_stmt)
    states = sorted({result[0] for result in state_data})
    conn.close()
    return states


@app.route('/<path:path>')
def catch_all(path): #redirects to home page for any faulty endpoint access
    return redirect(url_for("home"))


if __name__ == "__main__": #runs the Flask app
    app.secret_key = os.urandom(12)
    app.run(debug=True)




