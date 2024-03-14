# NEA
# My A level computer science NEA.
# This whole repository will probably be fairly rough as this is my first time using it and making one.

# My project is a life organiser using an SQL database to store information and using python FLASK for frontend management and HTML + CSS as the frontend.
# The backend will aslo be written in python (dw I'm gonna work on learning other languages).
# It will mostly consist of a calendar and a maybe a film recommendation/show rating storage system as the "relaxation area".

# The SQL Database:
# Will consist of 4 tables one of them a linking table subsequently called "Streaming" to link UserID, ShowID and rating. The other tables are...
# User: Storing user information like name, email, passwords etc.
# Show: Storing information on shows like the name and the ShowID.
# Events: Storing the calendar events that the user inputs, holding the type (personal or work) and having a priority, to be filtered.
# I hope to have SQL permissions on what data they can access and for admin to have any access. (Update: Probably not without changing how the sql is run)

# Frontend:
# The 'website' frontend will have a login system validated with the info on the database.
# Then lead to a main menu where you can choose the calendar area, see your added shows and see todays calendar and log out.
# Then you can go to calendar area which will display the data from the database with varying filters
# You will also be able to delete, edit and add events from here and you will be able to go back to home.

# Backend:
# A class called user is created when someone logs into th database which the relevent information is then retrieved and stored on Current_User.
# The data file holds the user class which has all of the methods required for the website to access and add information on the database.
# The app file holds all the app routes the website navigates, these allow the frontend to send and retrieve information between it and the database.


# This all together makes my webapp.