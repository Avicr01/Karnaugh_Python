from colorama import Fore, Back, Style

def tabla3(listing):
    print(" P  Q  R ")
    print("----------")
    print(" 0  0  0 | [1]")
    print(" 0  0  1 | [2]")
    print(" 0  1  0 | [3]")
    print(" 0  1  1 | [4]")
    print(" 1  0  0 | [5]")
    print(" 1  0  1 | [6]")
    print(" 1  1  0 | [7]")
    print(" 1  1  1 | [8]")

    posib =  8
    var = " "

    for i in range (0, posib):
        while var != 0 and var != 1:
            print(Fore.RESET + "Variables para " + Fore.RED + "[ ", i ," ]" + Fore.RESET);
            var = int(input())
        listing.append(var)
        var = " "

    return listing
 
 # ES NECESARIO CORREGIR LOS GRUPOS DE 4, 5 y 6!

#Para todos los ceros
def kmaps3 (listing, label):
    line1 = ()
    line2 = ()
    line1 = (listing[0],listing[2],listing[6],listing[4])
    line2 = (listing[1],listing[3],listing[7],listing[5])

    print(Fore.YELLOW + "\tMAPA DE KARNAUGH\n")
    print(Fore.LIGHTYELLOW_EX + "P  \\  QR     00      01      11     10")
    print("         |-------------------------------")
    print("    0    |  ", listing[0] ,"  |  ",listing[2],"  |  ",listing[6],"  |  ",listing[4]," |")
    print("         |-------------------------------")
    print("    1    |  ", listing[1] ,"  |  ",listing[3],"  |  ",listing[7],"  |  ",listing[5]," |")

    print("\n")
  
    print(Fore.BLUE + "\tTABLA DE REFERENCIA\n")
    print(Fore.LIGHTBLUE_EX+ "P  \\  QR     00      01      11     10")
    print("         |-------------------------------")
    print("    0    |  [1]  |  [3]  |  [7]  |  [5]  |")
    print("         |-------------------------------")
    print("    1    |  [2]  |  [4]  |  [8]  |  [6]  |") 

    print("\n" + Fore.WHITE)
    
    # Todos de 0
    if line1 == (0, 0, 0, 0) and line2 == (0, 0, 0, 0):
        label += "No hay grupos\n"
        label += "Funcion simplificada, S( P , Q , R )  = 0\n"

    # Todos de 1
    elif line1 == (1, 1, 1, 1) and line2 == (1, 1, 1, 1):
        label += "Grupo de 8 = [1], [2], [3], [4], [5], [6], [7], [8]\n"
        label += "Funcion simplificada, S( P , Q , R )  = 1\n"

    #Grupos con siete unos [ ]
    elif line1 == (1,1,1,0) and line2 == (1,1,1,1):
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [3],[4],[7],[8]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, f(P, Q, R) = Q' + R + P \n"

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [3],[4],[7],[8]\n"
        label += "Funcion simplificada, f(P , Q, R) = P' + Q' + R \n" 

    elif line1 == (1,1,0,1) and line2 == (1,1,1,1):
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, f(P, Q, R) = Q' + R' + P \n"

    elif line1 == (1,1,1,1) and line2 == (1,1,0,1):
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Funcion simplificada, f(P, Q, R) = P' + Q' + R'\n"

    elif line1 == (1,0,1,1) and line2 == (1,1,1,1):
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Grupo de 4 = [7],[8],[5],[6]\n"
        label += "Funcion simplificada, f(P, Q, R) = R' + Q + P \n"# commit

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [3],[4],[7],[8]\n"
        label += "Funcion simplificada, f(P , Q, R) = P' + Q' + R \n"

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [3],[4],[7],[8]\n"
        label += "Funcion simplificada, f(P , Q, R) = P' + Q' + R \n"

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [3],[4],[7],[8]\n"
        label += "Funcion simplificada, f(P , Q, R) = P' + Q' + R \n"

#Grupos de 6 de 1 (dos ceros)
#Grupos de seis unos (dos ceros)
#GRUPOS DE CEROS
#Grupo de [1] con el resto [ ]
    elif line1 == (0,0,1,1) and line2 == (1,1,1,1): #ceros en [1] y [3]
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q + P\n"

    elif line1 == (0,1,1,1) and line2 == (0,1,1,1): #ceros en [1] y [2]
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = R + Q\n"

    elif line1 == (0,1,1,1) and line2 == (1,0,1,1): #ceros en [1] y [4]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + Q + PR'\n"

    elif line1 == (0,1,1,1) and line2 == (1,1,0,1): #ceros en [1] y [8]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + QR' + PQ'\n"

    elif line1 == (0,1,1,1) and line2 == (1,1,1,0): #ceros en [1] y [6]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = R + P'Q + PQ'\n"

    elif line1 == (0,1,0,1) and line2 == (1,1,1,1): #ceros en [1] y [7]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + QR' + P\n"

    elif line1 == (0,1,1,0) and line2 == (1,1,1,1): #ceros en [1] y [5]
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = R + P\n"

#Grupo de [2] con el resto [ ]
    elif line1 == (1,1,1,1) and line2 == (0,0,1,1): #ceros en [2] y [4]
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + Q\n"

    elif line1 == (1,0,1,1) and line2 == (0,1,1,1): #ceros en [2] y [3]
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + Q + PR\n"

    elif line1 == (1,1,0,1) and line2 == (0,1,1,1): #ceros en [2] y [7]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + QR' + PR\n"

    elif line1 == (1,1,1,0) and line2 == (0,1,1,1): #ceros en [2] y [5]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + R + PQ\n"

    elif line1 == (1,1,1,1) and line2 == (0,1,0,1): #ceros en [2] y [8]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + Q'R + QR'\n"

    elif line1 == (1,1,1,1) and line2 == (0,1,1,0): #ceros en [2] y [6]
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + R\n"

#Grupo de [3] con el resto [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,1,1): #ceros en [3] y [7]
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = R' + P\n"

    elif line1 == (1,0,1,1) and line2 == (1,0,1,1): #ceros en [3] y [4]
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = R' + Q\n"

    elif line1 == (1,0,1,1) and line2 == (1,1,0,1): #ceros en [3] y [8]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 4 = [5],[6],[1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = R' + P'Q + PQ'\n"

    elif line1 == (1,0,1,1) and line2 == (1,1,1,0): #ceros en [3] y [6]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + QR + PQ'\n"

    elif line1 == (1,0,1,0) and line2 == (1,1,1,1): #ceros en [3] y [5]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + QR + P\n"


