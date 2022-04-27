import functools
import mysql.connector
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
cursor = mydb.cursor(buffered=True)

bp = Blueprint("loginauth", __name__, url_prefix="/loginauth")


@bp.route("/",methods=("GET","POST"))
def home():
    return render_template("loginsucc.html")

@bp.route("/login", methods=("GET", "POST"))
def Homepage():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["user"]
        password = request.form["password"]
        error = None
        query = "SELECT accounttype FROM acinfo WHERE userID = '%s'" % (username)
        cursor.execute(query)
        role = cursor.fetchall()
        # print(role[0][0])

        if error is None:
            session.clear()
            print(username)
            session["user_id"] = username
            print(session.get("user_id"))
            query = "SELECT accounttype FROM acinfo WHERE userID = '%s'" % (username)
            cursor.execute(query)
            if role == "donor":
                return render_template("HomepageDonor.html")
            elif role == "recipient":
                return render_template("HomepageRecepient.html")
            elif role == "admin":
                return render_template("HomepageAdministration.html")
        flash(error)
    return render_template("login.html")
