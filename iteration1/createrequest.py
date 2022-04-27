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

    role = g.user[7]
    if role == "donor":
        cursor.execute("SELECT * FROM requests")
        requestList = cursor.fetchall()
        newRequestList = []
        for i in range(len(requestList)):
            user = requestList[i]
            cursor.execute("SELECT zip FROM acinfo WHERE userID = '%s'" % user[0])
            zip = cursor.fetchone()
            newUser = []
            for j in range(len(user)):
                if j == 2:
                    newList = user[j].replace("'", "").replace(" ", "").split(',')
                    newList2 = user[4].replace("'", "").replace(" ", "").split(',')
                    newList2 = list(filter(None, newList2))
                    newUser.append(newList + newList2)
                elif j != 4:
                    newUser.append(user[j])
            newUser.append(zip[0])
            newRequestList.append(newUser)
        return render_template("HomepageDonor.html",requestList=newRequestList)
    elif role == "recipient":
        return render_template("HomepageRecepient.html")
    elif role == "admin":
        return render_template("HomepageAdministration.html")
    else:
        return render_template("loginsucc.html")

@bp.route("/pledge",methods=["POST","GET"])
def pledgehelp():
    username = g.user[0]
    state = g.user[5]
    cursor.execute("SELECT name FROM events WHERE state = '%s'" % state)
    namematch = cursor.fetchall()
    cursor.execute("SELECT item FROM items")
    possitems = cursor.fetchall()

    if request.method == "POST":
        error = None

        eventname = request.form["Location"]
        items = request.form.getlist('items')
        description = request.form["description"]
        quantities = request.form.getlist('quantity')
        if len(items) == 0:
            error = "No Items Selected"

        if error is None:
            quants = list(filter(None, quantities))
            cursor.execute("INSERT INTO pledge (username, event, items, description,quantity)  VALUES (%s,%s,%s,%s,%s)", (username,eventname, str(items).strip("[]"),description,str(quants).strip("[]")))
            mydb.commit()
            msg = "pledge Created Successfully"
            flash(msg)
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("createpledge.html",eventlist=namematch,itemlist=possitems)


@bp.route("/response",methods=["POST","GET"])
def responsehelp():
    username = g.user[0]
    state = g.user[5]
    cursor.execute("SELECT name FROM events WHERE state = '%s'" % state)
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

        if len(items) == 0:
            error = "No Items Selected"

        if error is None:
            quants = list(filter(None, quantities))
            cursor.execute("INSERT INTO response (username, event, items, description,quantity)  VALUES (%s,%s,%s,%s,%s)",
                           (username, eventname, str(items).strip("[]"), description, str(quants).strip("[]")))
            mydb.commit()
            msg = "response Created Successfully"
            flash(msg)
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("createresponse.html",eventlist=namematch,itemlist=possitems)

@bp.route("/item", methods=["POST","GET"])
def item():
    return render_template("itemlist.html")

@bp.route("/additem", methods=["POST","GET"])
def additem():
    username = g.user[0]
    if request.method == "POST":
        itemname = request.form["itemname"]
        cursor.execute("INSERT INTO items (addedby,item) VALUES (%s,%s)", (username, itemname))
        mydb.commit()

        flash("Item Added Successfully")
        return redirect(url_for("home.home"))
    return render_template("additem.html")

@bp.route("/delete", methods=["POST","GET"])
def deleteitem():

    cursor.execute("SELECT item FROM items")
    possitems = cursor.fetchall()
    newpossitems = []
    for j in range(len(possitems)):
        newpossitems.append(possitems[j][0])
    if request.method == "POST":
        itemname = request.form["items"]
        cursor.execute("DELETE FROM items WHERE item = '%s'" % itemname)
        mydb.commit()
        msg = "Request Deleted Successfully"
        flash(msg)
        return redirect(url_for("home.home"))
    return render_template("deleteitem.html",itemlist=newpossitems)

@bp.route("/modify",methods=["POST","GET"])
def modifyRequest():
    username = g.user[0]
    cursor.execute("SELECT * FROM requests WHERE username = '%s'" % username)
    namematch = cursor.fetchall()
    error = None
    if len(namematch) == 0:
        error = "You have not made a request yet"
        flash(error)
        return redirect(url_for("home.home"))

    if error is None:
        return render_template("modifyrequest.html")

