from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import webbrowser
import requests
from bs4 import BeautifulSoup

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

site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
               
            totalpts = 0
            for myplayer in lst: # loop to check my players
               dTag = content.find(attrs={"csk": myplayer})
               parent = dTag.findParent('tr')
               playerpts = int(parent.contents[8].text) # 8th tag is total points
               print(myplayer + " " + str(playerpts))
               totalpts = totalpts + playerpts         
            mypts.configure(text=totalpts)
            
    
    
def makeoptions():
    if content != -99:
        names = content.findAll(attrs={"data-stat": "player"})
        playerOptions = []
        for player in names:
            if(player != "None"):
                playerOptions.append(player.get('csk'))
        return playerOptions
            
            
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
    
def addPlayer(event):
    players = []
    name = variable.get()
    if players.count(name) > 0:
        return
        listbox.insert(END, name)
        for i in range(listbox.size()):
            players.append(listbox.get(i))
            
def helpItem():
    helpwindow = Tk()
    helpwindow.geometry("300x320+700+0")
    helpwindow.title("Help")
    
    titleLabel = Label(helpwindow, text = "Help")
    titleLabel.place(x = 100, y = 5)
    messageLabel = Label(helpwindow, text = "1. On the bottom right side of this \n hockeypool software \n there are various buttons which \n help edit your player list \n such as add and remove. \n 2. To add a player, type in the \n player's name \n in the following format \n 'Last,First' and press add. \n 3. To remove a player, click the \n selected player in the listbox \n and click the remove button. \n 4. The pull down in the top right is \n a list of all players in the NHL.\n Select a player to show individual \n statistics of the selected player. \n ")
    messageLabel.place(x = 0, y = 30)
    helpwindow.mainloop()
    
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
    listbox2=Listbox(root,bg='#D552FF')
    listbox2.place(x=220, y=290)
    listbox2.insert(END, "Age: "+ str(age))
    listbox2.insert(END,"Position: "+str(position))
    listbox2.insert(END,"Team: "+str(team))
    listbox2.insert(END,"Points: " + str(points))
    listbox2.insert(END,"Goals: " + str(goals))
    listbox2.insert(END,"Assists: "+str(assists))
    listbox2.insert(END,"Games Played: "+str(games))
    
    
def openwebsite():
    webbrowser.open_new('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")


OPTIONS = makeoptions()
variable = StringVar(root)
pulldown = OptionMenu(root, variable, *OPTIONS, command=createlistbox)
pulldown.place(x=410, y=280)

listbox= Listbox(root,bg='deep sky blue')
listbox.place(x=5,y=290)

entry = Entry(root)     
entry.place(x=5, y=260)

helpbutton = Button(root, text = "Help", command= helpItem)
helpbutton.place(x = 450, y = 340)

addbutton = Button(root, text="Add", command=addItem)
addbutton.place(x=450, y=380)

rembutton = Button(root, text="Remove", command=remItem)
rembutton.place(x=450, y=420)

savebutton = Button(root, text="Save", command=saveList)
savebutton.place(x=450, y=460)

#mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
#mylab.place(x=5, y=150)

ptsbutton = Button(root,text="Check Points", command=scrape)
ptsbutton.place(x=5, y=470)

mypts = Label(root,text=totalpts)
mypts.place(x=120, y=470)

website=Button(root,text="More Info",command=openwebsite)
website.place(x=270, y=470)

mainloop()