from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import Data

app = Flask(__name__)
Data.Initialise()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Organiser.db"
db = SQLAlchemy(app)


@app.route("/", methods=["POST", "GET"])
def index():
    try:
        if request.method == "POST":
            Current_User = Data.user()
            if Current_User.login(Email=request.form["Email"], Password=request.form["Password"]):
                return redirect("/Home")
            else:
                return redirect("/")
        else:
            return render_template("Index.html")
    except:
        print("There was an error with login")
        return redirect("/")


@app.route("/SignUp", methods=["POST", "GET"])
def SignUp():
    if request.method == "POST":
        Current_User = Data.user()
        try:
            if Current_User.signup(FName=request.form["FName"], LName=request.form["LName"], Email=request.form["Email"], Password=request.form["Password"]):
                return redirect("/")
            else:
                return redirect("/SignUp")
        except:
            return redirect("/SignUp")
    else:
        return render_template("SignUp.html")


@app.route("/Home")
def Home():
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True)