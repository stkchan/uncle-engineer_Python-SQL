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
#################################

L = Label(GUI, text = 'title', font = font2)
L.pack()

# E1 = Entry(GUI)
# E1.pack()

v_title = StringVar()
E1 = ttk.Entry(GUI, textvariable = v_title, font = font1, width = 20)
E1.pack()

def save():
    title = v_title.get() #Extract value from v_title
    messagebox.showinfo('Message', title)

B1 = ttk.Button(GUI, text = 'Save', command = save)
B1.pack(ipadx = 20, ipady = 10, pady= 10)

GUI.mainloop()