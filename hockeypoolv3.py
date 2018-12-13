from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

import requests
from bs4 import BeautifulSoup

print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
else:
    content = -99

def makeList():
	if content != -99:
		names = content.findAll(attrs={"data-stat" : "player"})
		playerlist = []
		for player in names:
			if (player != "None"):
				playerlist.append(player.get('csk'))
		return playerlist

def createlistbox(evt):  
    
    var = variable.get()
    print(variable)
    if var != None:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        points=int(parent.contents[8].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        games=int(parent.contents[5].text)
        minutes=int(parent.contents[21].text)
        team=parent.contents[3].text
        position=parent.contents[4].text
        age=int(parent.contents[2].text)
        average=float(parent.contents[20].text)
        plusminus=int(parent.contents[9].text)
    listbox2 = Listbox(root)
    listbox2.place(x=440, y=255)
    listbox2.insert(END, "Age: "+ str(age))
    listbox2.insert(END,"Position: "+str(position))
    listbox2.insert(END,"Team: "+str(team))
    listbox2.insert(END,"Points: " + str(points))
    listbox2.insert(END,"Goals: " + str(goals))
    listbox2.insert(END,"Assists: "+str(assists))
    listbox2.insert(END,"+/-: "+str(plusminus))
    listbox2.insert(END,"Shooting %: "+str(average))
    listbox2.insert(END,"Games Played: "+str(games))
    listbox2.insert(END,"Minutes Played: "+str(minutes))

        

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    totalpts = 0
    for myplayer in lst: # loop to check my players
        print("reached loop")
        dTag = content.find(attrs={"csk": myplayer})
        parent = dTag.findParent('tr')
        playerpts = int(parent.contents[8].text) # 8th tag is total points
        print(myplayer + " " + str(playerpts))
        totalpts = totalpts + playerpts
        mypts.configure(text=totalpts)
        

              
            
def updatelab():
    item = lst[-1]
    listbox.insert(END,item)
        
       
def addItem():
   item = entry.get() # gets text from entry 
   if (lst.count != 0):
      lst.append(item)
      print(lst)
      entry.delete(0, END) 
      updatelab()        
            
def remItem():
    """removes selected item"""
    listbox.delete(ANCHOR) 
    item = (ANCHOR)
    item = lst[0]
    lst.remove(item)
   
          
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Players saved to disk")
    
listbox = []
listboxprint = ""
totalpts = 0
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
    
    
root = Tk()
root.geometry("520x500+0+1000")
root.title("Hockey Pool")
root.config(background = "white")

can = Canvas(root, width=500, height=250)
can.grid(row=0,column=0,padx=10, pady=10)
image1 = Image.open("mcdavid.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

can.create_oval(125, 25, 175, 75, fill="black", outline="#DDD", width=4)
can.create_line(50, 50, 120, 50, fill="#DDD", width=4)
can.create_line(75, 40, 120, 40, fill="#DDD", width=4)
can.create_line(75, 60, 120, 60, fill="#DDD", width=4)
can.create_text(150,50, text="pool", fill="white")

listbox = Listbox(root,height=7)
listbox.place(x=10,y=300)

OPTIONS = makeList()
variable = StringVar(root)
variable.set(OPTIONS[0])
w = OptionMenu(root, variable, *OPTIONS, command=makeList)
w.place(x=380,y=290)


addbutton = Button(root, text="Add", command=addItem)
addbutton.place(x=440,y=340)

savebutton = Button(root, text="Save", command=saveList)
savebutton.place(x=435,y=440)

ptsbutton = Button(root,text="Check Points", command=scrape)
ptsbutton.place(x=10,y=270)

rembutton = Button(root, text="Remove", command=remItem)
rembutton.place(x=420,y=380)

entry = Entry(root)
entry.place(x=10,y=450)

mypts = Label(root,text=totalpts)
mypts.place(x=30,y=425)

mylab = Label(root,text=listboxprint,anchor=W,justify=LEFT)
mylab.place(x=10,y=470)


mainloop()