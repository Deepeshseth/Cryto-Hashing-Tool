import enter

import sys
from time import sleep
import random


class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


color_random = [colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
                colors.CRED, colors.CBEIGE]
random.shuffle(color_random)


def entryy():
    x = color_random[0] + """  
             
   ______                 __           __  __           __    _                ______            __
  / ____/______  ______  / /_____     / / / /___ ______/ /_  (_)___  ____ _   /_  __/___  ____  / /
 / /   / ___/ / / / __ \/ __/ __ \   / /_/ / __ `/ ___/ __ \/ / __ \/ __ `/    / / / __ \/ __ \/ / 
/ /___/ /  / /_/ / /_/ / /_/ /_/ /  / __  / /_/ (__  ) / / / / / / / /_/ /    / / / /_/ / /_/ / /  
\____/_/   \__, / .___/\__/\____/  /_/ /_/\__,_/____/_/ /_/_/_/ /_/\__, /    /_/  \____/\____/_/   
          /____/_/                                                /____/                           


\n"""

    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    y = "\t╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱\n\n"
    for c in y:
        print(colors.CBLUE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "\t╱╱                 CYPHER TOOLS                    ╱╱\n\n"
    for c in y:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    z = "\t╱╱               CODED BY Deepesh Seth                  ╱╱\n\n"
    for c in z:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "\t╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱\n\n"
    for c in y:
        print(colors.CBLUE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "\t╱╱              WELCOME TO MY WORLD                ╱╱\n\n"
    for c in y:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    y = "\t╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱\n\n"
    for c in y:
        print(colors.CBLUE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)


entryy()
