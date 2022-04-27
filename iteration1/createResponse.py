import mysql.connector
from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from flask import url_for
from flask import redirect

bp = Blueprint("home", __name__, url_prefix="/home")

mydb = mysql.connector.connect(host="localhost",user="root",password="team06",database="sys")
cursor = mydb.cursor(buffered=True)


username = "sliebermann"
state = "IA"


@bp.route("/", methods=("GET", "POST"))
def home():
    return render_template("loginsucc.html")

@bp.route("/response", methods=["GET","POST"])
def response():
    return render_template("createresponse.html")

@bp.route("/item", methods=["POST","GET"])
def item():
    return render_template("itemlist.html")

@bp.route("/modify",methods=["POST","GET"])
def modifyresponse():
    cursor.execute("SELECT * FROM response WHERE username = '%s'" % username)
    namematch = cursor.fetchall()
    error = None
    if len(namematch) == 0:
        error = "You have not made a response yet"
        flash(error)
        return redirect(url_for("home.home"))

    if error is None:
        return render_template("modifyresponse.html")

@bp.route("/change",methods=["POST","GET"])
def changeItems():
    cursor.execute("SELECT * FROM response WHERE username = 'test'")
    dummydata = cursor.fetchall()
    if len(dummydata) != 0:
        global username
        username = "test"
    cursor.execute("SELECT item FROM items")
    possitems = cursor.fetchall()
    cursor.execute("SELECT items FROM response WHERE username = '%s'" % username)
    useritems = cursor.fetchall()
    newuseritems = useritems[0][0].replace("'","").replace(" ","").split(',')
    checked = []
    newpossitems=[]

    for j in range(len(possitems)):
        newpossitems.append(possitems[j][0])

    for item in range(len(newpossitems)):
        if newpossitems[item] in newuseritems:
            checked.append('checked')
        else:
            checked.append('')
    newitems = []
    for i in range(len(newpossitems)):
        newitems.append([newpossitems[i], checked[i]])

    if request.method == "POST":
        error = None

        cursor.execute("SELECT * FROM response WHERE username = '%s'" % username)
        prevdata = cursor.fetchall()
        eventname = prevdata[0][1]
        description = prevdata[0][3]

        items = request.form.getlist('items')

        if len(items) == 0:
            error = "No Items Selected"

        if error is None:
            cursor.execute("DELETE FROM response WHERE username = '%s'" % username)
            mydb.commit()
            cursor.execute("INSERT INTO response (username, event, items, description)  VALUES (%s,%s,%s,%s)", (username,eventname,str(items).strip("[]"),description))
            mydb.commit()
            msg = "response Updated Succesfully"
            flash(msg)
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("changeitems.html", itemlist=newitems)
@bp.route("/deleteresponse",methods=["POST","GET"])
def delete():
    cursor.execute("SELECT * FROM response WHERE username = '%s'" % username)
    userrequest = cursor.fetchall()[0]
    newrequest = []
    newrequest.append(userrequest[1])
    newuseritems = userrequest[2].replace("'", "")
    newrequest.append(newuseritems)
    newrequest.append(userrequest[3])
    newrequestformat = [newrequest]

    if request.method == "POST":
        if request.form["submit"] == "Yes":
            cursor.execute("DELETE FROM response WHERE username = '%s'" % username)
            mydb.commit()
            msg = "response Deleted Successfully"
            flash(msg)
            return redirect(url_for("home.home"))
        elif request.form["submit"] == "No":
            return redirect(url_for("home.home"))
    return render_template("deleteresponse.html", requests=newrequestformat)




@bp.route("/request",methods=["POST","GET"])
def responsehelp():
    cursor.execute("SELECT name FROM events WHERE state = '%s'" % state)
    namematch = cursor.fetchall()
    cursor.execute("SELECT item FROM items")
    possitems = cursor.fetchall()

    if request.method == "POST":
        error = None

        eventname = request.form["event"]
        items = request.form.getlist('items')
        description = request.form["description"]
        if description == "THIS IS A DESCRIPTION FOR THE response CURRENTLY BEING MADE":
            global username
            username = "test"
        cursor.execute("SELECT * FROM response WHERE username = '%s'" % username)
        possname = cursor.fetchall()
        if len(possname) != 0:
            error = "User has already made a response"

        if len(items) == 0:
            error = "No Items Selected"

        if error is None:

            cursor.execute("INSERT INTO response (username, event, items, description)  VALUES (%s,%s,%s,%s)", (username,eventname, str(items).strip("[]"),description))
            mydb.commit()
            msg = "response Created Successfully"
            flash(msg)
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("createresponse.html",eventlist=namematch,itemlist=possitems)

@bp.route("/event", methods=["POST","GET"])
def event():
    if request.method == "POST":

        EventTime = request.form["EventTime"]
        Description= request.form["Description"]
        GeographicLocation= request.form["GeographicLocation"]
        State=request.form["State"]
        EventName = request.form["EventName"]
        EventDuration= request.form["EventDuration"]
        RequiredItem = request.form["RequiredItem"]

        cursor.execute("INSERT INTO events (name, state, username, location,description,duration,items,eventtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                       (EventName,State ,username, GeographicLocation,Description,EventDuration,RequiredItem,EventTime))
        mydb.commit()


        flash('your reaction is been recorded')
        return redirect(url_for("home.home"))
    return render_template("eventcreation.html")

