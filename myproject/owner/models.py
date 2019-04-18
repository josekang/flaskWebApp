#################################################
########## CREATE THE MODELS IMPORTS ############
#################################################
from myproject import db

##################################################
########## CREATE THE OWNER MODELS ###############
##################################################

class Owner(db.Model):
     __tablename__ = "owners"

     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.Text)
     ### THIS IS A ONE TO MANY RELITIONSHIP : THIS FOREIGN KEY IS A PRIMARY KEY IN THE PUPPY MODEL WHERE ONE OWNER ONLY OWNS ###
     ### ONE PUPPY ###
     puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

     def __init__(self, name, puppy_id):
         self.name = name
         self.puppy_id = puppy_id

     def __repr__(self):
         return f"The name of the owner is {self.name} and he or she owns the puppy with the ID number {self.puppy_id}."
