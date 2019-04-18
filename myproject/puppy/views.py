############################################################
##### MAKE THE NECESSARY IMPORT FOR THE PUPPY VIEWS ########
############################################################

from flask import Blueprint, render_template, redirect, url_for
from myproject.puppy.forms import AddPuppyForm, DeletePuppyForm
from myproject.puppy.models import Puppy
from myproject import db

puppy_blueprint = Blueprint("puppy", __name__, template_folder = "templates/puppy")

@puppy_blueprint.route("/addpuppy", methods = ["GET", "POST"])
def addpuppy():
    form = AddPuppyForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("puppy.list"))

    return render_template("addpuppy.html", form = form)

@puppy_blueprint.route("/deletepuppy", methods = ["GET", "POST"])
def deletepuppy():
    form = DeletePuppyForm()
    if form.validate_on_submit():
        id = form.puppy_id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("puppy.list"))

    return render_template("deletepuppy.html", form = form)

@puppy_blueprint.route("/list")
def list():
    puppies = Puppy.query.all()
    return render_template("listpuppy.html", puppies = puppies)
