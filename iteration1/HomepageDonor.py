import mysql.connector
from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from flask import g
from flask import url_for
from flask import redirect

bp = Blueprint("home", __name__, url_prefix="/home")

mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
cursor = mydb.cursor(buffered=True)


@bp.route("/", methods=("GET", "POST"))
def home():
    return render_template("loginsucc.html")


@bp.route("/pledge", methods=["POST", "GET"])
def GetResponse():
    username = g.user[0]
    state = g.user[5]
    cursor.execute("SELECT * FROM events ")
    namematch = cursor.fetchall()

    return render_template("HomepageDonor.html", eventlist=namematch, itemlist=possitems)

