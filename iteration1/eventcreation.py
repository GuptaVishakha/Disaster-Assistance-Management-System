
import mysql.connector
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import flash

bp = Blueprint("eventcreation", __name__, url_prefix="/eventcreation")

mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
cursor = mydb.cursor(buffered=True)


username = "vishakha"
password = "!Team006"
dob = "06/02/2000"

@bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":

        UserName = request.form["username"]
        Description= request.form["description"]
        GeographicLocation= request.form["geographiclocation"]
        State=request.form["state"]
        EventName = request.form["eventname"]
        EventDuration= request.form["eventduration"]
        RequiredItem = request.form["requireditem"]

        cursor.execute("INSERT INTO events (name, state, username, location,description,duration,items) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                       (EventName,State ,UserName, GeographicLocation,Description,EventDuration,RequiredItem))
        mydb.commit()


        flash('your reaction is been recorded')
    return redirect(url_for("home.home"))


