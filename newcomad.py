import logging
import os
import random
import time
from collections import OrderedDict
from tkinter import messagebox

from place import BuildingBase

logging.basicConfig(
    level=logging.DEBUG,
    format="time:%(asctime)s %(levelname)sSYSTEM: %(message)s",
    datefmt="%Y/%D %H:%M:%S",
)

class Lobby(BuildingBase):

    def __init__(self):

        self._in = True
        self.place = Lobby

    def getin():
        logging.info("wellcome comad(統整性cmd)!")

class Room (BuildingBase) :

    def __init__(self) :

        self.place = Room
        self.user_name = None

    def password (self) :
        times = 4
        locktime = 10

        while True:
            inpd = input("請輸入password:")
            pd = "01928374655647382910"
            if inpd != pd:
                times = times - 1

                if times == 0:
                    logging.error("已鎖定,請" + str(locktime) + "後重新登入")

                    for i in range(locktime, 0, -1):
                        logging.info(i)
                        time.sleep(1)
                    locktime += 20
                    times = 3

                errormessage = str(times) + "次後鎖定"
                logging.warning(errormessage)

            if inpd == pd:
                print("Microsoft Windows [版本 10.0.17134.590]")
                print("(c) 2018 Microsoft Corporation. 著作權所有，並保留一切權利。")
                logging.debug("shouldbe out of range")
                self._in = True

            if pd == "exit":
                self._in = False

    def do(self) :
        upgradecode = 0
        upgradebefore = False
        toppest = False
        cmdpath = str(os.getcwd())
        levela = "Top administrator"
        levelb = "administrator"
        levelc = "VIP member"
        leveld = "member"
        levelcode = 0
        member = {"howard", "the highest administrator"}
        while True:
            code = str(input(cmdpath + ">"))

            ### signout ###
            if "signout" == code.lower():

                logging.info('logout success')

            ### help ###
            elif code.lower()=="help" or code == "?":

                logging.info("1)       signout")
                logging.info("2)    password()")
                logging.info("3)       toppest")
                logging.info("4)       upgrade")
                logging.info("5)     addmember")
                logging.info("6)cleanallmember")

            ### printpd ###
            elif  code.lower()=="password()":
                logging.info("0192837465")


            ### toppest ###
            elif  code.lower()=="toppest":
                logging.critical("已啟動最高管理員權限")
                toppest = True

            ### upgrade ###

            elif  code.lower()=="upgrade" and toppest == True and upgradebefore == False:

                logging.info("__init__()...")
                time.sleep(random.randint(2, 5))
                logging.info("finding...")
                time.sleep(random.randint(5, 10))
                logging.info("1.3.5 or 1.3.6")
                upgradecode = str(input(">>>"))
                if upgradecode != str("1.3.5") and upgradecode != str("1.3.6"):
                    logging.warning("ValueError")
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
                        logging.info("finish")
            elif code.lower() == "upgrade" and toppest != True:
                logging.info("Permission denied!")
            elif code.lower() == "upgrade" and upgradebefore == True:
                logging.info("finish upgrade before")

            ### addmember ###

            elif  code.lower() == "addmember" :

                namenumber = input("input name >>>")
                levelcode = input("input grade (1>2>3>4)>>>")
                if levelcode == "1":
                    member = dict(zip([namenumber], [levela]))
                elif levelcode == "2":
                    member = dict(zip([namenumber], [levelb]))
                elif levelcode == "3":
                    member = dict(zip([namenumber], [levelc]))
                else:
                    logging.warning("error")
                OrderedDict(sorted(member.items()))

            ### printmember ###
            elif code.lower()=="printmember":
                logging.info(member)

            ### space ###
            elif "" == code:
                pass

            ### None ###
            else:
                logging.info("'" + code + "'不是內部或外部命令、可執行的程式或批次檔。")

class Controlroom(BuildingBase):

    def __init__(self):
        self.place = "controlroom"
        self.keypath = r"system\ssl.txt"
        self.key = str(bin(0x219238557398363493676721635178235482736451287365417567235421037))
        del self.user_name

    def sslcheck(self):
        try :
            with open(self.keypath, 'r') as sslpd :
                ssl = sslpd.read()

                if ssl == self.key :

                    logging.critical("gate opening")
                    self._in = True

                else :
                    logging.warning("you shouldn't be here !")

        except Exception as error:
            logging.error(error)

user_lobby = Lobby()
user_room = Room()
user_controlroom = Controlroom()

user_lobby.getin()