#Grupo de [4] con el resto [ ]
    elif line1 == (1,1,1,1) and line2 == (1,0,0,1): #ceros en [4] y [8]
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + R'\n"

    elif line1 == (1,1,1,0) and line2 == (1,0,1,1): #ceros en [4] y [5]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + QR + PR'\n"

    elif line1 == (1,1,0,1) and line2 == (1,0,1,1): #ceros en [4] y [7]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Grupo de 4 = [5],[6],[1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + R' + PQ\n"

    elif line1 == (1,1,1,1) and line2 == (1,0,1,0): #ceros en [4] y [6]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + Q'R' + QR\n"

#Grupo de [5] con el resto [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,1,1): #ceros en [5] y [7]
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q' + P\n"

    elif line1 == (1,1,1,0) and line2 == (1,1,0,1): #ceros en [5] y [8]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q' + P'R + PR'\n"

    elif line1 == (1,1,1,0) and line2 == (1,1,1,0): #ceros en [5] y [6]
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = R + Q\n"

#Grupo de [6] con el resto [ ]
    elif line1 == (1,1,0,1) and line2 == (1,1,1,0): #ceros en [6] y [7]
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q' + P'R' + PR\n"

    elif line1 == (1,1,1,1) and line2 == (1,1,0,0): #ceros en [6] y [8]
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + Q'\n"

