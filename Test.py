import sqlite3
from datetime import datetime

# Define the data to be inserted
event_data = [
    (1, "Stranger Things"),
    (2, "The Crown"),
    (3, "Breaking Bad"),
    (4, "Friends"),
    (5, "Game of Thrones"),
    (6, "The Office"),
    (7, "Black Mirror"),
    (8, "The Mandalorian"),
    (9, "The Witcher"),
    (10, "Money Heist")
]

# Connect to the database
conn = sqlite3.connect('Organiser.db')
cursor = conn.cursor()

# Insert data into the Event table
for event in event_data:
    cursor.execute('''INSERT INTO Show (ShowID, ShowName)
                      VALUES (?, ?)''', event)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully.")
