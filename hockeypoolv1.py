# imports functiosn from within the tkinter interface
from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

# defines a function in which updates takes data from the addItem function and places it onto a list
def updatelab():
    lstprint = ""
    for item in lst:
        lstprint = lstprint + item + "\n"
    mylab.configure(text=lstprint)

# a function that takes data from the user in which was typed into the addButton and deletes the characters from the user interface. This function will be called upon later in the code
def addItem():
    item = entry.get()
    if (lst.count(item) == 0):
        lst.append(item)
        entry.delete(0, END)
        updatelab()

# a function that when clicked the Remove button tests if the item is in the list and if so removes the item completely and updates the interface        
def remItem():
    item = entry.get()
    if (lst.count(item) > 0):
        lst.remove(item)
        entry.delete(0, END)
        updatelab()
        
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt","Players saved to disk")
 

def scrape():
    if (messagebox.askyesno("wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
        content = BeautifulSoup(site.content, 'html.parser')
        totalpts = 0
        for myplayer in lst:
            dTag = sontent.find(attrs={"csk": myplayer})
            parent = dTag.findParent('tr')
            playerpts = int(parent.contents[8].text)
            print(myplayer + " " + str(playerpts))
            totalpts = totalpts + playerpts
        mypts.configure(text=totalpts)

# creates a list []        
lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leaugues/NHL_2019_skaters.html')

# root creates a user interface within python 
root = Tk()
root.geometry("300x400+0+900")
root.title("hockey pool")
root.config(background = "purple")

# produces text within the user interface for an example of what to write
instlab = Label(root,text="Input (e.g., Mcdavid,Connor): ")
instlab.pack()

entry = Entry(root)
entry.pack()

# this button runs the addItem function once clicked
addbutton = Button(root, text="Add", command=addItem)
addbutton.pack()

rembutton = Button(root, text="Remove", command=remItem)
rembutton.pack()

savebutton = Button(root, text="Save", command=saveList)
savebutton.pack()

getbutton = Button(root, text="Check Points", command=scrape)
getbutton.pack()

mypts = Label(root,text=totalpts)
mypts.pack()

# pack places the label within the user interface
mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
mylab.pack()



# mainloop countinuosly runs the code to ensure the user interface does not disappear
mainloop()
