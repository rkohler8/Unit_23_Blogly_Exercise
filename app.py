"""Blogly application."""

# from flask import Flask
# from models import db, connect_db
from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# app.config['SECRET_KEY'] = "abc123"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")

@app.route('/users')
def list_users():
    """Shows list of all users in db"""
    users = User.query.all()
    return render_template('listing.html', users=users)

@app.route('/users/create', methods=["GET"])
def add_user():
    # users = User.query.all()
    return render_template('new_user.html')

# @app.route("/users/create", methods=["POST"])
# def users_new():
#     """Handle form submission for creating a new user"""

#     new_user = User(
#         first_name=request.form['first_name'],
#         last_name=request.form['last_name'],
#         image_url=request.form['image_url'] or None)

#     db.session.add(new_user)
#     db.session.commit()

#     return redirect("/users")

@app.route('/users/create', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    
    # return redirect("/users")

    return redirect(f"/{new_user.id}")

@app.route('/<int:user_id>')
def show_user(user_id):
    """Show details about a single user"""
    # pet = Pet.query.get(pet_id)
    user = User.query.get_or_404(user_id)
    # return f"<h1>{user.first_name}</h1>"
    return render_template("details.html", user=user)