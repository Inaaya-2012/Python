from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Messagebox")
root.geometry("400x400+300+200")
root.configure(bg = 'lightgreen')
def msg():
    messagebox.showwarning("ALert","Stop!! Virus Found")

button1 = Button(root,text = 'Scan for virus',command = msg)
button1.place(x=150,y=150)

root.mainloop()
