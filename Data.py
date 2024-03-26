import sqlite3
from datetime import date, timedelta
from calendar import monthrange

def Initialise():
    # Creating tables if they dont exist
    with sqlite3.connect("Organiser.db") as db:
        cursor = db.cursor()
        # Creating User table
        sql = """CREATE TABLE IF NOT EXISTS User(
                 UserID INT AUTO_INCREMENT,
                 FirstName VARCHAR(20),
                 LastName VARCHAR(20),
                 Email TEXT UNIQUE NOT NULL,
                 Password TEXT NOT NULL,
                 PRIMARY KEY(UserID));
              """
        cursor.execute(sql)
        # Creating Event table
        sql = """CREATE TABLE IF NOT EXISTS Event(
                 EventID INT AUTO_INCREMENT,
                 UserID INT,
                 EventName TEXT NOT NULL,
                 Start DATETIME NOT NULL,
                 End DATETIME NOT NULL,
                 Type CHAR(1),
                 Priority INT NOT NULL,
                 PRIMARY KEY(EventID),
                 FOREIGN KEY(UserID) REFERENCES User);
               """
        cursor.execute(sql)
        # Creating Show table
        sql = """CREATE TABLE IF NOT EXISTS Show(
                 ShowID INT AUTO_INCREMENT,
                 ShowName TEXT NOT NULL,
                 PRIMARY KEY(ShowID));
              """
        cursor.execute(sql)
        # Creating Streaming table
        sql = """CREATE TABLE IF NOT EXISTS Streaming(
                 UserID INT,
                 ShowID INT,
                 Rating INT,
                 FOREIGN KEY(UserID) REFERENCES User,
                 FOREIGN KEY(ShowID) REFERENCES Streaming,
                 PRIMARY KEY(UserID, ShowID));
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
        self.FName = "" # Is public to use in website
        self.LName = ""
        self._Email = "" # Is protected no need to use in website
        self._Password = ""
        self._UserID = 0 # Is protected, would not be good if info was found only needed in tables

# Setters and Getters
        
    def GetFName(self):
        return self.FName
    
    def GetLName(self):
        return self.LName
    
    def Get_Email(self):
        return self._Email
    
    def Get_Password(self):
        return self._Password
    
    def Get_UserID(self):
        return self._UserID
    
    def SetFName(self, FName):
        self.FName = FName

    def SetLName(self, LName):
        self.LName = LName

    def Set_Email(self, Email):
        self._Email = Email

    def Set_Password(self, Password):
        self._Password = Password

    def Set_UserID(self, UserID):
        self._UserID = UserID
    
# Find values from SQL database
    
    def Find_UserID(self, Email):
        Values = (Email,)
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT UserID FROM User
                     WHERE Email = ?;
                  """
            cursor.execute(sql, Values) # SQL Injection handling
            result, = cursor.fetchone() # Gets the value from the returned tuple.
            return result
        
    def FindFName(self, UserID):
        Values = (UserID,)
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT FirstName FROM User
                     WHERE UserID = ?;
                  """
            cursor.execute(sql, Values)
            result, = cursor.fetchone()
            return result
        
    def FindLName(self, UserID):
        Values = (UserID,)
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT LastName FROM User
                     WHERE UserID = ?;
                  """
            cursor.execute(sql, Values)
            result, = cursor.fetchone()
            return result
        
    def Check_Password(self, Password, UserID):
        Values = (UserID,)
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT Password FROM User
                     WHERE UserID = ?;
                  """
            cursor.execute(sql, Values)
            result, = cursor.fetchone()
            if result == Password:
                return True
            else:
                return False

# Sign up and login
            
    def CreateAccount(self, FName, LName, Email, Password):
        Values = (FName, LName, Email, Password)
        try:
            with sqlite3.connect("Organiser.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO User (FirstName, LastName, Email, Password)
                         VALUES (?, ?, ?, ?);
                    """
                cursor.execute(sql, Values)
                db.commit()
                return True
        except sqlite3.Error as error:
            print("Failed to insert variables into table", error)
            return False
        
    def signup(self, **kwargs): # Passes through many values so would not crash from extra ones
        self.SetFName(kwargs["FName"])
        self.SetLName(kwargs["LName"])
        self.Set_Email(kwargs["Email"])
        self.Set_Password(kwargs["Password"])
        try: # Attempt to create account using values
            if self.CreateAccount(self.GetFName(), self.GetLName(), self.Get_Email(), self.Get_Password()):
                return True
        except:
            print("Error there is something wrong with those values for the database.")
            return False
        
        
    def login(self, **kwargs):
        self.Set_Email(kwargs["Email"])
        self.Set_Password(kwargs["Password"])
        try:
            self.Set_UserID(self.Find_UserID(self.Get_Email())) # Setting user id using email because email is unique
        except:
            return False # Login Failed wrong email
        if self.Check_Password(self.Get_Password(), self.Get_UserID()):
            self.SetFName(self.FindFName(self.Get_UserID())) # Retrieving relevent info from database
            self.SetLName(self.FindLName(self.Get_UserID()))
            return True # Login was successfull
        else:
            return False # Login Failed wrong password


