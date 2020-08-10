from tkinter import *
from datetime import date
from Project.classframes import MainScreen




root = Tk()
date = date.today()
mainscreen = MainScreen(root, date)
root.mainloop()
