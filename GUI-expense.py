from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Expenses Tracker')
GUI.geometry('700x600')

font1 = ('Google Sans', 20)
font2 = ('Angsana New', 30)

##################################
L = Label(GUI, text = 'Expenses Tracker', font = ('Google Sans', 20, 'bold'))
L.pack(pady = 10)
# L.place(x = 300, y = 300)
# L.grid(row = 0, column = 0)


#Title
L = Label(GUI, text = 'title', font = font2)
L.pack()

v_title = StringVar()
E1 = ttk.Entry(GUI, textvariable = v_title, font = font1, width = 20)
E1.pack()


#Price
L = Label(GUI, text = 'price', font = font2)
L.pack()

v_price = StringVar()
E2 = ttk.Entry(GUI, textvariable = v_price, font = font1, width = 20)
E2.pack()


#Others
L = Label(GUI, text = 'others', font = font2)
L.pack()

v_others = StringVar()
E3 = ttk.Entry(GUI, textvariable = v_others, font = font1, width = 20)
E3.pack()



def save(event=None):
    title  = v_title.get() 
    price  = float(v_price.get())
    others = v_others.get()

    print(title, price, others)

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
B1 = ttk.Button(GUI, text = 'Save', command = save)
B1.pack(ipadx = 20, ipady = 10, pady= 10)

GUI.mainloop()