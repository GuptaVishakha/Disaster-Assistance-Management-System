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
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
cursor = mydb.cursor(buffered=True)

bp = Blueprint("loginauth", __name__, url_prefix="/loginauth")


@bp.route("/",methods=("GET","POST"))
def home():
    return render_template("loginsucc.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["user"]
        password = request.form["password"]
        error = None
        query = "SELECT userID FROM acinfo WHERE userID = '%s'" % (username)
        cursor.execute(query)
        namematch = cursor.fetchall()
        # print(namematch[0][0])
        query = "SELECT PassWord FROM acinfo WHERE userID = '%s'" % (username)
        cursor.execute(query)
        pwmatch = cursor.fetchall()
        # print(pwmatch[0][0])
        # print(username)
        # print(password)
        if len(namematch)==0:
            error = "Incorrect username."
        elif pwmatch[0][0] != password:
            error = "Incorrect password."

        if error is None:
            session.clear()
            print(username)
            session["user_id"] = username
            print(session.get("user_id"))
            return render_template("loginsucc.html")
        flash(error)
    return render_template("login.html")
