import tkinter as tk

def calculate_interest():
    # Get input values from the user
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    # Simple Interest formula
    si = (p * t * r) / 100

   
    ci = p * (1 + r/100) ** t - p

   
    si_label.config(text="Simple Interest: " + str(round(si, 2)))
    ci_label.config(text="Compound Interest: " + str(round(ci, 2)))


window = tk.Tk()
window.title("Interest Calculator")


tk.Label(window, text="Enter Principal:").pack()
principal_entry = tk.Entry(window)
principal_entry.pack()


tk.Label(window, text="Enter Time (years):").pack()
time_entry = tk.Entry(window)
time_entry.pack()


tk.Label(window, text="Enter Rate (%):").pack()
rate_entry = tk.Entry(window)
rate_entry.pack()


tk.Button(window, text="Calculate", command=calculate_interest).pack()


si_label = tk.Label(window, text="Simple Interest: ")
si_label.pack()

ci_label = tk.Label(window, text="Compound Interest: ")
ci_label.pack()


window.mainloop()
