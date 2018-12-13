from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

def switchPhoto():
	global photo
	my_image = Image.open("headshots/kesseph01.jpg")
	photo = ImageTk.PhotoImage(my_image)
	can.itemconfig(myimg,image=photo)
	

root = Tk()
root.geometry()
root.title("hockey pool")

can = Canvas(root, width=125, height=180)
image1 = Image.open("headshots/marnemi01)
myimg = can.create_image(0, 0, anchor=NW, image=photo)
can.pack()

button = Button(root, text="Change photo", command=switchPhoto)
button.pack() 

listbox


def pulldown():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    Name = 0
    for myplayer in OPTIONS: # loop to check my players
        print("reached loop")
        dTag = content.find(attrs={"csk": myplayer})
        parent = dTag.findParent('tr')
        playername = int(parent.contents[2].text)
        print(myplayer + " " + str(playername))
        name = name + playername
        myname.configure(text=name)