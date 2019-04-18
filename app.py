##########################################################
#### IMPORT THE ENTIRE APP IN THIS FILE ##################
#### ALSO CREATE THE VIEWS FOR THE HOME PAGE #############

from flask import render_template

from myproject import app

@app.route("/")
def index():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug = True, port = 5000)
