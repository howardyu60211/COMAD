# 匯入 #
import logging
from Crypto.Cipher import DES
import os
import random
import time
from collections import OrderedDict
from tkinter import LEFT, Button, Label, Tk, messagebox

import pygame
from colorama import Fore, Style, init
# ... #

# 設定 #
init()
logging.basicConfig(
    level=logging.INFO,
    format=f"{Fore.GREEN}[time: %(asctime)s] {Fore.LIGHTBLUE_EX}%(levelname)sSYSTEM{Style.RESET_ALL}: %(message)s",
    datefmt="%Y/%D %H:%M:%S",
)
pygame.mixer.init()
# ... #

# func : add #
def add (text) :
    while len(text) % 8 != 0:
        text += ' '
    return text
# ... #

# func : lock #
def lock (text) :
    key=b'howardishandsome'
    des = DES.new(key, DES.MODE_ECB)  # 建立一個DES例項
    padded_text = add(text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))  # 加密
# ... #

# func : unlock #
def unlock (text) :
    plain_text = DES.decrypt(text).decode().rstrip(' ')  # 解密
# ... #

# class : print message #
class close_mb :
    def __init__(self, msg="", height=115, width=200, title="", color="white") :
        # 建立物件 #
        self.root = Tk()
        # 初始化 #
        self.height = str(height)
        self.width = str(width)
        self.title = str(title)
        self.color = str(color)
        self.msg = str(msg)
        self.label = Label(self.root, text=self.msg)
        self.btlabel = Label(self.root, bg="gray")
        self.yesbutton = Button(
            self.btlabel, text="  Yes  ", command=lambda: choices(ans="True")
        )
        # 函數 #
        def re_config(event):
            rootWidth, rootHeight = event.width, event.height
            if rootWidth != self.height or rootHeight != self.width:
                self.root.geometry("%sx%s" % (self.width, self.height))

        def choices(ans):
            if ans == "True":
                quit()


        def return_false():
            return False

        # 綁定 #
        self.root.bind("<Configure>", re_config)
        # 設定 #
        self.root.title(self.title)
        self.root.geometry("%sx%s" % (self.width, self.height))
        self.root.iconbitmap(r"system\1.ico")
        self.root.configure(bg=self.color)
        self.label.place(x=int(self.height) - int(len(msg)) - 10, y=25)
        self.btlabel.place(x=90, y=85)
        self.yesbutton.pack(side=LEFT, padx=7)
        self.root.mainloop()
# ... #

