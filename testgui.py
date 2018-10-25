from tkinter import *
master = Tk()
master. config(background="pink")
label = Label(master, text="Hockey Pool")
label.config(background="pink")
label.config(foreground="black")
label.pack()
button = Button(master, text="Quit", fg="blue", command=quit)
button.pack(side=BOTTOM)
listbox = Listbox(master)
listbox.config(background="pink")
listbox.config(foreground="black")
listbox.pack()
listbox.insert(END, "Player, Goals")
lst = [["jack fejer",208], ["zane roberge", 234], ["josh heldman", 187], ["jon choptiany", 70]]
for item in lst:
    listbox.insert(END, item[0] + "-" + str(item[1]))
    
mainloop()