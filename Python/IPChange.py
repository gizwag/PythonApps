from tkinter import * # Imports the tkinter framework.



class OptionButtons:


    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.staticButton = Button(frame, text='Set Adapter to Static IP', command=self.setStaticIP)
        self.staticButton.pack(side=LEFT)

        self.staticButton = Button(frame, text='Set Adapter to Dynamic IP', command=self.setDHCP)
        self.staticButton.pack(side=LEFT)

        self.exitButton = Button(frame, text='Exit', command=frame.quit)
        self.exitButton.pack()


        self.msg = Message(master, text="")
        self.msg.pack(side=LEFT)






    def setStaticIP(self):
       #print ("IP address has been made static")
        txt = "I pressed Static"

    def setDHCP(self):
        print ("IP address has been made dynamic")







root = Tk() # Creates a master window.
buttons = OptionButtons(root)
root.wm_title("LAN Adapter IP Changer") # Sets the windows title  bar to the app.
root.geometry("420x340")

root.mainloop() #Keeps the master window open until application is closed.