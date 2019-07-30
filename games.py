print("wellcome to color-race-game!!!")
print("start init( ) ...")
color_to_word = {"green" : "{Fore.GREEN}",
                "red" : "{Fore.RED}",
                "blue" : "{Fore.BLUE}",
                "black" : "{Fore.BLACK}",
                "yellow" : "{Fore.YELLOW}",
                "white" : "{Fore.WHITE}"}
point = 0
from colorama import init, Fore, Style
import time
import random
init()
print("finish init( )!!!")
#round = int(input("input round >>>"))
print(r"start !!!\n")
for i in range(1, 2) :
    print("       round ", i)
    print("start in ...")
    # wait() #

    for k in range(3, 0, -1) :
        print(k, end = " ")
        time.sleep(1)
    print("")

    # ... #
    random_color = random.choice(list(color_to_word.keys())).upper()
    print("{Fore.thecolor} which color is this ?" .format(thecolor = random_color))
    if input(" >>>") == random_color :
        point += 1
        print("you're right !!!")
    else :
        print("wrong ...")
    Style.RESET_ALL()