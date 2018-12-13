from tkinter import *
from tkinter import messagebox

import requests
from bs4 import BeautifulSoup

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
            content = BeautifulSoup(site.content, 'html.parser')                    
            totalpts = 0
            for myplayer in lst: # loop to check my players
               dTag = content.find(attrs={"csk": myplayer})
               parent = dTag.findParent('tr')
               playerpts = int(parent.contents[8].text) # 8th tag is total points
               print(myplayer + " " + str(playerpts))
               totalpts = totalpts + playerpts         
            mypts.configure(text=totalpts)
            
def updatelab():
   lstprint = ""
   for item in lst:
       lstprint = lstprint + item + "\n"
   mylab.configure(text=lstprint) 

def addItem():
   item = entry.get()
   if (lst.count != 0):
      lst.append(item)
      entry.delete(0, END) 
      updatelab()        
            
def remItem():
   item = entry.get()
   if (len(lst) != 0):
      lst.remove(item)
      entry.delete(0, END) 
      updatelab()
      
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Players saved to disk")

lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

root = Tk()
root.geometry("300x400+0+900")
root.title("hockey pool")

instlab = Label(root,text="Input (e.g., McDavid,Connor): ")
instlab.pack() 

entry = Entry(root)     
entry.pack()

addbutton = Button(root, text="Add", command=addItem)
addbutton.pack()

rembutton = Button(root, text="Remove", command=remItem)
rembutton.pack()

savebutton = Button(root, text="Save", command=saveList)
savebutton.pack()

mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
mylab.pack()

ptsbutton = Button(root,text="Check pts", command=scrape)
ptsbutton.pack()

mypts = Label(root,text=totalpts)
mypts.pack()

mainloop()

