from Tkinter import *
<<<<<<< HEAD
from gui.main import main

class Application():

      def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # main1 = main()
        # createwidgest = main1.createWidgets(self)
        createwidgest = main.createWidgets()

        self.createwidgest

=======
import gui.start  
    
>>>>>>> a6cba43112de4309e52e2404892962a4b96884fa
root = Tk()
app = gui.start.Application(master=root)
app.mainloop()
root.destroy()
