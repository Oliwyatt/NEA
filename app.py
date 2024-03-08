from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import calendar
import Data

global Current_User
Current_User = Data.user()

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
    Relaxation = Current_User.GetAllRData()
    Calendar = Current_User.GetTodaysCalendar(Date)
    return render_template("Home.html", Name=name, Rdata=Relaxation, Cdata=Calendar)

@app.route("/Calendar", methods=["POST", "GET"])
def Calendar():
    today = date.today()
    Monthlen = calendar.monthrange(today.year, today.month)[1]
    Calendar = Current_User.GetTodaysCalendar(str(today))
    if request.method == "POST":
        try:
            Date = date(int(request.form["Year"]), int(request.form["Month"]), int(request.form["Day"]))
            if request.form["Filter"] == "None":
                Calendar = Current_User.GetCalendar(Date, request.form["View"])
            elif request.form["Filter"] != "None":
                Calendar = Current_User.GetFilteredCalendar(Date, request.form["Filter"], request.form["View"])
            return render_template("Calendar.html", Year=today.year, Month=today.month, Day=today.day, Monthlen=Monthlen, Cdata = Calendar)
        except Exception as err:
            return render_template("Error.html", Error=err)
    else:
        return render_template("Calendar.html", Year=today.year, Month=today.month, Day=today.day, Monthlen=Monthlen, Cdata = Calendar)
    
@app.route("/Calendar/Update" methods=["POST", "GET"])
def Update():
    if request.method == "POST":
        try:
            
    
@app.route("/Error")
def Error(Error):
    return render_template("Error.html", Error)
if __name__ == "__main__":
    app.run(debug=True)