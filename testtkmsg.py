import logging
from tkinter import *
from tkinter import messagebox

import pygame

pygame.mixer.init()

class Own_mb :
    def __init__(self, msg = "", height = 115, width = 200, title = "", color = "white"):
        # 建立物件,函數 #
        self.root = Tk()
        
        def choise (ans) :
            if ans == "True" :
                try :
                    sound = pygame.mixer.Sound("system\media\Windows Shutdown.wav")
                    sound.play()
                    del sound
                    quit()
                except Exception as errmsg:
                    logging.error(errmsg)
            else :
                logging.error("登出失效")
            self.root.destroy()
        # 初始化 #
        self.height = str(height)
        self.width = str(width)
        self.title = str(title)
        self.color = str(color)
        self.msg = str(msg)
        self.label = Label(self.root, text = self.msg)
        self.btlabel = Label (self.root, bg = "gray")
        self.yesbutton = Button(self.btlabel, text = "  Yes  ", command = lambda : choise(ans = "True"))
        self.nobutton = Button(self.btlabel, text = "  No  ", command = lambda : choise(ans = "False"))
        def re_config ():
            self.root.geometry("%sx%s" % (self.width, self.height))
        self.root.bind("<Configure>", re_config())
        # 設定 #
        self.root.title(self.title)
        self.root.geometry("%sx%s" % (self.width, self.height))
        self.root.iconbitmap(r"system\1.ico")
        self.root.configure(bg = self.color)
        self.label.place(x = int(self.height)-int(len(msg))-10, y = 25)
        self.btlabel.place(x = 0, y = 85)
        self.nobutton.pack(side=LEFT, padx=50)
        self.yesbutton.pack(side=LEFT, padx=7)
        self.root.mainloop()





main = Own_mb("quit?")
