from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import Data

app = Flask(__name__)
Data.Initialise()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Organiser.db"
db = SQLAlchemy(app)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        Current_User = Data.user(email=request.form["Email"], password=request.form["Password"])
    else:
        return render_template("Index.html")
    return render_template("Index.html")

if __name__ == "__main__":
    app.run(debug=True)