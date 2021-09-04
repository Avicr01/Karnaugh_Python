from src.k2v import k2v, tabla2
# from src.k3v import k3v, tabla3
from src.k4v import k4v, tabla4
import os
import time
import sys
from colorama import Fore, Back, Style

# Works for Unix 
clear = lambda: os.system('clear')
# Works for Windows 
# clear = lambda: os.system("cls")

def Eleccion_variables():
    print(Fore.YELLOW + "SECCION DE NUMERO DE VARIABLES")
    print(Fore.RED + "  [ 2 ] " + Fore.RESET + "Dos variables")
    print(Fore.RED + "  [ 3 ] " + Fore.RESET + "Tres variables")
    print(Fore.RED + "  [ 4 ] " + Fore.RESET + "Cuatro variables")

    option = 0
    while option != 2 and option != 3 and option != 4:
        option = int(input("Elija el numero de variables que requiera: "))
        print(option)

    listing = [ ] 

    if option == 2:
        tabla2(listing)
        k2v(listing)
    elif option == 3:
        print("hello")
        # tabla3(listing)
        # k3v(listing)
    elif option == 4:
        tabla4(listing)
        k4v(listing)
    

while True: 
    print(Fore.YELLOW + "MENU DE OPCIONES - MAPA DE KARNAUGH")
    print(Fore.RESET + "Seleccione la opcion que quiere realizar: ")
    print(Fore.RED + "  1. " + Fore.RESET + "Elegir numero de variables")
    print(Fore.RED + "  2. " + Fore.RESET + "Salir")

    option = 0
    while option != 1 and option != 2:
        option = int(input('Elija su opcion: '))
        print(option)
    
    time.sleep(1)
    clear()

    if option == 1:
        Eleccion_variables()
        sys.exit()
    elif option == 2:
        # Salir
        sys.exit()
