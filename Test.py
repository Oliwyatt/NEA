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