#Grupo de [7] con el resto [ ]
    elif line1 == (1,1,0,1) and line2 == (1,1,0,1): #ceros en [7] y [8]
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Grupo de 4 = [1],[2],[5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q' + R'\n"

#No hay grupos de [8] porque ya se asoció con todos

#GRUPOS DE CINCO UNOS (tres ceros)
#Grupos de [1] [ ] [ ]
#Grupos de [1] [2] [ ]
    elif line1 == (0,0,1,1) and line2 == (0,1,1,1): #ceros en [1] , [2] y [3]
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q + PR\n"

    elif line1 == (0,1,1,1) and line2 == (0,0,1,1): #ceros en [1] , [2] y [4]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + Q\n"

    elif line1 == (0,1,1,0) and line2 == (0,1,1,1): #ceros en [1] , [2] y [5]
        label += "Grupo de 2 = [8],[6]\n"
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = R + PQ\n"

    elif line1 == (0,1,1,1) and line2 == (0,1,1,0): #ceros en [1] , [2] y [6]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = R + P'Q\n"

    elif line1 == (0,1,0,1) and line2 == (0,1,1,1): #ceros en [1] , [2] y [7]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + QR' + PR\n"

    elif line1 == (0,1,1,1) and line2 == (0,1,0,1): #ceros en [1] , [2] y [8]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + QR' + P'R\n"

#Grupos de [1] [3] [ ]
    elif line1 == (0,0,1,1) and line2 == (1,0,1,1): #ceros en [1] , [3] y [4]
        label += "Grupo de 2 = [6],[2]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q + PR'\n"

    elif line1 == (0,0,1,0) and line2 == (1,1,1,1): #ceros en [1] , [3] y [5]
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR + P\n"

    elif line1 == (0,0,1,1) and line2 == (1,1,1,0): #ceros en [1] , [3] y [6]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PQ' + QR\n"

    elif line1 == (0,0,0,1) and line2 == (1,1,1,1): #ceros en [1] , [3] y [7]
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR' + P\n"

    elif line1 == (0,0,1,1) and line2 == (1,1,0,1): #ceros en [1] , [3] y [8]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PQ' + QR'\n"

#Grupos de [1] [4] [ ]
    elif line1 == (0,1,1,0) and line2 == (1,0,1,1): #ceros en [1] , [4] y [5]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PR' + QR\n"

    elif line1 == (0,1,1,1) and line2 == (1,0,1,0): #ceros en [1] , [4] y [6]
        label += "Grupo de 1 = [2]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + P'Q + PQ'R' + QR\n"

    elif line1 == (0,1,0,1) and line2 == (1,0,1,1): #ceros en [1] , [4] y [7]
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R + QR' + PR' + PQ\n"

    elif line1 == (0,1,1,1) and line2 == (1,0,0,1): #ceros en [1] , [4] y [8] 
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PR' + P'Q\n"

#Grupos de [1] [5] [ ]
    elif line1 == (0,1,1,0) and line2 == (1,1,1,0): #ceros en [1] , [5] y [6]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = R + PQ'\n"

    elif line1 == (0,1,0,0) and line2 == (1,1,1,1): #ceros en [1] , [5] y [7]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + P\n"

    elif line1 == (0,1,1,0) and line2 == (1,1,0,1): #ceros en [1] , [5] y [8] 
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PR' + Q'R\n"

#Grupos de [1] [6] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,1,1,0): #ceros en [1] , [6] y [7]
        label += "Grupo de 1 = [5]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + P'QR' + PQ' + PR\n"

    elif line1 == (0,1,1,1) and line2 == (1,1,0,0): #ceros en [1] , [6] y [8]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [2],[3]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PQ' + P'R\n"

#Grupos de [1] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,1,0,1): #ceros en [1] , [7] y [8]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + QR' + PQ'\n"
#No hay grupos de [1] [8] [ ] porque ya está incluido

#Grupos de [2] [ ] [ ]
#Grupos de [2] [3] [ ]
    elif line1 == (1,0,1,1) and line2 == (0,0,1,1): #ceros en [2] , [3] y [4]
        label += "Grupo de 2 = [5],[1]\n"
        label += "Grupo de 4 = [7],[5],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + Q\n"

    elif line1 == (1,0,1,0) and line2 == (0,1,1,1): #ceros en [2] , [3] y [5]
        label += "Grupo de 1 = [1]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R' + QR + PR + PQ\n"

    elif line1 == (1,0,1,1) and line2 == (0,1,1,0): #ceros en [2] , [3] y [6]
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PR + P'Q\n"

    elif line1 == (1,0,0,1) and line2 == (0,1,1,1): #ceros en [2] , [3] y [7]
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PR + QR'\n"

    elif line1 == (1,0,1,1) and line2 == (0,1,0,1): #ceros en [2] , [3] y [8]
        label += "Grupo de 1 = [4]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + P'Q + PQ'R + QR'\n"

#Grupos de [2] [4] [ ]
    elif line1 == (1,1,1,0) and line2 == (0,0,1,1): #ceros en [2] , [4] y [5]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + PQ + P'R\n"

    elif line1 == (1,0,0,1) and line2 == (0,1,1,1): #ceros en [2] , [4] y [6]
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + QR\n"

    elif line1 == (1,1,0,1) and line2 == (0,0,1,1): #ceros en [2] , [4] y [7]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + PQ + P'R'\n"

    elif line1 == (1,1,1,1) and line2 == (0,0,0,1): #ceros en [2] , [4] y [8]
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + QR'\n"

#Grupos de [2] [5] [ ]
    elif line1 == (1,1,1,0) and line2 == (0,1,1,0): #ceros en [2] , [5] y [6]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 4 = [3],[7],[4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + R\n"

    elif line1 == (1,1,0,0) and line2 == (0,1,1,1): #ceros en [2] , [5] y [7]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + PQ + Q'R\n"

    elif line1 == (1,1,1,0) and line2 == (0,1,0,1): #ceros en [2] , [5] y [8]
        label += "Grupo de 1 = [6]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + P'R + Q'R + PQR'\n"

#Grupos de [2] [6] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,1,1,0): #ceros en [2] , [6] y [7]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PR + P'Q'\n"

    elif line1 == (1,1,1,1) and line2 == (0,1,0,0): #ceros en [2] , [6] y [8]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 4 = [1],[3],[7],[5]\n"        
        label += "Funcion simplificada, S(P, Q, R) = P' + Q'R\n"

#Grupos de [2] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,1,0,1): #ceros en [2] , [7] y [8]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + QR' + P'Q'\n"
#No hay grupos de [2] [8] [ ] porque ya está incluido 

#Grupos de [3] [ ] [ ]
#Grupos de [3] [4] [ ]
    elif line1 == (1,0,1,0) and line2 == (1,0,1,1): #ceros en [3] , [4] y [5]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + QR + PR'\n"

    elif line1 == (1,0,1,1) and line2 == (1,0,1,0): #ceros en [3] , [4] y [6]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + QR + P'R'\n"

    elif line1 == (1,0,0,1) and line2 == (1,0,1,1): #ceros en [3] , [4] y [7]
        label += "Grupo de 2 = [8],[6]\n"
        label += "Grupo de 4 = [5],[6],[1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = R' + PQ\n"

    elif line1 == (1,0,1,1) and line2 == (1,0,0,1): #ceros en [3] , [4] y [8]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 4 = [5],[6],[1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = R' + P'Q\n"

#Grupos de [3] [5] [ ]
    elif line1 == (1,0,1,0) and line2 == (1,1,1,0): #ceros en [3] , [5] y [6]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + QR + PQ'\n"

    elif line1 == (1,0,0,0) and line2 == (1,1,1,1): #ceros en [3] , [5] y [7]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + P\n"

    elif line1 == (1,0,1,0) and line2 == (1,1,0,1): #ceros en [3] , [5] y [8]
        label += "Grupo de 1 = [7]\n"
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + P'QR + PQ' + PR'\n"

#Grupos de [3] [6] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,1,0): #ceros en [3] , [6] y [7]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PR + Q'R'\n"

    elif line1 == (1,0,1,1) and line2 == (1,1,0,0): #ceros en [3] , [6] y [8]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PQ' + P'R'\n"

#Grupos de [3] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,0,1): #ceros en [3] , [7] y [8]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 4 = [5],[6],[1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = R' + PQ'\n"
#No hay grupos de [3] [8] [ ] porque ya está incluido 

#Grupos de [4] [ ] [ ]
#Grupos de [4] [5] [ ]
    elif line1 == (1,1,1,0) and line2 == (1,0,1,0): #ceros en [4] , [5] y [6]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + QR + P'Q'\n"

    elif line1 == (1,1,0,0) and line2 == (1,0,1,1): #ceros en [4] , [5] y [7]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + PQ + Q'R'\n"

    elif line1 == (1,1,1,0) and line2 == (1,0,0,1): #ceros en [4] , [5] y [8]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PR' + P'Q'\n"

#Grupos de [4] [6] [ ]
    elif line1 == (1,1,0,1) and line2 == (1,0,1,0): #ceros en [4] , [6] y [7]
        label += "Grupo de 1 = [8]\n"
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + P'R' + Q'R' + PQR\n"

    elif line1 == (1,1,1,1) and line2 == (1,0,0,0): #ceros en [4] , [6] y [8]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + Q'R'\n"

#Grupos de [4] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (1,0,0,1): #ceros en [4] , [7] y [8]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 4 = [5],[6],[1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + R'\n"
#No hay grupos de [4] [8] [ ] porque ya está incluido

#Grupos de [5] [ ] [ ]
#Grupos de [5] [6] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,1,0): #ceros en [5] , [6] y [7]
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q' + PR\n"

    elif line1 == (1,1,1,0) and line2 == (1,1,0,0): #ceros en [5] , [6] y [8]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q' + P'R\n"

#Grupos de [5] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,0,1): #ceros en [5] , [7] y [8]
        label += "Grupo de 2 = [6],[2]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q' + PR'\n"
#No hay grupos de [5] [8] [ ] porque ya está incluido 

#Grupos de [6] [ ] [ ]
#Grupos de [6] [7] [ ]
    elif line1 == (1,0,1,1) and line2 == (1,0,0,1): #ceros en [6] , [7] y [8]
        label += "Grupo de 2 = [1],[5]\n"
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = R' + P'Q\n"
#No hay grupos de [7] [ ] [ ] ni [8] [ ] [ ] porque ya está incluido en los anteriores


#GRUPOS DE CUATRO UNOS (cuatro ceros)
#Grupos de [1] [ ] [ ] [ ]
#Grupos de [1] [2] [ ] [ ]
#Grupos de [1] [2] [3] [ ]
    elif line1 == (0,0,1,1) and line2 == (0,0,1,1): #ceros en [1] , [2] , [3] , [4]
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q\n"

    elif line1 == (0,0,1,0) and line2 == (0,1,1,1): #ceros en [1] , [2] , [3] , [5]
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR + PR + PQ\n"

    elif line1 == (0,0,1,1) and line2 == (0,1,1,0): #ceros en [1] , [2] , [3] , [6]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PR\n"

    elif line1 == (0,0,0,1) and line2 == (0,1,1,1): #ceros en [1] , [2] , [3] , [7]
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PR\n"

    elif line1 == (0,0,1,1) and line2 == (0,1,1,0): #ceros en [1] , [2] , [3] , [8]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR' + PR\n"

#Grupos de [1] [2] [4] [ ]
    elif line1 == (0,1,1,0) and line2 == (0,0,1,1): #ceros en [1] , [2] , [4] , [5]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PQ\n"

    elif line1 == (0,1,1,1) and line2 == (0,0,1,0): #ceros en [1] , [2] , [4] , [6]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + P'Q + QR\n"

    elif line1 == (0,1,0,1) and line2 == (0,0,1,1): #ceros en [1] , [2] , [4] , [7]
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R + QR' + PQ\n"

    elif line1 == (0,1,1,1) and line2 == (0,0,0,1): #ceros en [1] , [2] , [4] , [8]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + QR'\n"

#Grupos de [1] [2] [5] [ ]
    elif line1 == (0,1,1,0) and line2 == (0,1,1,0): #ceros en [1] , [2] , [5] , [6]
        label += "Grupo de 4 = [3],[4],[7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = R\n"
        
    elif line1 == (0,1,0,0) and line2 == (0,1,1,1): #ceros en [1] , [2] , [5] , [7]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + PQ\n"

    elif line1 == (0,1,1,0) and line2 == (0,1,0,1): #ceros en [1] , [2] , [5] , [8]
        label += "Grupo de 1 = [6]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + Q'R + PQR'\n"

#Grupos de [1] [2] [6] [ ]
    elif line1 == (0,1,0,1) and line2 == (0,1,1,0): #ceros en [1] , [2] , [6] , [7]
        label += "Grupo de 1 = [5]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + P'QR' + PR\n"

    elif line1 == (0,1,1,1) and line2 == (0,1,0,0): #ceros en [1] , [2] , [6] , [8]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + Q'R\n"

#Grupos de [1] [2] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (0,1,0,1): #ceros en [1] , [2] , [7] , [8]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + QR'\n"
#Grupos de [1] [2] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [3] [ ] [ ]
#Grupos de [1] [3] [4] [ ]
    elif line1 == (0,0,1,0) and line2 == (1,0,1,1): #ceros en [1] , [3] , [4] , [5]
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR + PR'\n"

    elif line1 == (0,0,1,1) and line2 == (1,0,1,0): #ceros en [1] , [3] , [4] , [6]
        label += "Grupo de 1 = [2]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PQ'R' + QR\n"

    elif line1 == (0,0,0,1) and line2 == (1,0,1,1): #ceros en [1] , [3] , [4] , [7]
        label += "Grupo de 2 = [8],[6]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR' + PR' + PQ\n"

    elif line1 == (0,0,1,1) and line2 == (1,0,0,1): #ceros en [1] , [3] , [4] , [8]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PR'\n"

#Grupos de [1] [3] [5] [ ]
    elif line1 == (0,0,1,0) and line2 == (1,1,1,0): #ceros en [1] , [3] , [5] , [6]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR + PQ'\n"

    elif line1 == (0,0,0,0) and line2 == (1,1,1,1): #ceros en [1] , [3] , [5] , [7]
        label += "Grupo de 4 = [2],[4],[8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P\n"

    elif line1 == (0,0,1,0) and line2 == (1,1,0,1): #ceros en [1] , [3] , [5] , [8]
        label += "Grupo de 1 = [7]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'QR + PQ' + PR'\n"

#Grupos de [1] [3] [6] [ ]
    elif line1 == (0,0,0,1) and line2 == (1,1,1,0): #ceros en [1] , [3] , [6] , [7]
        label += "Grupo de 1 = [5]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'QR' + PQ' + PR\n"

    elif line1 == (0,0,1,1) and line2 == (1,1,0,0): #ceros en [1] , [3] , [6] , [8]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + PQ'\n"

#Grupos de [1] [3] [7] [ ]
    elif line1 == (0,0,0,1) and line2 == (1,1,0,1): #ceros en [1] , [3] , [7] , [8]
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR' + PQ'\n"
#Grupos de [1] [3] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [4] [ ] [ ]
#Grupos de [1] [4] [5] [ ]
    elif line1 == (0,1,1,0) and line2 == (1,0,1,0): #ceros en [1] , [4] , [5] , [6]
        label += "Grupo de 1 = [2]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PQ'R' + QR\n"

    elif line1 == (0,1,0,0) and line2 == (1,0,1,1): #ceros en [1] , [4] , [5] , [7]
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R + PR' + PQ\n"

    elif line1 == (0,1,1,0) and line2 == (1,0,0,1): #ceros en [1] , [4] , [5] , [8]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PR'\n"

#Grupos de [1] [4] [6] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,0,1,0): #ceros en [1] , [4] , [6] , [7] #DUDAA
        label += "Grupo de 1 = [2]\n"
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 1 = [8]\n"
        label += "Grupo de 1 = [5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R + P'QR' + PQ'R' + PQR\n"

    elif line1 == (0,1,1,1) and line2 == (1,0,0,0): #ceros en [1] , [4] , [6] , [8]
        label += "Grupo de 1 = [2]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + P'Q + PQ'R'\n"

#Grupos de [1] [4] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,0,0,1): #ceros en [1] , [4] , [7] , [8]
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R + QR' + PR'\n"
#Grupos de [1] [4] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [5] [ ] [ ]
#Grupos de [1] [5] [6] [ ]
    elif line1 == (0,1,0,0) and line2 == (1,1,1,0): #ceros en [1] , [5] , [6] , [7]
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + PQ' + PR\n"

    elif line1 == (0,1,1,0) and line2 == (1,1,0,0): #ceros en [1] , [5] , [6] , [8]
        label += "Grupo de 2 = [3],[7]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + PQ'\n"

#Grupos de [1] [5] [7] [ ]
    elif line1 == (0,1,0,0) and line2 == (1,1,0,1): #ceros en [1] , [5] , [7] , [8]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + PR'\n"
#Grupos de [1] [5] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [6] [ ] [ ]
#Grupos de [1] [6] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,1,0,0): #ceros en [1] , [6] , [7] , [8]
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R + P'QR' + PQ'\n"
#Grupos de [1] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [2] [ ] [ ] [ ]
#Grupos de [2] [3] [4] [ ]
    elif line1 == (1,0,1,0) and line2 == (0,0,1,1): #ceros en [2] , [3] , [4] , [5]
        label += "Grupo de 1 = [1]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R' + QR + PQ\n"

    elif line1 == (1,0,1,1) and line2 == (0,0,1,0): #ceros en [2] , [3] , [4] , [6]
        label += "Grupo de 2 = [7],[8]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + QR\n"

    elif line1 == (1,0,0,1) and line2 == (0,0,1,1): #ceros en [2] , [3] , [4] , [7]
        label += "Grupo de 2 = [5],[1]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PQ\n"

    elif line1 == (1,0,1,1) and line2 == (0,0,0,1): #ceros en [2] , [3] , [4] , [8]
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + P'Q + QR'\n"

#Grupos de [2] [3] [5] [ ]
    elif line1 == (1,0,1,0) and line2 == (0,1,1,0): #ceros en [2] , [3] , [5] , [6]
        label += "Grupo de 1 = [1]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R' + QR + PR\n"

    elif line1 == (1,0,0,0) and line2 == (0,1,1,1): #ceros en [2] , [3] , [5] , [7]
        label += "Grupo de 1 = [1]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R' + PR + PQ\n"

    elif line1 == (1,0,1,0) and line2 == (0,1,0,1): #ceros en [2] , [3] , [5] , [8] #DUDAA
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 1 = [5]\n"
        label += "Grupo de 1 = [2]\n"
        label += "Grupo de 1 = [8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R' + P'QR + PQ'R + PQR'\n"

#Grupos de [2] [3] [6] [ ]
    elif line1 == (1,0,0,1) and line2 == (0,1,1,0): #ceros en [2] , [3] , [6] , [7]
        label += "Grupo de 2 = [4],[8]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PR\n"

    elif line1 == (1,0,1,0) and line2 == (0,1,0,1): #ceros en [2] , [3] , [6] , [8] #DUDAA
        label += "Grupo de 1 = [4]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + P'Q + PQ'R\n"

#Grupos de [2] [3] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (0,1,0,1): #ceros en [2] , [3] , [7] , [8]
        label += "Grupo de 1 = [4]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PQ'R + QR'\n"

#Grupos de [2] [4] [5] [ ]
    elif line1 == (1,1,1,0) and line2 == (0,0,1,0): #ceros en [2] , [4] , [5] , [6]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + QR\n"

    elif line1 == (1,1,0,0) and line2 == (0,0,1,1): #ceros en [2] , [4] , [5] , [7]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + PQ\n"

    elif line1 == (1,1,1,0) and line2 == (0,0,0,1): #ceros en [2] , [4] , [5] , [8]
        label += "Grupo de 1 = [6]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + P'R + PQR'\n"
        
#Grupos de [2] [4] [6] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,0,1,0): #ceros en [2] , [4] , [6] , [7]
        label += "Grupo de 1 = [8]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + P'R' + PQR\n"

    elif line1 == (1,1,1,1) and line2 == (0,0,0,0): #ceros en [2] , [4] , [6] , [8]
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'\n"

#Grupos de [2] [4] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,0,0,1): #ceros en [2] , [4] , [7] , [8]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + QR'\n"

#Grupos de [2] [5] [6] [ ]
    elif line1 == (1,1,0,0) and line2 == (0,1,1,0): #ceros en [2] , [5] , [6] , [7]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + PR\n"

    elif line1 == (1,1,1,0) and line2 == (0,1,0,0): #ceros en [2] , [5] , [6] , [8]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + P'R + Q'R\n"

#Grupos de [2] [5] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (0,1,0,1): #ceros en [2] , [5] , [7] , [8]
        label += "Grupo de 1 = [6]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + Q'R + PQR'\n"

    elif line1 == (0,0,0,1) and line2 == (0,1,0,1): #ceros en [2] , [5] , [7] , [8]
        label += "Grupo de 1 = [4]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = QR' + PQ'R\n"



#Grupos de [2] [6] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,1,0,0): #ceros en [2] , [6] , [7] , [8]
        label += "Grupo de 2 = [3],[4]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + Q'R\n"
#Grupos de [2] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [3] [ ] [ ] [ ]
#Grupos de [3] [4] [5] [ ]
    elif line1 == (1,0,1,0) and line2 == (1,0,1,0): #ceros en [3] , [4] , [5] , [6]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [7],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + QR\n"

    elif line1 == (1,0,0,0) and line2 == (1,0,1,1): #ceros en [3] , [4] , [5] , [7]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [8],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + PQ\n"

    elif line1 == (1,0,1,0) and line2 == (1,0,0,1): #ceros en [3] , [4] , [5] , [8]
        label += "Grupo de 1 = [7]\n"
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + P'QR + PR'\n"

#Grupos de [3] [4] [6] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,0,1,0): #ceros en [3] , [4] , [6] , [7]
        label += "Grupo de 1 = [8]\n"
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + Q'R' + PQR\n"

    elif line1 == (1,0,1,1) and line2 == (1,0,0,0): #ceros en [3] , [4] , [6] , [8]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [7],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q + Q'R'\n"

#Grupos de [3] [4] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,0,0,1): #ceros en [3] , [4] , [7] , [8]
        label += "Grupo de 4 = [5],[6],[1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = R'\n"

#Grupos de [3] [5] [6] [ ]
    elif line1 == (1,0,0,0) and line2 == (1,1,1,0): #ceros en [3] , [5] , [6] , [7]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [4],[8]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + PR\n"

    elif line1 == (1,0,1,0) and line2 == (1,1,0,0): #ceros en [3] , [5] , [6] , [8]
        label += "Grupo de 1 = [7]\n"
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + P'QR + PQ'\n"

#Grupos de [3] [5] [7] [ ]
    elif line1 == (1,0,0,0) and line2 == (1,1,0,1): #ceros en [3] , [5] , [7] , [8]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'R' + PQ' + PR'\n"

#Grupos de [3] [6] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,0,0): #ceros en [3] , [6] , [7] , [8]
        label += "Grupo de 2 = [5],[1]\n"
        label += "Grupo de 2 = [2],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PQ'\n"
#Grupos de [3] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [4] [ ] [ ] [ ]
#Grupos de [4] [5] [6] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,0,1,0): #ceros en [4] , [5] , [6] , [7]
        label += "Grupo de 1 = [8]\n"
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [1],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + Q'R' + PQR\n"

    elif line1 == (1,1,1,0) and line2 == (1,0,0,0): #ceros en [4] , [5] , [6] , [8]
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [3],[7]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R + Q'R'\n"

#Grupos de [4] [5] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,0,0,1): #ceros en [4] , [5] , [7] , [8]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [6],[2]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + PR'\n"

#Grupos de [4] [6] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (1,0,0,0): #ceros en [4] , [6] , [7] , [8]
        label += "Grupo de 2 = [1],[3]\n"
        label += "Grupo de 2 = [1],[2]\n"
        label += "Grupo de 2 = [5],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q' + P'R' + Q'R'\n"
#Grupos de [4] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [5] [ ] [ ] [ ]
#Grupos de [5] [6] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,0,0): #ceros en [5] , [6] , [7] , [8]
        label += "Grupo de 4 = [1],[2],[3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = Q'\n"
#Grupos de [5] [7] [ ] [ ] ya están incluidos en las anteriores

#No hay grupos de [6] [ ] [ ] [ ], [7] [ ] [ ] [ ], [8] [ ] [ ] [ ] porque ya están dentro de las anteriores

# Grupos de 3 de 1 - TODO IMPLEMENTAR EL RESTO DE 3
#de tres unos-------------------------------------------
     #juntos
    elif line1 == (1,1,1,0) and line2 == (0,0,0,0):
         label += "Grupo de 2 = [1],[3]\n"
         label += "Grupo de 2 = [3],[5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q' + P'R \n"
    elif line1 == (0,1,1,1) and line2 == (0,0,0,0):
         label += "Grupo de 2 = [3],[7]\n"
         label += "Grupo de 2 = [7],[5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'R + P'Q \n"
    elif line1 == (0,0,0,0) and line2 == (1,1,1,0):
         label += "Grupo de 2 = [2],[4]\n"
         label += "Grupo de 2 = [4],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) = PQ' + PR \n"
    elif line1 == (0,0,0,0) and line2 == (0,1,1,1):
         label += "Grupo de 2 = [4],[8]\n"
         label += "Grupo de 2 = [8],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = PR + PQ \n"
    #en forma ed L normal
    elif line1 == (1,0,0,0) and line2 == (1,1,0,0):
         label += "Grupo de 2 = [1],[2]\n"
         label += "Grupo de 2 = [2],[4]\n"
         label += "Funcion simplificada, f(P , Q, R) = Q'R' + PQ' \n"
    elif line1 == (0,1,0,0) and line2 == (0,1,1,0):
         label += "Grupo de 2 = [3],[4]\n"
         label += "Grupo de 2 = [4],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) = Q'R + PR \n"
    elif line1 == (0,0,1,0) and line2 == (0,0,1,1):
         label += "Grupo de 2 = [7],[8]\n"
         label += "Grupo de 2 = [8],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = QR + PQ \n"
    elif line1 == (0,0,0,1) and line2 == (0,0,1,1):
         label += "Grupo de 2 = [5],[6]\n"
         label += "Grupo de 2 = [8],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = QR' + PQ \n"
    elif line1 == (0,0,1,0) and line2 == (0,1,1,0):
         label += "Grupo de 2 = [7],[8]\n"
         label += "Grupo de 2 = [4],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) = QR + PR \n"
    elif line1 == (0,1,0,0) and line2 == (1,1,0,0):
         label += "Grupo de 2 = [3],[4]\n"
         label += "Grupo de 2 = [2],[4]\n"
         label += "Funcion simplificada, f(P , Q, R) = Q'R + PQ' \n"
    #en forma ed L invertida
    elif line1 == (1,1,0,0) and line2 == (1,0,0,0):
         label += "Grupo de 2 = [1],[3]\n"
         label += "Grupo de 2 = [1],[2]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q' + Q'R' \n"
    elif line1 == (0,1,1,0) and line2 == (0,1,0,0):
         label += "Grupo de 2 = [3],[4]\n"
         label += "Grupo de 2 = [3],[7]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'R + Q'R \n"
    elif line1 == (0,0,1,1) and line2 == (0,0,1,0):
         label += "Grupo de 2 = [7],[5]\n"
         label += "Grupo de 2 = [7],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q + QR \n"
    elif line1 == (0,0,1,1) and line2 == (0,0,0,1):
         label += "Grupo de 2 = [7],[5]\n"
         label += "Grupo de 2 = [5],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q + QR' \n"
    elif line1 == (0,1,1,0) and line2 == (0,0,1,0):
         label += "Grupo de 2 = [3],[7]\n"
         label += "Grupo de 2 = [7],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) =  P'R + QR \n"
    elif line1 == (1,1,0,0) and line2 == (0,1,0,0):
         label += "Grupo de 2 = [1],[3]\n"
         label += "Grupo de 2 = [3],[4]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q' + Q'R \n"
 #en forma ed L con espacio---I--
  #----------------------------II
    elif line1 == (1,0,0,0) and line2 == (0,1,1,0):
         label += "Grupo de 1 = [1]\n"
         label += "Grupo de 2 = [4],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) =  P'Q'R' + PR \n"
    elif line1 == (0,1,0,0) and line2 == (0,0,1,1):
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 2 = [8],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R + PQ \n"
    elif line1 == (0,0,0,1) and line2 == (0,1,1,0):
         label += "Grupo de 1 = [5]\n"
         label += "Grupo de 2 = [4],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR' + PR \n"
    elif line1 == (0,0,1,0) and line2 == (1,1,0,0):
         label += "Grupo de 1 = [7]\n"
         label += "Grupo de 2 = [2],[4]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR + PQ' \n"
  #en forma ed L con espacio---I-- inversas
  #---------------------------- II       
    elif line1 == (1,1,0,0) and line2 == (0,0,1,0):
         label += "Grupo de 1 = [8]\n"
         label += "Grupo de 2 = [1],[3]\n"
         label += "Funcion simplificada, f(P , Q, R) =  P'Q' + PQR \n"
    elif line1 == (0,1,1,0) and line2 == (0,0,0,1):
         label += "Grupo de 1 = [6]\n"
         label += "Grupo de 2 = [3],[7]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'R + PQR' \n"
    elif line1 == (0,0,1,1) and line2 == (0,1,0,0):
         label += "Grupo de 1 = [4]\n"
         label += "Grupo de 2 = [7],[5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q + PQ'R \n"
    elif line1 == (0,1,1,0) and line2 == (1,0,0,0):
         label += "Grupo de 1 = [2]\n"
         label += "Grupo de 2 = [3],[7]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'R + PQ'R' \n"
 #en forma ed L con doble espacio---I--
  #----------------------------     --II 

    elif line1 == (1,1,0,0) and line2 == (0,0,0,1):
         label += "Grupo de 1 = [6]\n"
         label += "Grupo de 2 = [1],[3]\n"
         label += "Funcion simplificada, f(P , Q, R) =  P'Q' + PQR' \n"
    elif line1 == (0,0,1,1) and line2 == (1,0,0,0):
         label += "Grupo de 1 = [2]\n"
         label += "Grupo de 2 = [7],[5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q + PQ'R' \n"
    elif line1 == (0,0,0,1) and line2 == (1,1,0,0):
         label += "Grupo de 1 = [5]\n"
         label += "Grupo de 2 = [2],[4]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR' + PQ' \n"
    elif line1 == (1,0,0,0) and line2 == (0,0,1,1):
         label += "Grupo de 1 = [1]\n"
         label += "Grupo de 2 = [8],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R' + PQ \n"
#especiales....en L
    elif line1 == (1,0,0,0) and line2 == (1,0,0,1):
         label += "Grupo de 2 = [1],[2]\n"
         label += "Grupo de 2 = [2],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = Q'R' + PR' \n"
    elif line1 == (1,0,0,1) and line2 == (1,0,0,0):
         label += "Grupo de 2 = [1],[2]\n"
         label += "Grupo de 2 = [1],[5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'R' + Q'R' \n"
    elif line1 == (1,0,0,1) and line2 == (0,0,0,1):
         label += "Grupo de 2 = [1],[5]\n"
         label += "Grupo de 2 = [5],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'R' + QR' \n"
    elif line1 == (0,0,0,1) and line2 == (1,0,0,1):
         label += "Grupo de 2 = [2],[6]\n"
         label += "Grupo de 2 = [5],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = QR' + PR' \n"
# separados los tres
    elif line1 == (1,0,1,0) and line2 == (0,1,0,0):
         label += "Grupo de 1 = [1]\n"
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 1 = [4]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R' + P'QR + PQ'R \n"
    elif line1 == (0,1,0,1) and line2 == (0,0,1,0):
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 1 = [8]\n"
         label += "Grupo de 1 = [5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R + P'QR' + PQR \n"
    elif line1 == (0,1,0,0) and line2 == (1,0,1,0):
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 1 = [2]\n"
         label += "Grupo de 1 = [8]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R + PQ'R' + PQR \n"
    elif line1 == (0,0,1,0) and line2 == (0,1,0,1):
         label += "Grupo de 1 = [7]\n"
         label += "Grupo de 1 = [4]\n"
         label += "Grupo de 1 = [6]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR + PQ'R + PQR' \n"

# Grupos de 2 de 1
#------------juntos
    elif line1 == (1,1,0,0) and line2 == (0,0,0,0):
         label += "Grupo de 2 = [1],[3]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q' \n"
    elif line1 == (0,1,1,0) and line2 == (0,0,0,0):
         label += "Grupo de 2 = [3],[7]\n"
         label += "Funcion simplificada, f(P , Q, R) =  P'R \n"
    elif line1 == (0,0,1,1) and line2 == (0,0,0,0):
         label += "Grupo de 2 = [7],[5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q \n"
    elif line1 == (0,0,0,0) and line2 == (1,1,0,0):
         label += "Grupo de 2 = [2],[4]\n"
         label += "Funcion simplificada, f(P , Q, R) = PQ'\n"
    elif line1 == (0,0,0,0) and line2 == (0,1,1,0):
         label += "Grupo de 2 = [4],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) = PR \n"
    elif line1 == (0,0,0,0) and line2 == (0,0,1,1):
         label += "Grupo de 2 = [8],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = PQ \n"
         #---------
    elif line1 == (1,0,0,0) and line2 == (1,0,0,0):
         label += "Grupo de 2 = [1],[2]\n"
         label += "Funcion simplificada, f(P , Q, R) = Q'R' \n"
    elif line1 == (0,1,0,0) and line2 == (0,1,0,0):
         label += "Grupo de 2 = [3],[4]\n"
         label += "Funcion simplificada, f(P , Q, R) = Q'R\n"
    elif line1 == (0,0,1,0) and line2 == (0,0,1,0):
         label += "Grupo de 2 = [7],[8]\n"
         label += "Funcion simplificada, f(P , Q, R) = QR \n"
    elif line1 == (0,0,0,1) and line2 == (0,0,0,1):
         label += "Grupo de 2 = [5],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = QR' \n"
         #---------intercalados
    elif line1 == (1,0,0,0) and line2 == (0,1,0,0):
         label += "Grupo de 1 = [1]\n"
         label += "Grupo de 1 = [4]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R' + PQ'R \n"
    elif line1 == (0,1,0,0) and line2 == (0,0,1,0):
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 1 = [8]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R + PQR \n"
    elif line1 == (0,0,1,0) and line2 == (0,0,0,1):
         label += "Grupo de 1 = [7]\n"
         label += "Grupo de 1 = [6]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR + PQR' \n"
         #---------
    elif line1 == (0,1,0,0) and line2 == (1,0,0,0):
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 1 = [2]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R + PQ'R' \n"
    elif line1 == (0,0,1,0) and line2 == (0,1,0,0):
         label += "Grupo de 1 = [7]\n"
         label += "Grupo de 1 = [4]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR + PQ'R \n"
    elif line1 == (0,0,0,1) and line2 == (0,0,1,0):
         label += "Grupo de 1 = [8]\n"
         label += "Grupo de 1 = [5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR' + PQR \n"
         #---------
    elif line1 == (1,0,1,0) and line2 == (0,0,0,0):
         label += "Grupo de 1 = [1]\n"
         label += "Grupo de 1 = [7]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R' + P'QR \n"
    elif line1 == (0,1,0,1) and line2 == (0,0,0,0):
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 1 = [5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R + P'QR' \n"
    elif line1 == (0,0,0,0) and line2 == (1,0,1,0):
         label += "Grupo de 1 = [2]\n"
         label += "Grupo de 1 = [4]\n"
         label += "Funcion simplificada, f(P , Q, R) = PQ'R' + PQR \n"        
    elif line1 == (0,0,0,0) and line2 == (0,1,0,1):
         label += "Grupo de 1 = [8]\n"
         label += "Grupo de 1 = [6]\n"
         label += "Funcion simplificada, f(P , Q, R) = PQ'R + PQR' \n"
     #---------intercal de doble espacio
    elif line1 == (1,0,0,0) and line2 == (0,0,1,0):
         label += "Grupo de 1 = [1]\n"
         label += "Grupo de 1 = [8]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R' + PQR \n"
    elif line1 == (0,1,0,0) and line2 == (0,0,0,1):
         label += "Grupo de 1 = [3]\n"
         label += "Grupo de 1 = [6]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'Q'R + PQR' \n"
    elif line1 == (0,0,1,0) and line2 == (1,0,0,0):
         label += "Grupo de 1 = [7]\n"
         label += "Grupo de 1 = [2]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR + PQ'R' \n"
    elif line1 == (0,0,0,1) and line2 == (0,1,0,0):
         label += "Grupo de 1 = [5]\n"
         label += "Grupo de 1 = [4]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR' + PQ'R \n"
     #--------Esquinas  
    elif line1 == (0,0,0,1) and line2 == (1,0,0,0):
         label += "Grupo de 1 = [5]\n"
         label += "Grupo de 1 = [2]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'QR' + PQ'R' \n"
    elif line1 == (1,0,0,0) and line2 == (0,0,0,1):
         label += "Grupo de 1 = [1]\n"
         label += "Grupo de 1 = [6]\n"
         label += "Funcion simplificada, f(P , Q, R) =P'Q'R' + PQR' \n"
     #--------Especiales
    elif line1 == (1,0,0,1) and line2 == (0,0,0,0):
         label += "Grupo de 2 = [1],[5]\n"
         label += "Funcion simplificada, f(P , Q, R) = P'R' \n"   
    elif line1 == (0,0,0,0) and line2 == (1,0,0,1):
         label += "Grupo de 2 = [2],[6]\n"
         label += "Funcion simplificada, f(P , Q, R) = PR' \n"

# Grupos de 1 de 1
    elif line1 == (1,0,0,0) and line2 == (0,0,0,0):  #caso en [1]
        label += "Grupo de 1 = [1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R'\n"

    elif line1 == (0,0,0,0) and line2 == (1,0,0,0):  #caso en [2]
        label += "Grupo de 1 = [2]\n"
        label += "Funcion simplificada, S(P, Q, R) = PQ'R'\n"

    elif line1 == (0,1,0,0) and line2 == (0,0,0,0):  #caso en [3]
        label += "Grupo de 1 = [3]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R\n"

    elif line1 == (0,0,0,0) and line2 == (0,1,0,0):  #caso en [4]
        label += "Grupo de 1 = [4]\n"
        label += "Funcion simplificada, S(P, Q, R) = PQ'R\n"

    elif line1 == (0,0,0,1) and line2 == (0,0,0,0):  #caso en [5]
        label += "Grupo de 1 = [5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'QR'\n"

    elif line1 == (0,0,0,0) and line2 == (0,0,0,1):  #caso en [6]
        label += "Grupo de 1 = [6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R\n"

    elif line1 == (0,0,1,0) and line2 == (0,0,0,0):  #caso en [7]
        label += "Grupo de 1 = [7]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'QR\n"

    elif line1 == (0,0,0,0) and line2 == (0,0,1,0):  #caso en [8]
        label += "Grupo de 1 = [8]\n"
        label += "Funcion simplificada, S(P, Q, R) = PQR\n" 

    # Dsp de checkear
    elif line1 == (1,0,0,0) and line2 == (0,0,1,1):
        label += "Grupo de 1 = [1]\n"
        label += "Grupo de 1 = [6]\n"
        label += "Grupo de 1 = [8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R' + PQ'\n"

    elif line1 == (0,1,0,1) and line2 == (0,0,1,0):
        label += "Grupo de 2 = [3],[5]\n"
        label += "Grupo de 1 = [8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R + QR'\n"

    elif line1 == (1,0,1,0) and line2 == (1,0,1,0):
        label += "Grupo de 1 = [3]\n"
        label += "Grupo de 1 = [6]\n"
        label += "Grupo de 1 = [8]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'Q'R + PQ\n"

    elif line1 == (1,1,1,1) and line2 == (0,0,1,0):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 2 = [2],[1]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + Q'R'\n"

    elif line1 == (1,1,1,1) and line2 == (1,0,0,0):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 2 = [3],[4]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + Q'R\n"

    elif line1 == (1,1,1,1) and line2 == (0,0,1,0):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 2 = [8],[7]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + QR\n"

    elif line1 == (1,1,1,1) and line2 == (0,0,0,1):
        label += "Grupo de 4 = [1],[3],[7],[5]\n"
        label += "Grupo de 2 = [5],[6]\n"
        label += "Funcion simplificada, S(P, Q, R) = P' + QR'\n"

    elif line1 == (1,0,0,1) and line2 == (0,1,0,0):
        label += "Grupo de 1 = [4]\n"
        label += "Grupo de 2 = [1],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PQ'R \n"

    elif line1 == (1,0,0,1) and line2 == (0,0,1,0):
        label += "Grupo de 1 = [8]\n"
        label += "Grupo de 2 = [1],[5]\n"
        label += "Funcion simplificada, S(P, Q, R) = P'R' + PQR\n"

    return label