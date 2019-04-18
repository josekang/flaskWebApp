##################################################################
####### MAKE THE NECESSESSARY IMPORTS FOR THE PUPPY FORM #########
##################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField ,SubmitField
from wtforms.validators import DataRequired


class AddPuppyForm(FlaskForm):
    name = StringField("Enter the name of the puppy  ", validators = [DataRequired(message = "The name field cannnot be empty")])
    submit = SubmitField("ADD PUPPY")


class DeletePuppyForm(FlaskForm):
    puppy_id = IntegerField("Enter the ID number of the puppy you want to remove from the adoption list: ", validators = [DataRequired()])
    submit = SubmitField("REMOVE PUPPY")