class Tables():
    def __init__(self, User):
        self.__User = User

    def GetAllRData(self):
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT Show.ShowName, Streaming.Rating FROM Streaming
                     INNER JOIN Show
                     ON Streaming.ShowID = Show.ShowID
                     WHERE UserID = ?
                     ORDER BY Streaming.Rating DESC;
                  """
            Values = (self.__User.Get_UserID(),)
            cursor.execute(sql, Values)
            result = cursor.fetchall()
            return result
        
    def __GetWeek(self, Date): # Gets the week to display
        start = Date - timedelta(days=Date.weekday())
        end = start + timedelta(days=7)
        return start, end
    
    def __GetMonth(self, Date): # Gets the month to display
        res = monthrange(Date.year, Date.month)[1]
        start = date(Date.year, Date.month, 1)
        end = date(Date.year, Date.month, res)
        return start, end
        
    def GetTodaysCalendar(self, Date):
        Date = "%"+Date+"%"
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT EventID, EventName, Start, End, Type, Priority FROM Event
                     WHERE UserID = ? AND Start LIKE ?
                     ORDER BY Start;
                  """
            Values = (self.__User.Get_UserID(), Date)
            cursor.execute(sql, Values)
            result = cursor.fetchall()
            return result
    
    def GetCalendar(self, Date, View):
        if View == "Week":
            start, end = self.__GetWeek(Date)
        elif View == "Month":
            start, end = self.__GetMonth(Date)
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """SELECT EventID, EventName, Start, End, Type, Priority FROM Event
                     WHERE UserID = ? AND Start BETWEEN ? AND ?
                     ORDER BY START;
                  """
            Values = (self.__User.Get_UserID(), str(start), str(end))
            cursor.execute(sql, Values)
            result = cursor.fetchall()
            return result
        
    def GetFilteredCalendar(self, Date, Filter, View):
        if View == "Week":
            start, end = self.__GetWeek(Date)
        elif View == "Month":
            start, end = self.__GetMonth(Date)
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            if Filter != "Priority":
                sql = """SELECT EventID, EventName, Start, End, Type, Priority FROM Event
                        WHERE UserID = ? AND Type = ? AND Start BETWEEN ? AND ?
                        ORDER BY START;
                    """
                Values = (self.__User.Get_UserID(),Filter ,str(start), str(end))
            else:
                sql = """SELECT EventID, EventName, Start, End, Type, Priority FROM Event
                        WHERE UserID = ? AND Start BETWEEN ? AND ?
                        ORDER BY Priority;
                    """
                Values = (self.__User.Get_UserID(), str(start), str(end))
            
            cursor.execute(sql, Values)
            result = cursor.fetchall()
            return result
        
    def InsertCalendar(self, Values):
        Values.insert(0, self.__User.Get_UserID())
        Values = tuple(Values)
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """INSERT INTO Event(UserID, EventName, Start, End, Type, Priority)
                     VALUES(?, ?, ?, ?, ?, ?);
                  """
            cursor.execute(sql, Values)
            db.commit()
    
    def UpdateCalendar(self, Values):
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """UPDATE Event
                     SET EventName = ?, Start = ?, End = ?, Type = ?, Priority = ?
                     WHERE EventID = ?;
                  """
            cursor.execute(sql, Values)
            db.commit()

    def DeleteCalendar(self, EventID):
        with sqlite3.connect("Organiser.db") as db:
            cursor = db.cursor()
            sql = """Delete From Event
                     Where EventID = ?;
                  """
            Value = (EventID,)
            cursor.execute(sql, Value)
            sql = """REINDEX Event;"""
            cursor.execute(sql)
            db.commit()