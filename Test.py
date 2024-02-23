import sqlite3

try:
      Values = (, LName, Email, Password)
      with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """INSERT INTO User (FirstName, LastName, Email, Password, DeleteCal)
                     VALUES (?, ?, ?, ?, 'N');
                  """
            cursor.execute(sql, Values)
            db.commit()

except sqlite3.Error as error:
      print(error)