"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
stamos = User(first_name='John', last_name='Stamos', image_url="https://pyxis.nymag.com/v1/imgs/283/746/709a300b26da59b4950aa2dfeec3d0a03f-27-john-stamos-silo.rvertical.w330.png")
hader = User(first_name='Bill', last_name='Hader', image_url="https://variety.com/wp-content/uploads/2022/12/Bill_Hader-1.png")
reynolds = User(first_name='Ryan', last_name='Reynolds', image_url="https://static.wixstatic.com/media/e59907_a366bf5ce7ef48a98af5b99e46d3404f~mv2.png/v1/fill/w_392,h_392,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Image-empty-state.png")
jackman = User(first_name='Hugh', last_name='Jackman', image_url="https://variety.com/wp-content/uploads/2020/12/Hugh_Jackman.png")
carrey = User(first_name='Jim', last_name='Carrey', image_url="https://celebrityendorsers.com/wp-content/uploads/2022/08/Jim-Carrey.png")
freeman = User(first_name='Morgan', last_name='Freeman', image_url="https://vz.cnwimg.com/thumb-900x/wp-content/uploads/2020/01/Morgan-Freeman.jpg")
hepburn = User(first_name='Audrey', last_name='Hepburn', image_url="https://www.pngmart.com/files/22/Audrey-Hepburn-PNG-Transparent.png")

# Add new objects to session, so they'll persist
db.session.add (stamos)
db.session.add (hader)
db.session.add (reynolds)
db.session.add (jackman)
db.session.add (carrey)
db.session.add (freeman)
db.session.add (hepburn)

# Commit--otherwise, this never gets saved!
db.session.commit()