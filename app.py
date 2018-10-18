from Tkinter import *
from gui.start import Application


root = Tk()
app = start.Application(master=root)
app.mainloop()
root.destroy()
