#########################################################
####### CREATE ALL THE IMPORTS FOR THE APP ##############
#########################################################
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail, Message

##########################################################
########## SET UP THE APPLICATION ########################
##########################################################

login_manager = LoginManager()

mail = Mail()

app = Flask(__name__)

##########################################################
######### SET UP THE DATABASE ############################
##########################################################

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "WAMUgijOSEPhKaNG'etHE"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "josekangethe2@gmail.com"


db = SQLAlchemy(app)
Migrate(app, db)

login_manager.__init__(app)
login_manager.login_view = "login"

mail.__init__(app)

###########################################################
### IMPORT ALL THE BLUEPRINTS #############################
###########################################################
from myproject.puppy.views import puppy_blueprint
from myproject.owner.views import Owner_blueprint
from myproject.user.views import user_blueprint
from myproject.contact.views import contact_blueprint


###########################################################
###### REGISTER THE BLUEPRINTS ############################
###########################################################
app.register_blueprint(puppy_blueprint, url_prefix = "/puppy")
app.register_blueprint(Owner_blueprint, url_prefix = "/owner")
app.register_blueprint(user_blueprint, url_prefix = "/user")
app.register_blueprint(contact_blueprint, url_prefix = "/contact")
