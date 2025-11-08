from tkinter import *
root = Tk()
root.title("My event Handler")
root.geometry("400x400")
root.configure(bg = 'lightblue')

def key_press(event):
    print(event.char)
root.bind("<Key>",key_press)

def mouse_click(event):
    print("\n The mouse is clicked")
button1 = Button(text = "Click me")
button1.place(x=100,y=100)
button1.bind("<Button-1>",mouse_click)
root.mainloop()
