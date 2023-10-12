import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk # takes ttk styling and converts them for more styling options

def convert():
  mile_input = entry_Int.get()
  km_output = mile_input * 1.61
  output_string.set(km_output)

# window 
window = ttk.Window(themename='darkly')
window.title("Demo")
window.geometry("300x150")

# title // another way of saying text and master == parent
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field 
input_frame = ttk.Frame(master = window)
entry_Int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_Int)
button = ttk.Button(master = input_frame, text = 'Convert', command= convert)
entry.pack(side="left", padx = 10)
button.pack(side="left")
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text="Output",  font = 'Calibri 24', textvariable=output_string)
output_label.pack(pady = 10)
# run
window.mainloop()