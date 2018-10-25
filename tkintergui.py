# importing tkinter module into python so it can be used
from tkinter import *
# Tk() makes a window
master = Tk()

def return_entry(en):
    """Gets and prints the content of the entry"""
    content = entry.get()
    print(content)
	
Label(master, text="Input: ").grid(row=0, sticky=W)

#places the entry box inside the master window
entry = Entry(master)

# the placing wihin the window row 0 column 1
entry.grid(row=0, column=1)

#connects the entry with the return button (once you press return the function/code runs)
entry.bind('<Return>', return_entry)

# keeps window open (keeps running through the code)
mainloop()