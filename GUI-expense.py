from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import os


######################## SQL ########################
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


####################################################



GUI = Tk()
GUI.title('Expenses Tracker')
GUI.geometry('700x600')

font1 = ('Google Sans', 20)
font2 = ('Angsana New', 30)

#Creating Tab name & icon
path = os.getcwd() #Check current folder
tab = ttk.Notebook(GUI)
tab.pack(fill = BOTH, expand = 1)

T1 = Frame(tab)
T2 = Frame(tab)

icon_t1 = os.path.join(path, 'picture-1.png') #Get picuture file
icon_t2 = os.path.join(path, 'picture-2.png') #Get picuture file
iconimage_t1 = PhotoImage(file = icon_t1)
iconimage_t2 = PhotoImage(file = icon_t2)


tab.add(T1, text = 'Expense Record',  image = iconimage_t1, compound = 'left') #compound = define where the icon should be located
tab.add(T2, text = 'Expense History', image = iconimage_t2, compound = 'left')


#Creating Icon
path =  os.getcwd() #Check current folder
icon =  os.path.join(path, 'wallet-1.png')
iconimage = PhotoImage(file = icon)

L = Label(T1, image = iconimage)
L.pack()


#Creating Label
L = Label(T1, text = 'Expenses Tracker', font = ('Google Sans', 20, 'bold'))
L.pack(pady = 10)
# L.place(x = 300, y = 300)
# L.grid(row = 0, column = 0)


#Title
L = Label(T1, text = 'title', font = font2)
L.pack()

v_title = StringVar()
E1 = ttk.Entry(T1, textvariable = v_title, font = font1, width = 20)
E1.pack()


#Price
L = Label(T1, text = 'price', font = font2)
L.pack()

v_price = StringVar()
E2 = ttk.Entry(T1, textvariable = v_price, font = font1, width = 20)
E2.pack()


#Others
L = Label(T1, text = 'others', font = font2)
L.pack()

v_others = StringVar()
E3 = ttk.Entry(T1, textvariable = v_others, font = font1, width = 20)
E3.pack()



def save(event=None):

    #If there is no price value please popup message
    if v_price.get() == '' :
        E2.focus()
        messagebox.showinfo("Please fill in the price information.")

    else :
        title  = v_title.get() 
        price  = float(v_price.get())
        others = v_others.get()

        print(title, price, others)
        insert_expense(title, price, others)

        #Clear values in form
        v_title.set('') 
        v_price.set('')
        v_others.set('')

        #Make cursor mouse at title after clicking save
        E1.focus()

        # messagebox.showinfo('Message', title)


#Using for pressing Enter button without clicking on it
E3.bind('<Return>', save) # Apply event=None in function "save" & '<Return>' = Enter button


#Create "Save" button
B1 = ttk.Button(T1, text = 'Save', command = save)
B1.pack(ipadx = 20, ipady = 10, pady= 10)


###################### TAB2 ###################### 


GUI.mainloop()