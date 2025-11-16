import tkinter as tk

def check_strength():
    password = password_entry.get()
    length = len(password)

    
    if length == 0:
        result_label.config(text="Enter a password!")
    elif length < 4:
        result_label.config(text="Strength: Very Weak")
    elif length < 7:
        result_label.config(text="Strength: Weak")
    elif length < 10:
        result_label.config(text="Strength: Medium")
    elif length < 13:
        result_label.config(text="Strength: Strong")
    else:
        result_label.config(text="Strength: Very Strong")


window = tk.Tk()
window.title("Password Strength Checker")


tk.Label(window, text="Enter Password:").pack()


password_entry = tk.Entry(window, show="*")
password_entry.pack()


tk.Button(window, text="Check Strength", command=check_strength).pack()


result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()
