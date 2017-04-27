from tkinter import * # Imports the tkinter framework.

root = Tk() # Creates a master window.
root.geometry("420x340")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

buttonStatic = Button(topFrame, text='Set Adapter to Static IP')
buttonDHCP = Button(topFrame, text = 'Set Adapter to DHCP')



buttonStatic.pack(side=LEFT)
buttonDHCP.pack(side=LEFT)




root.wm_title("LAN Adapter IP Changer") # Sets the windows title  bar to the app.

root.mainloop() #Keeps the master window open until application is closed.

