import sqlite3

def Initialise():
    # Creating tables if they dont exist
    with sqlite3.connect("Organiser.db") as db:
        cursor = db.cursor()
        # Creating User table
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
        # Creating Event table
        sql = """CREATE TABLE IF NOT EXISTS Event(
                 EventID integer,
                 UserID integer,
                 EventName text,
                 Start DateTime,
                 End DateTime,
                 Type char(1),
                 Priority integer,
                 Primary key(EventID),
                 Foreign key(UserID) References User);
               """
        cursor.execute(sql)
        # Creating Streaming table
        sql = """CREATE TABLE IF NOT EXISTS Streaming(
                 ShowID integer,
                 ShowName text,
                 Rating integer,
                 Primary key(ShowID));
              """
        cursor.execute(sql)
        # Creating Link table
        sql = """CREATE TABLE IF NOT EXISTS Link(
                 UserID integer,
                 ShowID integer,
                 Foreign key(UserID) References User,
                 Foreign key(ShowID) References Streaming,
                 Primary key(UserID, ShowID));
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
        self.FName = ""
        self.LName = ""
        self._Email = ""

    def signup(self):
        # Need FLASK and set up 'website'
        pass
        
        
#Sign up
#log in (access sql)
#password system?

class edit(): #self, user, table, mode):
    pass
    #update
    #insert
    #delete()