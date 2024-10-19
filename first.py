import sqlite3
from datetime import datetime

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
def insert_expense(title, price, others):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')               #Generate timestamp
    with conn:
        command = 'INSERT INTO expense VALUES (?, ?, ?, ?, ?)'      #SQL -- ? = Number of Field/Column when insert data
        c.execute(command, (None, title , price, others, ts))
    conn.commit()                                                   #Save data to database
    print(f'saving completed at {ts}')

#insert_expense('7-11', 20, 'ichitan_greetea')

for i in range(3) :
    print(f'####################{i+1}###########################')
    title = input('title: ')
    price = float(input('price: '))
    others = input('detail: ')
    insert_expense(title, price, others)