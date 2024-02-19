5# https://nitratine.net/blog/post/how-to-create-dialogs-in-python/

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

parent = tkinter.Tk() # Create the object
parent.eval('tk::PlaceWindow . center') # Place window in center 
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
parent.iconbitmap("PythonIcon.ico") # Set an icon (this is optional - must be in a .ico format)
parent.withdraw() # Hide the window as we do not want to see this one

# After creating parent...

# Message Dialogs

info = messagebox.showinfo('Information Title', 'A simple message with an information icon', parent=parent)
warn = messagebox.showwarning('Warning Title', 'A simple message with a warning icon', parent=parent)
error = messagebox.showerror('Error Title', 'A simple message with an error icon', parent=parent)

# Question Dialogs

okcancel = messagebox.askokcancel('Question Title', 'Do you want to perform this action?', parent=parent) # OK / Cancel
retrycancel = messagebox.askretrycancel('Question Title', 'Do you want to retry?', parent=parent) # Retry / Cancel
yesno = messagebox.askyesno('Question Title', 'Are you sure you want to undo?', parent=parent) # Yes / No
yesnocancel = messagebox.askyesnocancel('Question Title', 'Are you sure you want to undo?', parent=parent) # Yes / No / Cancel

# Input Dialogs

string_value = simpledialog.askstring('Dialog Title', 'What is your name?', parent=parent)
integer_value = simpledialog.askinteger('Dialog Title', 'What is your age?', minvalue=0, maxvalue=100, parent=parent)
float_value = simpledialog.askfloat('Dialog Title', 'What is your salary?', minvalue=0.0, maxvalue=100000.0, parent=parent)

# File / Folder Dialogs

directory = filedialog.askdirectory(title='Select a folder', parent=parent)

# Ask the user to select a single file name.
file_name = filedialog.askopenfilename(title='Select a file', parent=parent)
# Ask the user to select a one or more file names.
file_names = filedialog.askopenfilenames(title='Select one or more files', parent=parent)
# Ask the user to select a single file name for saving.
save_as = filedialog.asksaveasfilename(title='Save as', parent=parent)

directory_to_start_from = 'C:/Users/User/Downloads/'
directory = filedialog.askdirectory(initialdir=directory_to_start_from, title='Please select a folder:', parent=parent)

parent.destroy()


