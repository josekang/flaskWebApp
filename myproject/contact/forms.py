###################################################
#### CREATE THE NECESSARY IMPORTS FOR THE CONT#####
###################################################

from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.validators import ValidationError

######################################
###### CREATE THE CONTACT FORM #######
######################################

class ContactForm(FlaskForm):
    name = TextField("Name", validators = [DataRequired("The name field cannot be empty")])
    email = TextField("Email", validators = [DataRequired(), Email("please enter a valid email address")])
    subject = TextField("Subject", validators = [DataRequired("The subject field cannot be empty")])
    message = TextAreaField("Message", validators = [DataRequired("The message field cannot be empty")])
    submit = SubmitField("SEND")
