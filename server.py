"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route("/registration", methods=['POST'])
def register_user():
    """Send the user to a registration form."""

    return render_template("registration.html")


  # #if the form data is identical to an existing user_id's values, send to login
    user_lib = 
    email = request.form['email']    
    password = request.form['password']    
    age = request.form['age']
    zipcode = request.form['zipcode']   

    if email, password, age, zipcode in db,
        return render_template("login_form")
    else:
        return add_user()


@app.route("/login_form", methods=['POST'])
def add_user():
    """Adds the user to the database if not already existing"""

    User(email=request.form['email'], password=request.form['password'], 
        age=request.form['age'], zipcode=request.form['zipcode'])
    db.session.add()


@app.route("/login_form", methods=['POST'])
def login():
    """Send the user to an email/password form."""

    return render_template("login_form.html")


@app.route("/user_list")
def user_list():
    """Show list of users"""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/user", method=['POST'])
def user_info():
    """Show information about a particular user, including 
    age
    zipcode
    list of movies they have rated AND the scores for each rating"""
    # May 6 receive information in POST request
    firstname = request.form['firstname']

    # use information of input email and password and check to see if in database

    return render_template("user.html", firstname)








if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()