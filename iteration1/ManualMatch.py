
import mysql.connector
from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from flask import g
from flask import url_for
from flask import redirect

bp = Blueprint("home", __name__, url_prefix="/home")

mydb = mysql.connector.connect(host="localhost",user="root",password="team06",database="sys")
cursor = mydb.cursor(buffered=True)



@bp.route("/", methods=("GET", "POST"))
def home():
    return render_template("loginsucc.html")

@bp.route("/pledge",methods=["POST","GET"])
def GetEvent():
    username = g.user[0]
    state = g.user[5]
    cursor.execute("SELECT * FROM events ")
    namematch = cursor.fetchall()

    newrequest = []
    newrequest.append(userrequest[1])
    newuseritems = userrequest[2].replace("'", "")
    newrequest.append(newuseritems)
    newrequest.append(userrequest[3])
    newrequestformat = [newrequest]

        if request.method == "POST":
            if request.form["submit"] == "Yes":
                cursor.execute("DELETE FROM event WHERE username = '%s'" % username)
                mydb.commit()
                msg = "Request Deleted Successfully"
                flash(msg)
                return redirect(url_for("home.home"))
            elif request.form["submit"] == "No":
                return redirect(url_for("home.home"))
           return render_template("Mannualmatch.html",eventlist=namematch,itemlist=possitems)


@bp.route("/response",methods=["POST","GET"])
def GetResponse():
    username = g.user[0]
    state = g.user[5]
    cursor.execute("SELECT * FROM Response)
    namematch = cursor.fetchall()
    cursor.execute("SELECT item FROM items")
    possitems = cursor.fetchall()

    if request.method == "POST":
        error = None

        eventname = request.form["event"]
        items = request.form.getlist('items')
        description = request.form["description"]
        quantities = request.form.getlist('quantity')
        cursor.execute("SELECT * FROM response WHERE username = '%s'" % username)
        possname = cursor.fetchall()
        if len(possname) != 0:
            error = "User has already made a response"

        if len(items) == 0:
            error = "No Items Selected"

        if error is None:
            cursor.execute("INSERT INTO response (username, event, items, description,quantity)  VALUES (%s,%s,%s,%s,%s)",
                           (username, eventname, str(items).strip("[]"), description, str(quantities).strip("[]")))
            mydb.commit()
            msg = "response Created Successfully"
            flash(msg)
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("createresponse.html",eventlist=namematch,itemlist=possitems)

