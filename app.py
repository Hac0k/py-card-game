from Tkinter import *
from gui import *

class Application(Frame):

      def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        createwidgest = new main.createWidgets(self)
        self.createwidgest

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
