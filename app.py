from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import Data

app = Flask(__name__)
Data.Initialise()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Organiser.db"
db = SQLAlchemy(app)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        Current_User = Data.user()
        try:
            if Current_User.login(Email=request.form["Email"], Password=request.form["Password"]):
                return render_template("Base.html")
            else:
                return redirect("/")
        except:
            print("There was a problem")
            return redirect("/")
    else:
        return render_template("Index.html")

if __name__ == "__main__":
    app.run(debug=True)