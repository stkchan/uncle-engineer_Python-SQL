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
    conn.commit()                                                   #Save data to database -- Use when data in database has changed For example: if just only Query data no need to commit
    print(f'saving completed at {ts}')  

#insert_expense('7-11', 20, 'ichitan_greetea')

# for i in range(3) :
#     print(f'####################{i+1}###########################')
#     title = input('title: ')
#     price = float(input('price: '))
#     others = input('detail: ')
#     insert_expense(title, price, others)

def view_expense():
    with conn:
        command = 'SELECT * FROM expense' 
        c.execute(command)
        result = c.fetchall()
    # print(result)
    return result


def update_expense(id, field, value):
    with conn:
        command = 'UPDATE expense SET {} = (?) WHERE ID = (?)'.format(field)
        c.execute(command, (value, id))
    conn.commit()                                                   #Save data to database


# update_expense(3, 'price', 12)
def delete_expense(id):
    with conn:
        command = 'DELETE FROM expense WHERE id = {?}'
        c.execute(command, ([id]))
    conn.commit()


data = view_expense()
for i in data :
    print(i)