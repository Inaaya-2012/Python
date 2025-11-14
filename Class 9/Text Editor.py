import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

window = Tk()
window.title("Text  Editor")
window.geometry("500x500")
def open_file():
    file1 = askopenfile(mode = 'r',filetypes = [('text files','*.txt'),('PYTHON FILES','*.py')])
    if file1 is not None:
                   content = file1.read()
                   text1.delete("1.0","end",)
                   text1.insert(END,content)
    file1.close()

def save_file():
    file1 = asksaveasfile(mode = "w",filetypes = [('text files','*.txt')])
    if file1 is not None:
                       mytext = text1.get(1.0,END)
                       file1.write(mytext)
    file1.close()

text1 = Text(window,width = 50,height = 20,relief = 'sunken',border = 3)
button1 = Button(window,width = 10,text = "Open",command = open_file)
button2 = Button(window,width = 10,text = "Save",command = save_file)
button1.grid(row =1,column = 1)
button2.grid(row = 2,column = 1)
text1.grid(row = 1,column = 2,pady = 20,rowspan = 2)
window.mainloop()


                       
                                               
