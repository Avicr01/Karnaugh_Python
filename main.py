from src.k2v import k2v, tabla2
from src.k3v import k3v, tabla3
from src.k4v import k4v, tabla4

import os
import time
import sys
from colorama import Fore, Back, Style

# Works for Unix 
#clear = lambda: os.system('clear')
# Works for Windows 
def clear():
    # Para Windows es "nt"
    return os.system("cls" if os.name == "nt" else "clear")

def Eleccion_variables():
    print(Fore.YELLOW + "SECCION DE NUMERO DE VARIABLES")
    print(Fore.RED + "  [ 2 ] " + Fore.RESET + "Dos variables")
    print(Fore.RED + "  [ 3 ] " + Fore.RESET + "Tres variables")
    print(Fore.RED + "  [ 4 ] " + Fore.RESET + "Cuatro variables")

    option = 0
    while option != 2 and option != 3 and option != 4:
        option = int(input("Elija el numero de variables que requiera: "))
        print(option)

    listing = [] 

    if option == 2:
        tabla2(listing)
        k2v(listing)
    elif option == 3:
        tabla3(listing)
        k3v(listing)
    elif option == 4:
        tabla4(listing)
        k4v(listing)

def Title():
    print(Fore.RED + """
        ___  ___                            _        _   __                                   _     
        |  \/  |                           | |      | | / /                                  | |    
        | .  . | __ _ _ __   __ _ ___    __| | ___  | |/ /  __ _ _ __ _ __   __ _ _   _  __ _| |__  
        | |\/| |/ _` | '_ \ / _` / __|  / _` |/ _ \ |    \ / _` | '__| '_ \ / _` | | | |/ _` | '_ \ 
        | |  | | (_| | |_) | (_| \__ \ | (_| |  __/ | |\  \ (_| | |  | | | | (_| | |_| | (_| | | | |
        \_|  |_/\__,_| .__/ \__,_|___/  \__,_|\___| \_| \_/\__,_|_|  |_| |_|\__,_|\__,_|\__, |_| |_|
                     | |                                                                 __/ |      
                     |_|                                                                |___/
    """)
    time.sleep(0.8)
    clear();
    print(Fore.BLUE + """
        ___  ___                            _        _   __                                   _     
        |  \/  |                           | |      | | / /                                  | |    
        | .  . | __ _ _ __   __ _ ___    __| | ___  | |/ /  __ _ _ __ _ __   __ _ _   _  __ _| |__  
        | |\/| |/ _` | '_ \ / _` / __|  / _` |/ _ \ |    \ / _` | '__| '_ \ / _` | | | |/ _` | '_ \ 
        | |  | | (_| | |_) | (_| \__ \ | (_| |  __/ | |\  \ (_| | |  | | | | (_| | |_| | (_| | | | |
        \_|  |_/\__,_| .__/ \__,_|___/  \__,_|\___| \_| \_/\__,_|_|  |_| |_|\__,_|\__,_|\__, |_| |_|
                     | |                                                                 __/ |      
                     |_|                                                                |___/
    """)
    time.sleep(0.8)
    clear();
    print(Fore.YELLOW + """
        ___  ___                            _        _   __                                   _     
        |  \/  |                           | |      | | / /                                  | |    
        | .  . | __ _ _ __   __ _ ___    __| | ___  | |/ /  __ _ _ __ _ __   __ _ _   _  __ _| |__  
        | |\/| |/ _` | '_ \ / _` / __|  / _` |/ _ \ |    \ / _` | '__| '_ \ / _` | | | |/ _` | '_ \ 
        | |  | | (_| | |_) | (_| \__ \ | (_| |  __/ | |\  \ (_| | |  | | | | (_| | |_| | (_| | | | |
        \_|  |_/\__,_| .__/ \__,_|___/  \__,_|\___| \_| \_/\__,_|_|  |_| |_|\__,_|\__,_|\__, |_| |_|
                     | |                                                                 __/ |      
                     |_|                                                                |___/
    """ + Fore.RESET)
    time.sleep(0.8)
    clear();
    

if __name__ == "__main__":

    print(Fore.RED + """
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@#K|R@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@#y- x@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@&B@@@@@@@g!   t@@@@@@@@@@@@@@Qg@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@d]D@@@@@@@8,    r@@@@@@@@@@@@@@@d]R@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@Q|!8@@@@@@@@|     `l@@@@@@@@@@@@@@@&: Q@@@@@@@@@@@@ 
              @@@@@@@@@@@5-.D@@@@@@@@g'      `}Q@@@@@@@@@@@@@@b`_d@@@@@@@@@@@ 
              @@@@@@@@@@g` i@@@@@@@@@0`        'vg@@@@@@@@@@@@@v `W@@@@@@@@@@ 
              @@@@@@@@@8_ `R@@@@@@@@@Q,          `B@@@@@@@@@@@N`  `Q@@@@@@@@@ 
              @@@@@@@@@|  `&@@@@@@@@@@y`           ~B@@@@@@@@@@&`  x@@@@@@@@@ 
              @@@@@@@@&'  `b@@@@@@@@@@#x            ]@@@@@@@@@@S`  .Q@@@@@@@@ 
              @@@@@@@@2    }@@@@@@@@@@@@t.          -Q@@@@@@@@@v    K@@@@@@@@ 
              @@@@@@@@c    .E@@@@@@@@@@@@Qi.        `0@@@@@@@@R'    k@@@@@@@@ 
              @@@@@@@@y     !Q@@@@@@@@@@@@@By'      .Q@@@@@@@g"     o@@@@@@@@ 
              @@@@@@@@d`     :0@@@@@@@@@@@@@@E`     v@@@@@@@R_     `E@@@@@@@@ 
              @@@@@@@@#~      `}B@@@@@@@@@@@@@*    !Q@@@@@B7`      *@@@@@@@@@ 
              @@@@@@@@@d'       -1Q@@@@@@@@@@@y   ^B@@@@8}.       `E@@@@@@@@@ 
              @@@@@@@@@@o         `v3Q@@@@@@@@|`:s#@@QH/`         v@@@@@@@@@@ 
              @@@@@@@@@@@l`           `:r7yfHk-/17*:`           `y@@@@@@@@@@@ 
              @@@@@@@@@@@@N"                                   :R@@@@@@@@@@@@ 
              @@@@@@@@@@@@@#l-                               -y#@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@Bk:                           !o#@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@0}!                     =1&@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@&f]^_`         `,^isg@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@#Q&RdddR&Q#@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """ + Fore.RESET)

    time.sleep(1.5)
    clear()

    Title()

    print(Fore.YELLOW + "\nMENU DE OPCIONES - MAPA DE KARNAUGH")
    print(Fore.RESET + "Seleccione la opcion que quiere realizar: ")
    print(Fore.RED + "  1. " + Fore.RESET + "Elegir numero de variables")
    print(Fore.RED + "  2. " + Fore.RESET + "Salir")

    option = 0
    while option != 1 and option != 2:
        option = int(input('Elija su opcion: '))
        print(option)
    
    time.sleep(0.4)
    clear()

    if option == 1:
        Eleccion_variables()
        sys.exit()
    elif option == 2:
        # Salir
        sys.exit()
