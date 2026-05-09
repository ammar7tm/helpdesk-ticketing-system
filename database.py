import sqlite3

def create_database():
    connection = sqlite3.connect("tickets.db")  # connect to the databse file 

    cursor = connection.cursor()    # cursor let us run the SQL command 

    #creating the ticket table 

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

     # save the changes
    connection.commit()

    # close the connection
    connection.close()

# run it
create_database()
print("Database created!")

