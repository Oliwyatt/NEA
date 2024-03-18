from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import calendar
import Data

global Current_User
Current_User = Data.user()
global User_Data
User_Data = Data.Tables(Current_User)

app = Flask(__name__)
Data.Initialise()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Organiser.db"
db = SQLAlchemy(app)


@app.route("/", methods=["POST", "GET"])
def index():
    
    try:
        if request.method == "POST":
            if Current_User.login(Email=request.form["Email"], Password=request.form["Password"]):
                return redirect("/Home")
            else:
                return redirect("/")
        else:
            return render_template("Index.html")
    except Exception as err:
        return render_template("Error.html", Error=err)


@app.route("/SignUp", methods=["POST", "GET"])
def SignUp():
    if request.method == "POST":
        try:
            if Current_User.signup(FName=request.form["FName"], LName=request.form["LName"], Email=request.form["Email"], Password=request.form["Password"]):
                return redirect("/")
            else:
                return redirect("/SignUp")
        except Exception as err:
            return render_template("Error.html", Error=err)
    else:
        return render_template("SignUp.html")


@app.route("/Home", methods=["POST", "GET"])
def Home():
    name = Current_User.GetFName()
    Date = str(date.today())
    Relaxation = User_Data.GetAllRData()
    Calendar = User_Data.GetTodaysCalendar(Date)
    return render_template("Home.html", Name=name, Rdata=Relaxation, Cdata=Calendar)

@app.route("/LogOut", methods=["POST", "GET"])
def LogOut():
    try:
        Current_User = Data.user()
        print(Current_User.GetFName())
        return redirect("/")
    except Exception as err:
        return render_template("Error.html", Error=err)

@app.route("/Calendar", methods=["POST", "GET"])
def Calendar():
    today = date.today()
    Monthlen = calendar.monthrange(today.year, today.month)[1]
    Calendar = User_Data.GetTodaysCalendar(str(today))
    if request.method == "POST":
        try:
            Date = date(int(request.form["Year"]), int(request.form["Month"]), int(request.form["Day"]))
            if request.form["Filter"] == "None":
                Calendar = User_Data.GetCalendar(Date, request.form["View"])
            elif request.form["Filter"] != "None":
                Calendar = User_Data.GetFilteredCalendar(Date, request.form["Filter"], request.form["View"])
            return render_template("Calendar.html", Year=today.year, Month=today.month, Day=today.day, Monthlen=Monthlen, Cdata=Calendar)
        except Exception as err:
            return render_template("Error.html", Error=err)
    else:
        return render_template("Calendar.html", Year=today.year, Month=today.month, Day=today.day, Monthlen=Monthlen, Cdata=Calendar)
    
@app.route("/Calendar/Update", methods=["POST", "GET"])
def Update():
    if request.method == "POST" and request.form.get("Update", False) != False:
        try:
            return render_template("Update.html", EventData=request.form.getlist("Calendar-Data"), EventID=request.form["Update"])
        except Exception as err:
            return render_template("Error.html", Error=err)
    elif request.method == "POST" and request.form.get("Update", False) == False:
        try:
            User_Data.UpdateCalendar((request.form["Event-Name"], request.form["Start-Time"], request.form["End-Time"], request.form["Type"], request.form["Priority"], request.form["Submit"]))
            return redirect("/Calendar")
        except Exception as err:
            return render_template("Error.html", Error=err)
    else:
        return render_template("Update.html")

@app.route("/Calendar/Delete", methods=["POST", "GET"])
def Delete():
    if request.method == "POST":
        try:
            User_Data.DeleteCalendar(request.form["Delete"])
            return redirect("/Calendar")
        except Exception as err:
            return render_template("Error.html", Error=err)
    else:
        return render_template("Error.html", Error="There was an error deleting that")

@app.route("/Calendar/Insert", methods=["POST", "GET"])
def Insert():
    if request.method == "POST":
        try:
            User_Data.InsertCalendar([request.form["Event-Name"], request.form["Start-Time"], request.form["End-Time"], request.form["Type"], request.form["Priority"]])
            return redirect("/Calendar")
        except Exception as err:
            return render_template("Error.html", Error=err)
    else:
        return render_template("Insert.html")

@app.route("/Error")
def Error(Error):
    return render_template("Error.html", Error)


if __name__ == "__main__":
    app.run(debug=True)