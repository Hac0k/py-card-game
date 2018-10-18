from Tkinter import *
from gui.start import Application


root = Tk()
app = gui.start.Application(master=root)
app.mainloop()
root.destroy()
