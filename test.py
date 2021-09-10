from colorama import Fore, Back, Style
import numpy as np

def tabla4(listing):
    print(Fore.RED + " P  Q  R  S")
    print("------------|")
    print(Fore.RESET +" 0  0  0  1 " + Fore.RED + "| [1]")
    print(Fore.RESET +" 0  0  0  0 " + Fore.RED + "| [2]")
    print(Fore.RESET +" 0  0  1  1 " + Fore.RED + "| [3]")
    print(Fore.RESET +" 0  0  1  0 " + Fore.RED + "| [4]")
    print(Fore.RESET +" 0  1  0  1 " + Fore.RED + "| [5]")
    print(Fore.RESET +" 0  1  0  0 " + Fore.RED + "| [6]")
    print(Fore.RESET +" 0  1  1  1 " + Fore.RED + "| [7]")
    print(Fore.RESET +" 1  1  1  0 " + Fore.RED + "| [8]")
    print(Fore.RESET +" 1  0  0  1 " + Fore.RED + "| [9]")
    print(Fore.RESET +" 1  0  0  0 " + Fore.RED + "| [10]")
    print(Fore.RESET +" 1  0  1  1 " + Fore.RED + "| [11]")
    print(Fore.RESET +" 1  0  1  0 " + Fore.RED + "| [12]")
    print(Fore.RESET +" 1  1  0  1 " + Fore.RED + "| [13]")
    print(Fore.RESET +" 1  1  0  0 " + Fore.RED + "| [14]")
    print(Fore.RESET +" 1  1  1  1 " + Fore.RED + "| [15]")
    print(Fore.RESET +" 1  1  1  0 " + Fore.RED + "| [16]")

    print("\n")
    posib = 16 
    var = " "

    for i in range (0, posib):
        print(Fore.RESET + "Variables para " + Fore.RED + "[ ", i ," ]" + Fore.RESET);
        listing.append(int(input(var)))

    return listing

def k4v(listing):
    posib = 16
    var = " "
    line1 = ()
    line2 = ()
    line3 = ()
    line4 = ()

    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    print("\n")

    print(Fore.LIGHTYELLOW_EX + "  PQ \ RS      00      01      11      10")
    print("          |-------------------------------")
    print("    00    |  ", listing[0] ,"  |  ",listing[1],"  |  ",listing[3],"  |  ",listing[2]," |")
    print("          |-------------------------------")
    print("    01    |  ", listing[4] ,"  |  ",listing[5],"  |  ",listing[7],"  |  ",listing[6]," |")
    print("          |-------------------------------")
    print("    11    |  ", listing[12] ,"  |  ",listing[13],"  |  ",listing[15],"  |  ",listing[14]," |")
    print("          |-------------------------------")
    print("    10    |  ", listing[8] ,"  |  ",listing[9],"  |  ",listing[11],"  |  ",listing[10]," |")

    print("\n")

    print(Fore.LIGHTBLUE_EX + "  PQ \ RS      00      01      11      10")
    print("          |---------------------------------")
    print("    00    |  [1]  |  [2]  |  [3]   |  [4]  |")
    print("          |---------------------------------")
    print("    01    |  [5]  |  [6]  |  [7]   |  [8]  |")
    print("          |---------------------------------")
    print("    11    |  [9]  |  [10] |  [11]  |  [12] |")
    print("          |---------------------------------")
    print("    10    |  [13] |  [14] |  [15]  |  [16] |")

    print("\n" + Fore.WHITE)

    
