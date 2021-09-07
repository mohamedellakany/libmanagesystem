import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# root.geometry("400x400")
# root.title("Hello")

def greet():
    print ('Hello')

button_one = ttk.Button(root, text="Click me", command=greet).pack(side='left', fill='y')
button_two = ttk.Button(root, text="Quit", command=root.destroy).pack(side='left')

root.mainloop()