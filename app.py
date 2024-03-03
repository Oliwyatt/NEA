from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date
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
        return render_template("/Error", Error=err)


@app.route("/SignUp", methods=["POST", "GET"])
def SignUp():
    if request.method == "POST":
        try:
            if Current_User.signup(FName=request.form["FName"], LName=request.form["LName"], Email=request.form["Email"], Password=request.form["Password"]):
                return redirect("/")
            else:
                return redirect("/SignUp")
        except Exception as err:
            return render_template("/Error", Error=err)
    else:
        return render_template("SignUp.html")


@app.route("/Home", methods=["POST", "GET"])
def Home():
    name = Current_User.GetFName()
    Date = str(date.today())
    relaxation = Current_User.GetAllRData()
    calendar = Current_User.GetTodaysCalendar(Date)
    print(relaxation)
    print(calendar)
    return render_template("Home.html", Name=name, Rdata = relaxation, Cdata = calendar)

@app.route("/Calendar", methods=["POST", "GET"])
def Calendar():
    return render_template("Calendar.html")

if __name__ == "__main__":
    app.run(debug=True)