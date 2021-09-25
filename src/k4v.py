from colorama import Fore, Back, Style

import src.k4_groups.k4v_con15 as g15
import src.k4_groups.k4v_con14 as g14
import src.k4_groups.k4v_con13 as g13
import src.k4_groups.k4v_con12 as g12

### Las iteraciones son tan grandes que tenemos que separarlos en grupos
## Para 11
#import src.k4_groups.k4v_con11 as g11
## Para 10
#import src.k4_groups.k4v_con10 as g10
## Para 9
# import src.k4_groups.k4v_con9 as g9
## Para 8
#import src.k4_groups.k4v_con8 as g8
## Para 7
# Lo completado hasta ahora
import src.k4_groups.k4v_con7 as g7
## Para 6
#import src.k4_groups.k4v_con6 as g6
## Para 5
#import src.k4_groups.k4v_con5 as g5

import src.k4_groups.k4v_con4 as g4
import src.k4_groups.k4v_con3 as g3
import src.k4_groups.k4v_con2 as g2
import src.k4_groups.k4v_con1 as g1


def tabla4(listing):

    print("\nEsta version funciona completa para los grupos de 1-3 y 14-16")
    print("Para los demas grupos solo evalua los casos minimos")

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
        while var != 0 and var != 1:
            print(Fore.RESET + "Variables para " + Fore.RED + "[ ", (i + 1) ," ]" + Fore.RESET);
            var = int(input())
        listing.append(var)
        var = " "

    return listing

def k4v(listing):
    count = sum(map(lambda x: x == 1, listing))
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

    print(Fore.YELLOW + "\t\tMAPA DE KARNAUGH\n")
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

    print(Fore.CYAN + "\t\tTABLA DE REFERENCIA\n")
    print(Fore.LIGHTCYAN_EX + "  PQ \ RS      00      01      11      10")
    print("          |---------------------------------")
    print("    00    |  [1]  |  [2]  |  [3]   |  [4]  |")
    print("          |---------------------------------")
    print("    01    |  [5]  |  [6]  |  [7]   |  [8]  |")
    print("          |---------------------------------")
    print("    11    |  [9]  |  [10] |  [11]  |  [12] |")
    print("          |---------------------------------")
    print("    10    |  [13] |  [14] |  [15]  |  [16] |")

    print("\n" + Fore.WHITE)

# ----------------------------------------------------------------------
# Para todos ceros 
# ----------------------------------------------------------------------
    if count == 0:
        print("No hay grupos")
        print("Funcion simplificada, f(P, Q, R, S) = 0")

# ----------------------------------------------------------------------
# Para todos unos
# ----------------------------------------------------------------------
    elif count == 16:
        print("Grupo de 16 = { [1], [2], [3], [4], [5], [6], [7], [8], ",
                "\n[9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = 1")

# ----------------------------------------------------------------------
# Para grupos de 15 unos
# ----------------------------------------------------------------------
    elif count == 15:
        g15.k4v15(listing)

# TODO Arnol
# ----------------------------------------------------------------------
# Para grupos de 14 unos
# ----------------------------------------------------------------------
    elif count == 14:
        g14.k4v14(listing)

# ----------------------------------------------------------------------
# Para grupos de 13 unos
# ----------------------------------------------------------------------
    elif count == 13:
        g13.k4v13(listing)

# ----------------------------------------------------------------------
# Para grupos de 12 unos
# ----------------------------------------------------------------------
    elif count == 12:
        g12.k4v12(listing)

# TODO Danny 
# ----------------------------------------------------------------------
# Para grupos de 11 unos
# ----------------------------------------------------------------------
    #elif count == 11:
    #    g11.k4v11(listing)

# ----------------------------------------------------------------------
# Para grupos de 10 unos
# ----------------------------------------------------------------------
    #elif count == 10:
    #    g10.k4v10(listing)

# ----------------------------------------------------------------------
# Para grupos de 9 unos
# ----------------------------------------------------------------------
    #elif count == 9:
    #    g9.k4v9(listing)

# TODO Jack
# ----------------------------------------------------------------------
# Para grupos de 8 unos
# ----------------------------------------------------------------------
    #elif count == 8:
    #    g8.k4v8(listing)

# ----------------------------------------------------------------------
# Para grupos de 7 unos
# ----------------------------------------------------------------------
    elif count == 7:
        g7.k4v7(listing)

# TODO Nack
# ----------------------------------------------------------------------
# Para grupos de 6 unos
# ----------------------------------------------------------------------
    #elif count == 6:
    #    g6.k4v6(listing)

# ----------------------------------------------------------------------
# Para grupos de 5 unos
# ----------------------------------------------------------------------
    #elif count == 5:
    #    g5.k4v5(listing)

# ----------------------------------------------------------------------
# Para grupos de 4 unos
# ----------------------------------------------------------------------
    elif count == 4:
        g4.k4v4(listing)


# ----------------------------------------------------------------------
# Para grupos de 3 unos
# ----------------------------------------------------------------------
    elif count == 3:
        g3.k4v3(listing)
   
# ----------------------------------------------------------------------
# Para grupos de 2 unos
# ----------------------------------------------------------------------
    elif count == 2:
        g2.k4v2(listing)

# ----------------------------------------------------------------------
# Para grupos de 1 unos
# ----------------------------------------------------------------------
    elif count == 1:
        g1.k4v1(listing)

print("\n\n")