@bp.route("/change",methods=["POST","GET"])
def changeItems():
    username = g.user[0]
    cursor.execute("SELECT item FROM items")
    possitems = cursor.fetchall()
    cursor.execute("SELECT * FROM requests WHERE username = '%s'" % username)
    useritems = cursor.fetchall()
    newuseritems = useritems[0][2].replace("'","").replace(" ","").split(',')
    checked = []
    newquantities = useritems[0][4].replace("'","").replace(" ","").split(',')
    newpossitems=[]

    for j in range(len(possitems)):
        newpossitems.append(possitems[j][0])

    for item in range(len(newpossitems)):
        if newpossitems[item] in newuseritems:
            checked.append('checked')
        else:
            checked.append('')
    newitems = []
    j=0
    for i in range(len(newpossitems)):
        if(checked[i]=='checked'):
            newitems.append([newpossitems[i], checked[i],newquantities[j].strip(' ')])
        else:
            newitems.append([newpossitems[i], checked[i], ''])

    if request.method == "POST":
        error = None

        cursor.execute("SELECT * FROM requests WHERE username = '%s'" % username)
        prevdata = cursor.fetchall()
        eventname = prevdata[0][1]
        description = prevdata[0][3]

        items = request.form.getlist('items')
        quants = request.form.getlist('quantity')
        quants = list(filter(None, quants))
        if len(items) == 0:
            error = "No Items Selected"

        if error is None:
            cursor.execute("DELETE FROM requests WHERE username = '%s'" % username)
            mydb.commit()
            cursor.execute("INSERT INTO requests (username, event, items, description,quantity)  VALUES (%s,%s,%s,%s,%s)", (username,eventname,str(items).strip("[]"),description,str(quants).strip("[]").replace("'","")))
            mydb.commit()
            msg = "Request Updated Succesfully"
            flash(msg)
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("changeitems.html", itemlist=newitems)
@bp.route("/deleterequest",methods=["POST","GET"])
def delete():
    username = g.user[0]
    cursor.execute("SELECT * FROM requests WHERE username = '%s'" % username)
    userrequest = cursor.fetchall()[0]
    newrequest = []
    newrequest.append(userrequest[1])
    newuseritems = userrequest[2].replace("'", "")

    newrequest.append(newuseritems)
    newrequest.append(userrequest[3])
    newrequestformat = [newrequest]


    if request.method == "POST":
        if request.form["submit"] == "Yes":
            cursor.execute("DELETE FROM requests WHERE username = '%s'" % username)
            mydb.commit()
            msg = "Request Deleted Successfully"
            flash(msg)
            return redirect(url_for("home.home"))
        elif request.form["submit"] == "No":
            return redirect(url_for("home.home"))
    return render_template("deleterequest.html", requests=newrequestformat)




@bp.route("/request",methods=["POST","GET"])
def requestHelp():
    username = g.user[0]
    state = g.user[5]
    cursor.execute("SELECT name FROM events WHERE state = '%s'" % state)
    namematch = cursor.fetchall()
    cursor.execute("SELECT item FROM items")
    possitems = cursor.fetchall()

    if request.method == "POST":
        error = None

        eventname = request.form["event"]
        items = request.form.getlist('items')
        quantities = request.form.getlist('quantity')
        quantities = list(filter(None, quantities))
        description = request.form["description"]
        cursor.execute("SELECT * FROM requests WHERE username = '%s'" % username)
        possname = cursor.fetchall()
        if len(possname) != 0:
            error = "User has already made a request"

        if len(items) == 0:
            error = "No Items Selected"

        if error is None:

            cursor.execute("INSERT INTO requests (username, event, items, description,quantity)  VALUES (%s,%s,%s,%s,%s)", (username,eventname,str(items).strip("[]"),description,str(quantities).strip("[]").replace("'","")))
            mydb.commit()
            msg = "Request Created Successfully"
            flash(msg)
            return redirect(url_for("home.home"))
        flash(error)
    return render_template("request.html",eventlist=namematch,itemlist=possitems)

