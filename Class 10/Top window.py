from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("The main window")
def mytoplevel():
    mytop = Toplevel()
    mytop.geometry("100x200")
    mytop.title("Top Level")
    mytop.configure(bg = 'blue')
    label2 = Label(mytop,text = "This is the top window")
    label2.pack()
    mytop.mainloop()

label1 = Label(root,text = "This is the main window")
label1.pack()

button1 = Button(root,text = 'Click me',command = mytoplevel)
button1.pack()
root.mainloop()

    
