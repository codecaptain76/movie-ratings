"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session
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

@app.route("/register", methods=['POST'])
def register_user():
    """Send the user to a registration form."""

    return render_template("register.html")


   
#@app.route("/add_user", methods=['POST'])
def add_to_db_User():
    """Adds the user to the database if not already existing"""
    #
    #db.session.add()
    # db.session.commit()
    redirect("/")



@app.route("/login_form", methods=['GET'])
def add_user():

    return render_template("login_form.html")
    


@app.route("/login_submit", methods=['POST'])
def login():
    """Send the user to an email/password form."""
    #add the user id to the session
    email = request.form.get("email")
    password = request.form.get("password")

    if email == User.query.get('email') and password == User.query.get('password'):

        if email in browser_session:
            browser_session['email'] = email
            browser_session['password'] = request.form['password']
            flash("You are now logged in")
            redirect("/")
        else:
            flash("You are not logged in")
            redirect("/login_form")




    # if request.form.get('email') != 'users':
    #     flash("Invalid login") #do you want to 1. retry? or do you want to 2. register as 
    #     #a new user??
    #     redirect("/login_form")
    # else: 
    #     email = request.form.get("email")
    #     registration_info = authenticate(email)
    #     if registration_info:
    #         session['registration_info'] = registration_info
    #         flash("You are logged in!")
    #         redirect("/")



@app.route("/users")
def user_list():
    """Show list of users"""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/user", methods=['POST'])
def user_info():
    """Show information about a particular user, including 
    age
    zipcode
    list of movies they have rated AND the scores for each rating"""
    # May 6 receive information in POST request
    firstname = request.form['firstname']

    # use information of input email and password and check to see if in database

    return render_template("user.html", firstname=firstname)








if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()