import os
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import_directory = 'B-Dot Data/raw' #Saved as a subfile so the singular directory entry should be fine. File specificication will require manual input.
filenames = os.listdir(import_directory)

root = tk.Tk()
root.title("File Select")
selected_file = tk.StringVar(root)
selected_file.set(filenames[0])
selected_result = {"file_path": None}

dropdown_menu = tk.OptionMenu(root,selected_file,*filenames)
dropdown_menu.pack(padx=20,pady=10)

def show_selection():
    selected = selected_file.get()
    full_path = f"{import_directory}/{selected}"
    print(f"{full_path} selected.")
    selected_result["file_path"] = full_path
    root.destroy()
    

select_button = tk.Button(root,text="Select File", command=show_selection)
select_button.pack(pady=10)
root.mainloop()

print(selected_result['file_path'])
