"""Blogly application."""

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

@app.route('/users/new', methods=["GET"])
def add_user():
    """Shows an add form for users"""

    # users = User.query.all()
    return render_template('new_user.html')

@app.route('/users/new', methods=["POST"])
def create_user():
    """Process the add form, adding a new user and going back to /users"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"] or None
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about a single user"""

    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show the edit page for a user"""

    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """Process the edit form, returning the user to the /users page"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete the user"""
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

