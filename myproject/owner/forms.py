###################################################
#### MAKE ALL THE IMPORTS FOR THE OWNER FORM ######
###################################################

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


####################################################
################## CREATE THE FORMS ################
####################################################

class AddOwnerForm(FlaskForm):
    name = StringField("Enter the name of the owner: ")
    puppy_id = IntegerField("Enter the Identification number of the dog: ")
    submit = SubmitField("ADD OWNER")