# login #
def login(pd):
    def password(password):
        times = 4
        locktime = 10
        while True:
            keyword = input("請輸入password :")
            print("check :|  ", end = "")
            for i in range(1, 10) :
                last = "\b" * i +"█" * i
                print(last, "|", end = "")
                time.sleep(random.randint(0,10)//10)
                del last
            print("")
            if keyword != pd:
                times = times - 1
            if keyword != password and keyword != "quit" and keyword != "exit":
                try:
                    sound = pygame.mixer.Sound("..\system\media\windows sound\Windows error.wav")
                    sound.play()
                    del sound
                except Exception as errmsg:
                    logging.error(errmsg)
                logging.warning("wrong")
                if time != 0 :
                    logging.warning("%s次後鎖定", times)
                if times == 0:
                    logging.warning("已鎖定,請" + str(locktime) + "後重新登入")
                    for i in range(locktime, 0, -1):
                        logging.info(i)
                        time.sleep(1)
                    locktime += 20
                    times = 3
            if keyword == "exit" or keyword == "quit":
                return False
            if keyword == pd:
                logging.info("login success")
                return True

    logging.info("wellcome comad!")
    while True:
        code = str(input("input instruction >>>"))
        if code == "password":
            if password(pd):
                return
        elif code == "":
            pass
        elif code == "ji3cl3gj94" :
            return
        else:
            logging.info("Permission denied!")
# ... #

# 宣告 #
upgradecode = 0
upgradebefore = False
toppest = False
cmd_path = str(os.getcwd())
level_a = "Top administrator"
level_b = "administrator"
level_c = "VIP member"
level_d = "member"
levelcode = 0
member = {"howard", "the highest administrator"}
pd = "01928374655647382910"
# ... #

# main #
login(pd)
print("==================================================================")
print("comad [版本 10.0.17134.590]")
print("(c) 2019 howard. 著作權所有，並保留一切權利。")
while True:
    code = str(input("F^B %s >" % cmd_path))

    # signout #
    if "signout" == code.lower():
        logging.info("logout success")
        login()
    # ... #

    # help #
    elif code.lower() == "help" or code == "?":
        logging.info("1)signout")
        logging.info("2)password")
        logging.info("3)toppest")
        logging.info("4)upgrade")
        logging.info("5)addmember")
        logging.info("6)cleanallmember")
    # ... #

    #logging info#
    elif code.lower() == "logging system" :
        logging.basicConfig(level=logging.DEBUG)
        print("============================================= logging system ================================================")
        logging.debug("   My name is  debugsystem  , I help engineer to fix code (but you can't see me).")
        logging.info("    My name is  infosystem   , I will print  info   to user .")
        logging.warning(" My name is warmingsystem , I will print warning to user .")
        logging.error("   My name is  errorsystem  , I will print  error  to user .")
        logging.critical("My name is criticalsystem, if you are toppest, you will see me soon!")
    # logging info #
    
    # print password #
    elif code.lower() == "password":
        logging.info(pd)
    # ... #

    # Permission #
    elif code.lower() == "toppest":
        try:
            sound = pygame.mixer.Sound("..\system\media\windows sound\Windows Permission.wav")
            sound.play()
            del sound
        except Exception as errmsg:
            logging.error(errmsg)
        logging.critical("已啟動最高管理員權限")
        toppest = True
    # ... #

    # upgrade #
    elif code.lower() == "upgrade" and toppest == True and upgradebefore == False:
        logging.info("__init__()...")
        time.sleep(random.randint(2, 5))
        logging.info("finding...")
        time.sleep(random.randint(5, 10))
        logging.info("1.3.5 or 1.3.6")
        upgradecode = str(input(">>>"))
        if upgradecode != str("1.3.5") and upgradecode != str("1.3.6"):
            logging.error("ValueError")
            upgrade = input(">>>")
        else:
            logging.info("upgrading...")
            try:
                for file in os.listdir(r"C:\Windows\System32"):
                    logging.info(file)
                    time.sleep(random.randint(0, 0.5))
                    upgradebefore = True
            except IndexError:
                logging.error("sslerror")
            finally :
                logging.info("finish")
    elif code.lower() == "upgrade" and toppest != True:
        logging.info("Permission denied!")
    elif code.lower() == "upgrade" and upgradebefore == True:
        logging.info("finish upgrade before")
    # ... #

    # member #
    elif code.lower() == "addmember":
        namenumber = input("input name >>>")
        levelcode = input("input grade (1>2>3>4)>>>")
        if levelcode == "1":
            member = dict(zip([namenumber], [level_a]))
        elif levelcode == "2":
            member = dict(zip([namenumber], [level_b]))
        elif levelcode == "3":
            member = dict(zip([namenumber], [level_c]))
        else:
            logging.warning("IndexError")
        OrderedDict(sorted(member.items()))
    # ... #

    # print member #
    elif code.lower() == "printmember":
        logging.info(member)
    # ... #

    # shutdown #
    elif code.lower() == "goodbye":
        if close_mb("quit?") == True:
            try:
                sound = pygame.mixer.Sound("..\system\media\windows sound\Windows Shutdown.wav")
                sound.play()
                del sound
                quit()
            except Exception as errmsg:
                logging.error(errmsg)
        else:
            logging.warning("登出失效")
    # ... #

    # do none #
    elif "" == code:
        pass
    # ... #

    # unknown code #
    else:
        logging.info('"' + code + '" 不是內部或外部命令、可執行的程式或批次檔。')
    # ... #

    # next line #
    print("")
    # ... #

# ... #
