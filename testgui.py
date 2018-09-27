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
lst = [["connor mcdavid",208], ["sidney crosby", 234], ["steven stamkos", 187], ["auston mathews", 70]]
for item in lst:
    listbox.insert(END, item[0] + "-" + str(item[1]))
    
mainloop()