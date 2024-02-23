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
                 Email text UNIQUE,
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
        self.FName = "" # Is public to use in website
        self.LName = ""
        self._Email = "" # Is protected no need to use in website
        self._Password = ""
        self.__UserID = 0 # Is private, would not be good if info was found

# Setters and Getters
        
    def GetFName(self):
        return self.FName
    
    def GetLName(self):
        return self.LName
    
    def Get_Email(self):
        return self._Email
    
    def Get_Password(self):
        return self._Password
    
    def Get__UserID(self):
        return self.__UserID
    
    def SetFName(self, FName):
        self.FName = FName

    def SetLName(self, LName):
        self.LName = LName

    def Set_Email(self, Email):
        self._Email = Email

    def Set_Password(self, Password):
        self._Password = Password

    def Set__UserID(self, UserID):
        self.__UserID = UserID
    
# Find values from SQL database
    
    def Find__UserID(self, Email):
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
        
    def signup(self, **kwargs): # Passes through many values so would not crash from extra ones
        self.SetFName(kwargs["FName"])
        self.SetLName(kwargs["LName"])
        self.Set_Email(kwargs["Email"])
        self.Set_Password(kwargs["Password"])
        try: # Attempt to create account using values
            self.CreateAccount(self.GetFName(), self.GetLName(), self.Get_Email, self.Get_Password)
        except:
            print("Error there is something wrong with those values for the database.")
            return False
        
    def login(self, **kwargs):
        self.Set_Email(kwargs["Email"])
        self.Set_Password(kwargs["Password"])
        self.Set__UserID(self.Find__UserID(self.Get_Email())) # Setting user id using email because email is unique
        if self.Check_Password(self.Get_Password(), self.Get__UserID()):
            self.SetFName(self.FindFName(self.Get__UserID())) # Retrieving relevent info from database
            self.SetLName(self.FindLName(self.Get__UserID()))
            return True # Login was successfull
        else:
            return False # Login Failed wrong email or password

#Sign up
#log in (access sql)
#password system?

class edit(): #self, user, table, mode):
    pass
    #update
    #insert
    #delete()