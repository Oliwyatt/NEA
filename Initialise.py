import sqlite3

def SetUp():
    with sqlite3.connect("Organiser.db") as db:
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS User(
                 UserID integer,
                 FirstName varchar(20),
                 LastName varchar(20),
                 Email text,
                 Password text,
                 DeleteCal char(1),
                 Primary key(UserID));
              """
        cursor.execute(sql)

def view():
    with sqlite3.connect("Organiser.db") as db:
        cursor = db.cursor()
        sql = """SELECT * FROM USER;"""
        cursor.execute(sql)
        result = cursor.fetchall()

        for each in result:
            print(each)

class user():
    def __init__(self):
        self.__FName = ""
        self.__LName = ""
        self.__Email = ""

    def signup(self):
        pass
        
        
#Sign up
#log in (access sql)
#password system?

class edit(): #self, user, table, mode):
    pass
    #update
    #insert
    #delete
SetUp()
