import sqlite3

conn = sqlite3.connect('expense.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS expense (
                ID      INTEGER PRIMARY KEY AUTOINCREMENT,  
                title   TEXT,
                price   REAL,
                others  TEXT,
                timestamp   TEXT )
          """)


#Insert Data
with conn:
    command = 'INSERT INTO expense VALUES (?, ?, ?, ?, ?)' #SQL
    c.execute(command, (None, '7-11' , 43, 'tofusan_soymilk_chocolate-cacao', '2024-10-19 11:11:11'))
conn.commit() #Save data to database