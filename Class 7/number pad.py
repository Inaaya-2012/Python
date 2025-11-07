import tkinter
from tkinter import *
window = Tk()
window.title("Number Pad")
window.geometry('200x300')
t = [[7,8,9],[4,5,6],[1,2,3],['0','#','*']]
for i in range(0,3+1):
    window.rowconfigure(i,weight = 1,minsize = 80)
    for j in range(0,3):
        window.columnconfigure(j,weight = 1,minsize = 70)
        label = Label(window,relief = RAISED, bg = 'skyblue',fg = 'darkblue',text = t[i][j],width = 3)
        label.grid(row= i,column = j)

windrow.mainloop()    
