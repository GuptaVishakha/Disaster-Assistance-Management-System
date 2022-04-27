import mysql.connector
from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from flask import url_for
from flask import redirect
from flask import session
from flask import g
from iteration1 import loginauth
from flask import g
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")

mydb = mysql.connector.connect(host="localhost",user="root",password="team06",database="sys")
cursor = mydb.cursor(buffered=True)


username = "sliebermann"
password = "!Team006"
dob = "06/02/2000"

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        cursor.execute("SELECT * FROM acinfo WHERE userID = '%s'" % (user_id))
        g.user = (cursor.fetchone())


@bp.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        error = None
        username = request.form["user"]
        password = request.form["password"]
        confirmpass = request.form["confirmpass"]
        dob = request.form["birthdate"]
        address = request.form["address"]
        city = request.form["city"]
        state = request.form["state"]
        zipcode = request.form["zip"]
        usertype = request.form["type"]
        if password != confirmpass:
            error = "Passwords do not match"

        query = "SELECT userID FROM acinfo WHERE userID = '%s'" % (username)
        cursor.execute(query)
        namematch = cursor.fetchall()

        if len(namematch) != 0:
            error = "User is already registered."
        if error is None:
            cursor.execute("INSERT INTO acinfo (userID,password,dob,address,city,state,zip,accounttype) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (username,generate_password_hash(password),dob,address,city,state,zipcode,usertype))
            mydb.commit()
            return redirect(url_for("auth.login"))
        flash(error)
    return render_template("accountcreate.html")

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
        query = "SELECT password FROM acinfo WHERE userID = '%s'" % (username)
        cursor.execute(query)
        pwmatch = cursor.fetchall()
        if len(namematch) == 0:
            error = "Incorrect username."
        elif not check_password_hash(pwmatch[0][0],password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = username
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("login.html")



