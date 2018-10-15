from Tkinter import *
from gui.main import main

class Application():

      def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # main1 = main()
        # createwidgest = main1.createWidgets(self)
        createwidgest = main.createWidgets()

        self.createwidgest

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
