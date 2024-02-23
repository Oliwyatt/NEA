import sqlite3

Email = ("S2208@st-martins.essex.sch.uk", )

with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT UserID FROM User
                     WHERE Email = ?;
                  """
            cursor.execute(sql, Email)
            result, = cursor.fetchone()
            print(result)