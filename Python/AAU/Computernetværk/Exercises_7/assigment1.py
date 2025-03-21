import sqlite3 as lite
import sys

# Create a version of the database in database file (.db)
DB_NAME = "assigment1.db"
con = lite.connect(DB_NAME)

# Create a version of the database in RAM 
# con = lite.connect(':memory:')

# Creates the SQLite cursor that is used to query the database
cur = con.cursor()  

# Execute desired SQL script
cur.executescript("""
    DROP TABLE IF EXISTS Cars;
    CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
    INSERT INTO Cars VALUES(1,'Audi',52642);
    INSERT INTO Cars VALUES(2,'Mercedes',57127);
    INSERT INTO Cars VALUES(3,'Skoda',9000);
    INSERT INTO Cars VALUES(4,'Volvo',29000);
    INSERT INTO Cars VALUES(5,'Bentley',350000);
    INSERT INTO Cars VALUES(6,'Citroen',21000);
    INSERT INTO Cars VALUES(7,'Hummer',41400);
    INSERT INTO Cars VALUES(8,'Volkswagen',21600);
    """)

# Force the database to make changes with the commit command
con.commit()

# Execute simple SQL query
cur.execute('SELECT Name FROM Cars WHERE Price < 30000 ORDER BY Price')
for i in cur:
    print("\n")
    for j in i:
        print(j)

# Close the database
con.close()
