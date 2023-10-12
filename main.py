import tkinter as tk
from tkinter import ttk

# window 
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

# title // another way of saying text and master == parent
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field 
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Convert')
entry.pack(side="left", padx = 10)
button.pack(side="left")
input_frame.pack(pady = 10)
# run
window.mainloop()