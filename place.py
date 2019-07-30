import logging
from tkinter import *
import tkinter as tk

class BuildingBase () :

    def __init__(self) :
        
        self.place = None
        self._in = False
        self.username = None

    def is_in(self):
        return self._in

    def showmap (self) :

        window = tk.Tk()

        img = PhotoImage(r"D:\code\PY\comad\COMAD\system\the" + self.place)
        map = Label(window,text='map', image=img, compound=BOTTOM)
        map.pack()

        window.mainloop()

'''
#測試#

logging.warning("Lobby開始")
howard = Lobby()
howard.is_in()
del howard
logging.warning("Lobby結束")
logging.warning("Controlroom開始")
howard = controlroom()
howard.sslcheck()
del howard
logging.warning("Controlroom結束")
'''