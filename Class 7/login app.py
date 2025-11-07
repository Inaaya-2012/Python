import tkinter
from tkinter import *
window = Tk()
window.title("Login")
window.geometry('500x500')
window.configure(bg = 'beige')
def login():
    n = entry1.get()
    msg = "welcome" + n + " you have successfuly logged in!"
    text1 .delete("1.0","end")
    text1.insert("1.0",msg)
frame1 = Frame(window,width = 300,height = 200,bd = 3,bg = 'teal',relief = 'sunken')
label1 = Label(frame1,text = "Name",bg ='teal')
label2 = Label(frame1,text = "Password",bg ='teal')
entry1 = Entry(frame1)
entry2 = Entry(frame1,show = "*")
frame1.pack(pady = 10)

label1.place(x = 30,y = 30)
label2.place(x = 30,y = 80)
entry1.place(x = 150,y = 30)
entry2.place(x = 150,y = 80)
button1 = Button(frame1,text = 'login',width = 10,bg = 'lightgreen',command = login)
button1.place(x= 80,y = 130)

text1 = Text(window,width = 200,height = 10,bd = 5,bg = 'grey',relief = SUNKEN,fg = 'white')
text1.pack(pady = 50)

                 
