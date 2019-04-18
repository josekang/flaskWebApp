#################################################
########## CREATE THE MODELS IMPORTS ############
#################################################
from myproject import db
from myproject.owner.models import Owner

##################################################
########## CREATE THE PUPPY MODELS ###############
##################################################

class Puppy(db.Model):
    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    ### ONE TO ONE RELATIONSHIP: WHERE ONE OWNER ONLY OWNS ON PUPPY ####
    owner = db.relationship("Owner", backref = "puppy", uselist = False)

    def __init__(self, name):
        self.name = name

    def  __repr__(self):
        if self.owner:
            return f"The name of the puppy is {self.name} and the it belongs to {self.owner.name}."
        return f"The name of the puppy is {self.name} and it has got no owner yet."
