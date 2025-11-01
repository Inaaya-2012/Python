from tkinter import *
from datetime import date

window = Tk()
window.geometry("400x500")
window.configure(bg = "lightblue")
def greeting():
    name = entry1.get()
    g = "Welcome " + name + "\n Today's date and time is" + str(date.today())
    text1.delete("1.0","end")
    text1.insert("1.0",g)

label1 = Label(text = "Name",bg = "lightblue", fg = "navy")
label1.pack()
entry1 = Entry()
entry1.pack()
button1 = Button(text = "Login",bg = "Navy",fg = "lightblue",command = greeting)
button1.pack()
text1 = Text(bg = "grey",fg = "navy",height = 10,width = 150)
text1.pack()

window.mainloop()
