###########################################################
#### CREATE THE NECESSARY IMPORTS FOR THE OWNNER VIEWS ####
###########################################################

from flask import Blueprint, render_template, redirect, url_for
from myproject.owner.forms import AddOwnerForm
from myproject.owner.models import Owner
from myproject import db

###########################################################
### CREATE THE VIEWS FOR THE OWNER ########################
###########################################################

Owner_blueprint = Blueprint("owner", __name__, template_folder="templates/owner")

@Owner_blueprint.route("/addowner", methods = ["GET", "POST"])
def addowner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("puppy.list"))

    return render_template("addowner.html", form = form)