@bp.route("/event", methods=["POST","GET"])
def event():
    username = g.user[0]
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
@bp.route("/match", methods=["POST","GET"])
def match():

    cursor.execute("SELECT * FROM requests")
    requestList = cursor.fetchall()
    newRequestList = []
    for i in range(len(requestList)):
        user = requestList[i]
        cursor.execute("SELECT zip FROM acinfo WHERE userID = '%s'" % user[0])
        zip = cursor.fetchone()
        newUser = []
        for j in range(len(user)):
            if j == 2:
                newList = user[j].replace("'","").replace(" ","").split(',')
                newList2 = user[4].replace("'", "").replace(" ", "").split(',')
                newList2 = list(filter(None,newList2))
                newUser.append(newList + newList2)
            elif j != 4:
                newUser.append(user[j])
        newUser.append(zip[0])
        newRequestList.append(newUser)

    cursor.execute("SELECT * FROM response")
    responseList = cursor.fetchall()
    newResponseList = []
    for i in range(len(responseList)):
        user = responseList[i]
        if user[5] is None:
            cursor.execute("SELECT zip FROM acinfo WHERE userID = '%s'" % user[0])
            zip = cursor.fetchone()
            newUser = []
            for j in range(len(user)-1):
                if j == 2:
                    newList = user[j].replace("'", "").replace(" ", "").split(',')
                    newList2 = user[4].replace("'", "").replace(" ", "").split(',')
                    newList2 = list(filter(None, newList2))
                    newUser.append(newList + newList2)
                elif j != 4:
                    newUser.append(user[j])
            newUser.append(zip[0])
            newResponseList.append(newUser)

    cursor.execute("SELECT * FROM pledge")
    responseList = cursor.fetchall()

    for i in range(len(responseList)):

        user = responseList[i]
        if(user[5] is None):
            cursor.execute("SELECT zip FROM acinfo WHERE userID = '%s'" % user[0])
            zip = cursor.fetchone()
            newUser = []
            for j in range(len(user)-1):
                if j == 2:
                    newList = user[j].replace("'", "").replace(" ", "").split(',')
                    newList2 = user[4].replace("'", "").replace(" ", "").split(',')
                    newList2 = list(filter(None, newList2))
                    newUser.append(newList + newList2)
                elif j != 4:
                    newUser.append(user[j])
            newUser.append(zip[0])
            newResponseList.append(newUser)

    if request.method == "POST":
        requser = request.form["requests"]
        items = request.form["responses"]
        divideditems = items.split("/")
        newitem = str(divideditems[0]).strip("[]").replace("'", "").replace(" ", "")
        newitems = newitem.split(',')

        resuser = divideditems[1]
        query = "SELECT * FROM response WHERE username = '%s' AND items = \"%s\"" % (resuser,str(newitems[:len(newitems)//2]).strip("[]"))
        cursor.execute(query)
        possresponse = cursor.fetchone()
        if(possresponse is not None):
            query = "DELETE FROM response WHERE username = '%s' AND items = \"%s\" AND quantity = \"%s\"" % (resuser,str(newitems[:len(newitems)//2]).strip("[]"),str(newitems[len(newitems)//2:]).strip("[]"))
            print(query)
            cursor.execute(query)
            mydb.commit()
            query = "INSERT INTO response (username, event, items,description,quantity,matchuser) VALUES ('%s','%s',\"%s\",'%s',\"%s\",'%s')" % (possresponse[0], possresponse[1], possresponse[2], possresponse[3], possresponse[4], requser)
            cursor.execute(query)
            mydb.commit()

        query = "SELECT * FROM pledge WHERE username = '%s' AND items = \"%s\"" % (resuser,str(newitems[:len(newitems)//2]).strip("[]"))
        cursor.execute(query)
        posspledge = cursor.fetchone()

        if (posspledge is not None):
            query = "DELETE FROM pledge WHERE username = '%s' AND items = \"%s\" AND quantity = \"%s\"" % (resuser,str(newitems[:len(newitems)//2]).strip("[]"),str(newitems[len(newitems)//2:]).strip("[]"))
            cursor.execute(query)
            mydb.commit()
            query = "INSERT INTO pledge (username, event, items,description,quantity,matchuser) VALUES ('%s','%s',\"%s\",'%s',\"%s\",'%s')" % (posspledge[0], posspledge[1], posspledge[2], posspledge[3], posspledge[4], requser)
            cursor.execute(query)
            mydb.commit()

        cursor.execute("SELECT * FROM requests WHERE username = '%s'" % requser)
        newRequest = cursor.fetchone()
        oldItemsItems = newRequest[2].strip("[]").replace("'", "").replace(" ", "").split(',')
        oldItemsQuants = newRequest[4].strip("[]").replace("'", "").replace(" ", "").split(',')
        newItemsItems = newitems[:len(newitems)//2]
        newItemsQuants = newitems[len(newitems)//2:]

        i = 0
        for item in oldItemsItems:
            j = 0
            for item2 in newItemsItems:
                if item == item2:
                    oldItemsQuants[i] = int(oldItemsQuants[i]) - int(newItemsQuants[j])
                    if(oldItemsQuants[i] < 0):
                        oldItemsQuants[i] = 0
                j+=1
            i+=1


        query = "DELETE FROM requests WHERE username = '%s'" % requser
        cursor.execute(query)
        mydb.commit()
        query = "INSERT INTO requests (username, event, items,description,quantity) VALUES ('%s','%s',\"%s\",'%s',\"%s\")" % (
        newRequest[0], newRequest[1],newRequest[2], newRequest[3], str(oldItemsQuants).strip("[]").replace("'",""))
        cursor.execute(query)
        mydb.commit()




        msg = "Match made successfully"
        flash(msg)


        return redirect(url_for("home.home"))
    return render_template("manualmatch.html",requestList = newRequestList,responseList = newResponseList)