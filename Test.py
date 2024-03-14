"""
import sqlite3
from datetime import datetime

# Define the data to be inserted
event_data = [
    (1, 1, 8),
    (1, 2, 4),
    (1, 3, 9),
    (1, 4, 9),
    (1, 5, 10),
    (1, 6, 7),
    (1, 7, 3),
    (1, 8, 9),
    (1, 9, 10),
    (1, 10, 2)
]

# Connect to the database
conn = sqlite3.connect('Organiser.db')
cursor = conn.cursor()

# Insert data into the Event table
for event in event_data:
    cursor.execute('''INSERT INTO Streaming (UserID, ShowID, Rating)
                      VALUES (?, ?, ?)''', event)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully.")
"""

from datetime import date, timedelta
import calendar

# Day view
"""



# Week view
today = date.today() # Server output
res = today.weekday()
start = date(today.year, today.month, today.day - res)
day_add = 6
Month_end = calendar.monthrange(start.year, start.month)[1]
S_Day = start.day
S_Month = start.month
S_Year = start.year
if S_Day + day_add > Month_end:
    New_Day = (Month_end - S_Day)
    if S_Month == 12:
        New_Month = 1
        New_Year = S_Year + 1
    else:
        New_Month = S_Month + 1
        New_Year = S_Year
    end = date(New_Year, New_Month, New_Day)
else:
    end = date(S_Year, S_Month, S_Day + day_add)

print(str(start), str(end))

# Month view

today = date.today() # Server output
res = calendar.monthrange(today.year, today.month)[1]
start = date(today.year, today.month, 1)
end = date(today.year, today.month, res)
print(str(start), str(end))
"""
"""Date = date.today()
res = Date.weekday()
Year = []
for j in range(1, 12):
    Year.append([i for i in  range(1, calendar.monthrange(Date.year, j)[1]+1)])

if Date.day - res > 0:
    StartDate = Year[Date.month-1][Date.day - res-1]
else:
    NewMonth = Date.month - 1
    NewRes =  (Date.day - res)
    StartDate = Year[NewMonth-1][calendar.monthrange(Date.year, j)[1]]
if StartDate + 6 <= calendar.monthrange(Date.year, Date.month)[1]:
    EndDate = Year[Date.month][StartDate + 6]"""
today = date(2024, 3, 3)
start = today - timedelta(days=today.weekday())
end = start + timedelta(days=6)
print("Today: " + str(today))
print("Start: " + str(start))
print("End: " + str(end))
