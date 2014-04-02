# Made by Jamie

from tkinter import *

def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()

### main
window = Tk()
window.title("Minecraft Version Installer")

# menu bar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Options", command=donothing)
filemenu.add_command(label="Exit application", command=donothing)

menubar.add_cascade(label="File", menu=filemenu)

# image 
labelWidget = Label(window)

imgFile = 'logo.gif'
imageObject = PhotoImage(file = imgFile)

labelWidget.pack()

labelWidget['image']=imageObject

### main loop
window.config(menu=menubar)
window.mainloop()
