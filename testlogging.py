import logging
from colorama import Fore, Style, init

init()
logging.basicConfig(level=logging.DEBUG,format=f"{Fore.GREEN}[time: %(asctime)s] {Fore.LIGHTBLUE_EX}%(levelname)sSYSTEM{Style.RESET_ALL}: %(message)s",
    datefmt="%Y/%D %H:%M:%S")

print("                                           logging system")
logging.debug("   My name is  debugsystem  , I help engineer to fix code (but you can't see me).")
logging.info("    My name is  infosystem   , I will print  info   to user .")
logging.warning(" My name is warmingsystem , I will print warning to user .")
logging.error("   My name is  errorsystem  , I will print  error  to user .")
logging.critical("My name is criticalsystem, if you are toppest, you will see me soon!")