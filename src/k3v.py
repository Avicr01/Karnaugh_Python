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
        print(Fore.RESET + "Variables para " + Fore.RED + "[ ", i ," ]" + Fore.RESET);
        listing.append(int(input(var)))

    return listing
 
 # ES NECESARIO CORREGIR LOS GRUPOS DE 4, 5 y 6!

#Para todos los ceros
def k3v (listing):
    line1 = ()
    line2 = ()
    line1 = (listing[0],listing[2],listing[6],listing[4])
    line2 = (listing[1],listing[3],listing[7],listing[5])

    print("P \\ QR   00   01   11   10")
    print("         |-------------------")
    print("    0    |  ", listing[0] ,"  |  ",listing[2],"  |  ",listing[6],"  |  ",listing[4]," |")
    print("         |-------------------")
    print("    1    |  ", listing[1] ,"  |  ",listing[3],"  |  ",listing[7],"  |  ",listing[5]," |")
  
    print("P \\ QR     00      01      11      10")
    print("         ---------------------------------")
    print("    0    |  [1]  |  [3]  |  [7]  |  [5]  |")
    print("         ---------------------------------")
    print("    1    |  [2]  |  [4]  |  [8]  |  [6]  |") 
    
    # Todos de 0
    if line1 == (0, 0, 0, 0) and line2 == (0, 0, 0, 0):
        print("No hay grupos")
        print("Funcion simplificada, S( P , Q , R )  = 0")

    # Todos de 1
    elif line1 == (1, 1, 1, 1) and line2 == (1, 1, 1, 1):
        print("Grupo de 8 = [1], [2], [3], [4], [5], [6], [7], [8]")
        print("Funcion simplificada, S( P , Q , R )  = 1")

    #Grupos con siete unos [ ]
    elif line1 == (1,1,1,0) and line2 == (1,1,1,1):
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [3],[4],[7],[8]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, f(P, Q, R) = Q' + R + P ")

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [3],[4],[7],[8]")
        print("Funcion simplificada, f(P , Q, R) = P' + Q' + R ") 

    elif line1 == (1,1,0,1) and line2 == (1,1,1,1):
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, f(P, Q, R) = Q' + R' + P ")

    elif line1 == (1,1,1,1) and line2 == (1,1,0,1):
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Funcion simplificada, f(P, Q, R) = P' + Q' + R'")

    elif line1 == (1,0,1,1) and line2 == (1,1,1,1):
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Grupo de 4 = [7],[8],[5],[6]")
        print("Funcion simplificada, f(P, Q, R) = R' + Q + P ")# commit

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [3],[4],[7],[8]")
        print("Funcion simplificada, f(P , Q, R) = P' + Q' + R ")

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [3],[4],[7],[8]")
        print("Funcion simplificada, f(P , Q, R) = P' + Q' + R ")

    elif line1 == (1,1,1,1) and line2 == (1,1,1,0):
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [3],[4],[7],[8]")
        print("Funcion simplificada, f(P , Q, R) = P' + Q' + R ")

#Grupos de 6 de 1 (dos ceros)
#Grupos de seis unos (dos ceros)
#GRUPOS DE CEROS
#Grupo de [1] con el resto [ ]
    elif line1 == (0,0,1,1) and line2 == (1,1,1,1): #ceros en [1] y [3]
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q + P")

    elif line1 == (0,1,1,1) and line2 == (0,1,1,1): #ceros en [1] y [2]
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = R + Q")

    elif line1 == (0,1,1,1) and line2 == (1,0,1,1): #ceros en [1] y [4]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [6],[2]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R + Q + PR'")

    elif line1 == (0,1,1,1) and line2 == (1,1,0,1): #ceros en [1] y [8]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R + QR' + PQ'")

    elif line1 == (0,1,1,1) and line2 == (1,1,1,0): #ceros en [1] y [6]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = R + P'Q + PQ'")

    elif line1 == (0,1,0,1) and line2 == (1,1,1,1): #ceros en [1] y [7]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + QR' + P")

    elif line1 == (0,1,1,0) and line2 == (1,1,1,1): #ceros en [1] y [5]
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = R + P")

#Grupo de [2] con el resto [ ]
    elif line1 == (1,1,1,1) and line2 == (0,0,1,1): #ceros en [2] y [4]
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P' + Q")

    elif line1 == (1,0,1,1) and line2 == (0,1,1,1): #ceros en [2] y [3]
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[1]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + Q + PR")

    elif line1 == (1,1,0,1) and line2 == (0,1,1,1): #ceros en [2] y [7]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + QR' + PR")

    elif line1 == (1,1,1,0) and line2 == (0,1,1,1): #ceros en [2] y [5]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [8],[6]")
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + R + PQ")

    elif line1 == (1,1,1,1) and line2 == (0,1,0,1): #ceros en [2] y [8]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P' + Q'R + QR'")

    elif line1 == (1,1,1,1) and line2 == (0,1,1,0): #ceros en [2] y [6]
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Funcion simplificada, S(P, Q, R) = P' + R")

#Grupo de [3] con el resto [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,1,1): #ceros en [3] y [7]
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Funcion simplificada, S(P, Q, R) = R' + P")

    elif line1 == (1,0,1,1) and line2 == (1,0,1,1): #ceros en [3] y [4]
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = R' + Q")

    elif line1 == (1,0,1,1) and line2 == (1,1,0,1): #ceros en [3] y [8]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 4 = [5],[6],[1],[2]")
        print("Funcion simplificada, S(P, Q, R) = R' + P'Q + PQ'")

    elif line1 == (1,0,1,1) and line2 == (1,1,1,0): #ceros en [3] y [6]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + QR + PQ'")

    elif line1 == (1,0,1,0) and line2 == (1,1,1,1): #ceros en [3] y [5]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + QR + P")

#Grupo de [4] con el resto [ ]
    elif line1 == (1,1,1,1) and line2 == (1,0,0,1): #ceros en [4] y [8]
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Funcion simplificada, S(P, Q, R) = P' + R'")

    elif line1 == (1,1,1,0) and line2 == (1,0,1,1): #ceros en [4] y [5]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + QR + PR'")

    elif line1 == (1,1,0,1) and line2 == (1,0,1,1): #ceros en [4] y [7]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [8],[6]")
        print("Grupo de 4 = [5],[6],[1],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + R' + PQ")

    elif line1 == (1,1,1,1) and line2 == (1,0,1,0): #ceros en [4] y [6]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P' + Q'R' + QR")

#Grupo de [5] con el resto [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,1,1): #ceros en [5] y [7]
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q' + P")

    elif line1 == (1,1,1,0) and line2 == (1,1,0,1): #ceros en [5] y [8]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [6],[2]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q' + P'R + PR'")

    elif line1 == (1,1,1,0) and line2 == (1,1,1,0): #ceros en [5] y [6]
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = R + Q")

#Grupo de [6] con el resto [ ]
    elif line1 == (1,1,0,1) and line2 == (1,1,1,0): #ceros en [6] y [7]
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[1]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q' + P'R' + PR")

    elif line1 == (1,1,1,1) and line2 == (1,1,0,0): #ceros en [6] y [8]
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = P' + Q'")

#Grupo de [7] con el resto [ ]
    elif line1 == (1,1,0,1) and line2 == (1,1,0,1): #ceros en [7] y [8]
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Grupo de 4 = [1],[2],[5],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q' + R'")

#No hay grupos de [8] porque ya se asoció con todos

#GRUPOS DE CINCO UNOS (tres ceros)
#Grupos de [1] [ ] [ ]
#Grupos de [1] [2] [ ]
    elif line1 == (0,0,1,1) and line2 == (0,1,1,1): #ceros en [1] , [2] y [3]
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q + PR")

    elif line1 == (0,1,1,1) and line2 == (0,0,1,1): #ceros en [1] , [2] y [4]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R + Q")

    elif line1 == (0,1,1,0) and line2 == (0,1,1,1): #ceros en [1] , [2] y [5]
        print("Grupo de 2 = [8],[6]")
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Funcion simplificada, S(P, Q, R) = R + PQ")

    elif line1 == (0,1,1,1) and line2 == (0,1,1,0): #ceros en [1] , [2] y [6]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Funcion simplificada, S(P, Q, R) = R + P'Q")

    elif line1 == (0,1,0,1) and line2 == (0,1,1,1): #ceros en [1] , [2] y [7]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + QR' + PR")

    elif line1 == (0,1,1,1) and line2 == (0,1,0,1): #ceros en [1] , [2] y [8]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + QR' + P'R")

#Grupos de [1] [3] [ ]
    elif line1 == (0,0,1,1) and line2 == (1,0,1,1): #ceros en [1] , [3] y [4]
        print("Grupo de 2 = [6],[2]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q + PR'")

    elif line1 == (0,0,1,0) and line2 == (1,1,1,1): #ceros en [1] , [3] y [5]
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = QR + P")

    elif line1 == (0,0,1,1) and line2 == (1,1,1,0): #ceros en [1] , [3] y [6]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PQ' + QR")

    elif line1 == (0,0,0,1) and line2 == (1,1,1,1): #ceros en [1] , [3] y [7]
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = QR' + P")

    elif line1 == (0,0,1,1) and line2 == (1,1,0,1): #ceros en [1] , [3] y [8]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PQ' + QR'")

#Grupos de [1] [4] [ ]
    elif line1 == (0,1,1,0) and line2 == (1,0,1,1): #ceros en [1] , [4] y [5]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PR' + QR")

    elif line1 == (0,1,1,1) and line2 == (1,0,1,0): #ceros en [1] , [4] y [6]
        print("Grupo de 1 = [2]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'R + P'Q + PQ'R' + QR")

    elif line1 == (0,1,0,1) and line2 == (1,0,1,1): #ceros en [1] , [4] y [7]
        print("Grupo de 1 = [3]")
        print("Grupo de 2 = [8],[6]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R + QR' + PR' + PQ")

    elif line1 == (0,1,1,1) and line2 == (1,0,0,1): #ceros en [1] , [4] y [8] 
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PR' + P'Q")

#Grupos de [1] [5] [ ]
    elif line1 == (0,1,1,0) and line2 == (1,1,1,0): #ceros en [1] , [5] y [6]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Funcion simplificada, S(P, Q, R) = R + PQ'")

    elif line1 == (0,1,0,0) and line2 == (1,1,1,1): #ceros en [1] , [5] y [7]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + P")

    elif line1 == (0,1,1,0) and line2 == (1,1,0,1): #ceros en [1] , [5] y [8] 
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PR' + Q'R")

#Grupos de [1] [6] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,1,1,0): #ceros en [1] , [6] y [7]
        print("Grupo de 1 = [5]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + P'QR' + PQ' + PR")

    elif line1 == (0,1,1,1) and line2 == (1,1,0,0): #ceros en [1] , [6] y [8]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [2],[3]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PQ' + P'R")

#Grupos de [1] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,1,0,1): #ceros en [1] , [7] y [8]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + QR' + PQ'")
#No hay grupos de [1] [8] [ ] porque ya está incluido

#Grupos de [2] [ ] [ ]
#Grupos de [2] [3] [ ]
    elif line1 == (1,0,1,1) and line2 == (0,0,1,1): #ceros en [2] , [3] y [4]
        print("Grupo de 2 = [5],[1]")
        print("Grupo de 4 = [7],[5],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + Q")

    elif line1 == (1,0,1,0) and line2 == (0,1,1,1): #ceros en [2] , [3] y [5]
        print("Grupo de 1 = [1]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R' + QR + PR + PQ")

    elif line1 == (1,0,1,1) and line2 == (0,1,1,0): #ceros en [2] , [3] y [6]
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PR + P'Q")

    elif line1 == (1,0,0,1) and line2 == (0,1,1,1): #ceros en [2] , [3] y [7]
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PR + QR'")

    elif line1 == (1,0,1,1) and line2 == (0,1,0,1): #ceros en [2] , [3] y [8]
        print("Grupo de 1 = [4]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + P'Q + PQ'R + QR'")

#Grupos de [2] [4] [ ]
    elif line1 == (1,1,1,0) and line2 == (0,0,1,1): #ceros en [2] , [4] y [5]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + PQ + P'R")

    elif line1 == (1,0,0,1) and line2 == (0,1,1,1): #ceros en [2] , [4] y [6]
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P' + QR")

    elif line1 == (1,1,0,1) and line2 == (0,0,1,1): #ceros en [2] , [4] y [7]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [5],[1]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + PQ + P'R'")

    elif line1 == (1,1,1,1) and line2 == (0,0,0,1): #ceros en [2] , [4] y [8]
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P' + QR'")

#Grupos de [2] [5] [ ]
    elif line1 == (1,1,1,0) and line2 == (0,1,1,0): #ceros en [2] , [5] y [6]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 4 = [3],[7],[4],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + R")

    elif line1 == (1,1,0,0) and line2 == (0,1,1,1): #ceros en [2] , [5] y [7]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + PQ + Q'R")

    elif line1 == (1,1,1,0) and line2 == (0,1,0,1): #ceros en [2] , [5] y [8]
        print("Grupo de 1 = [6]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [3],[4]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + P'R + Q'R + PQR'")

#Grupos de [2] [6] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,1,1,0): #ceros en [2] , [6] y [7]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PR + P'Q'")

    elif line1 == (1,1,1,1) and line2 == (0,1,0,0): #ceros en [2] , [6] y [8]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 4 = [1],[3],[7],[5]")        
        print("Funcion simplificada, S(P, Q, R) = P' + Q'R")

#Grupos de [2] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,1,0,1): #ceros en [2] , [7] y [8]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + QR' + P'Q'")
#No hay grupos de [2] [8] [ ] porque ya está incluido 

#Grupos de [3] [ ] [ ]
#Grupos de [3] [4] [ ]
    elif line1 == (1,0,1,0) and line2 == (1,0,1,1): #ceros en [3] , [4] y [5]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + QR + PR'")

    elif line1 == (1,0,1,1) and line2 == (1,0,1,0): #ceros en [3] , [4] y [6]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + QR + P'R'")

    elif line1 == (1,0,0,1) and line2 == (1,0,1,1): #ceros en [3] , [4] y [7]
        print("Grupo de 2 = [8],[6]")
        print("Grupo de 4 = [5],[6],[1],[2]")
        print("Funcion simplificada, S(P, Q, R) = R' + PQ")

    elif line1 == (1,0,1,1) and line2 == (1,0,0,1): #ceros en [3] , [4] y [8]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 4 = [5],[6],[1],[2]")
        print("Funcion simplificada, S(P, Q, R) = R' + P'Q")

#Grupos de [3] [5] [ ]
    elif line1 == (1,0,1,0) and line2 == (1,1,1,0): #ceros en [3] , [5] y [6]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + QR + PQ'")

    elif line1 == (1,0,0,0) and line2 == (1,1,1,1): #ceros en [3] , [5] y [7]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + P")

    elif line1 == (1,0,1,0) and line2 == (1,1,0,1): #ceros en [3] , [5] y [8]
        print("Grupo de 1 = [7]")
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + P'QR + PQ' + PR'")

#Grupos de [3] [6] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,1,0): #ceros en [3] , [6] y [7]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PR + Q'R'")

    elif line1 == (1,0,1,1) and line2 == (1,1,0,0): #ceros en [3] , [6] y [8]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PQ' + P'R'")

#Grupos de [3] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,0,1): #ceros en [3] , [7] y [8]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 4 = [5],[6],[1],[2]")
        print("Funcion simplificada, S(P, Q, R) = R' + PQ'")
#No hay grupos de [3] [8] [ ] porque ya está incluido 

#Grupos de [4] [ ] [ ]
#Grupos de [4] [5] [ ]
    elif line1 == (1,1,1,0) and line2 == (1,0,1,0): #ceros en [4] , [5] y [6]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + QR + P'Q'")

    elif line1 == (1,1,0,0) and line2 == (1,0,1,1): #ceros en [4] , [5] y [7]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + PQ + Q'R'")

    elif line1 == (1,1,1,0) and line2 == (1,0,0,1): #ceros en [4] , [5] y [8]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PR' + P'Q'")

#Grupos de [4] [6] [ ]
    elif line1 == (1,1,0,1) and line2 == (1,0,1,0): #ceros en [4] , [6] y [7]
        print("Grupo de 1 = [8]")
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + P'R' + Q'R' + PQR")

    elif line1 == (1,1,1,1) and line2 == (1,0,0,0): #ceros en [4] , [6] y [8]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P' + Q'R'")

#Grupos de [4] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (1,0,0,1): #ceros en [4] , [7] y [8]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 4 = [5],[6],[1],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + R'")
#No hay grupos de [4] [8] [ ] porque ya está incluido

#Grupos de [5] [ ] [ ]
#Grupos de [5] [6] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,1,0): #ceros en [5] , [6] y [7]
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q' + PR")

    elif line1 == (1,1,1,0) and line2 == (1,1,0,0): #ceros en [5] , [6] y [8]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q' + P'R")

#Grupos de [5] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,0,1): #ceros en [5] , [7] y [8]
        print("Grupo de 2 = [6],[2]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q' + PR'")
#No hay grupos de [5] [8] [ ] porque ya está incluido 

#Grupos de [6] [ ] [ ]
#Grupos de [6] [7] [ ]
    elif line1 == (1,0,1,1) and line2 == (1,0,0,1): #ceros en [6] , [7] y [8]
        print("Grupo de 2 = [1],[5]")
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = R' + P'Q")
#No hay grupos de [7] [ ] [ ] ni [8] [ ] [ ] porque ya está incluido en los anteriores


#GRUPOS DE CUATRO UNOS (cuatro ceros)
#Grupos de [1] [ ] [ ] [ ]
#Grupos de [1] [2] [ ] [ ]
#Grupos de [1] [2] [3] [ ]
    elif line1 == (0,0,1,1) and line2 == (0,0,1,1): #ceros en [1] , [2] , [3] , [4]
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q")

    elif line1 == (0,0,1,0) and line2 == (0,1,1,1): #ceros en [1] , [2] , [3] , [5]
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = QR + PR + PQ")

    elif line1 == (0,0,1,1) and line2 == (0,1,1,0): #ceros en [1] , [2] , [3] , [6]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PR")

    elif line1 == (0,0,0,1) and line2 == (0,1,1,1): #ceros en [1] , [2] , [3] , [7]
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PR")

    elif line1 == (0,0,1,1) and line2 == (0,1,1,0): #ceros en [1] , [2] , [3] , [8]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = QR' + PR")

#Grupos de [1] [2] [4] [ ]
    elif line1 == (0,1,1,0) and line2 == (0,0,1,1): #ceros en [1] , [2] , [4] , [5]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PQ")

    elif line1 == (0,1,1,1) and line2 == (0,0,1,0): #ceros en [1] , [2] , [4] , [6]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P'R + P'Q + QR")

    elif line1 == (0,1,0,1) and line2 == (0,0,1,1): #ceros en [1] , [2] , [4] , [7]
        print("Grupo de 1 = [3]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R + QR' + PQ")

    elif line1 == (0,1,1,1) and line2 == (0,0,0,1): #ceros en [1] , [2] , [4] , [8]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R + QR'")

#Grupos de [1] [2] [5] [ ]
    elif line1 == (0,1,1,0) and line2 == (0,1,1,0): #ceros en [1] , [2] , [5] , [6]
        print("Grupo de 4 = [3],[4],[7],[8]")
        print("Funcion simplificada, S(P, Q, R) = R")
        
    elif line1 == (0,1,0,0) and line2 == (0,1,1,1): #ceros en [1] , [2] , [5] , [7]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + PQ")

    elif line1 == (0,1,1,0) and line2 == (0,1,0,1): #ceros en [1] , [2] , [5] , [8]
        print("Grupo de 1 = [6]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [3],[7]")
        print("Funcion simplificada, S(P, Q, R) = P'R + Q'R + PQR'")

#Grupos de [1] [2] [6] [ ]
    elif line1 == (0,1,0,1) and line2 == (0,1,1,0): #ceros en [1] , [2] , [6] , [7]
        print("Grupo de 1 = [5]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + P'QR' + PR")

    elif line1 == (0,1,1,1) and line2 == (0,1,0,0): #ceros en [1] , [2] , [6] , [8]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + Q'R")

#Grupos de [1] [2] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (0,1,0,1): #ceros en [1] , [2] , [7] , [8]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + QR'")
#Grupos de [1] [2] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [3] [ ] [ ]
#Grupos de [1] [3] [4] [ ]
    elif line1 == (0,0,1,0) and line2 == (1,0,1,1): #ceros en [1] , [3] , [4] , [5]
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = QR + PR'")

    elif line1 == (0,0,1,1) and line2 == (1,0,1,0): #ceros en [1] , [3] , [4] , [6]
        print("Grupo de 1 = [2]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PQ'R' + QR")

    elif line1 == (0,0,0,1) and line2 == (1,0,1,1): #ceros en [1] , [3] , [4] , [7]
        print("Grupo de 2 = [8],[6]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = QR' + PR' + PQ")

    elif line1 == (0,0,1,1) and line2 == (1,0,0,1): #ceros en [1] , [3] , [4] , [8]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PR'")

#Grupos de [1] [3] [5] [ ]
    elif line1 == (0,0,1,0) and line2 == (1,1,1,0): #ceros en [1] , [3] , [5] , [6]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = QR + PQ'")

    elif line1 == (0,0,0,0) and line2 == (1,1,1,1): #ceros en [1] , [3] , [5] , [7]
        print("Grupo de 4 = [2],[4],[8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P")

    elif line1 == (0,0,1,0) and line2 == (1,1,0,1): #ceros en [1] , [3] , [5] , [8]
        print("Grupo de 1 = [7]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'QR + PQ' + PR'")

#Grupos de [1] [3] [6] [ ]
    elif line1 == (0,0,0,1) and line2 == (1,1,1,0): #ceros en [1] , [3] , [6] , [7]
        print("Grupo de 1 = [5]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'QR' + PQ' + PR")

    elif line1 == (0,0,1,1) and line2 == (1,1,0,0): #ceros en [1] , [3] , [6] , [8]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [2],[4]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + PQ'")

#Grupos de [1] [3] [7] [ ]
    elif line1 == (0,0,0,1) and line2 == (1,1,0,1): #ceros en [1] , [3] , [7] , [8]
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [2],[4]")
        print("Funcion simplificada, S(P, Q, R) = QR' + PQ'")
#Grupos de [1] [3] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [4] [ ] [ ]
#Grupos de [1] [4] [5] [ ]
    elif line1 == (0,1,1,0) and line2 == (1,0,1,0): #ceros en [1] , [4] , [5] , [6]
        print("Grupo de 1 = [2]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PQ'R' + QR")

    elif line1 == (0,1,0,0) and line2 == (1,0,1,1): #ceros en [1] , [4] , [5] , [7]
        print("Grupo de 1 = [3]")
        print("Grupo de 2 = [8],[6]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R + PR' + PQ")

    elif line1 == (0,1,1,0) and line2 == (1,0,0,1): #ceros en [1] , [4] , [5] , [8]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PR'")

#Grupos de [1] [4] [6] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,0,1,0): #ceros en [1] , [4] , [6] , [7] #DUDAA
        print("Grupo de 1 = [2]")
        print("Grupo de 1 = [3]")
        print("Grupo de 1 = [8]")
        print("Grupo de 1 = [5]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R + P'QR' + PQ'R' + PQR")

    elif line1 == (0,1,1,1) and line2 == (1,0,0,0): #ceros en [1] , [4] , [6] , [8]
        print("Grupo de 1 = [2]")
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P'R + P'Q + PQ'R'")

#Grupos de [1] [4] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,0,0,1): #ceros en [1] , [4] , [7] , [8]
        print("Grupo de 1 = [3]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R + QR' + PR'")
#Grupos de [1] [4] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [5] [ ] [ ]
#Grupos de [1] [5] [6] [ ]
    elif line1 == (0,1,0,0) and line2 == (1,1,1,0): #ceros en [1] , [5] , [6] , [7]
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + PQ' + PR")

    elif line1 == (0,1,1,0) and line2 == (1,1,0,0): #ceros en [1] , [5] , [6] , [8]
        print("Grupo de 2 = [3],[7]")
        print("Grupo de 2 = [2],[4]")
        print("Funcion simplificada, S(P, Q, R) = P'R + PQ'")

#Grupos de [1] [5] [7] [ ]
    elif line1 == (0,1,0,0) and line2 == (1,1,0,1): #ceros en [1] , [5] , [7] , [8]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + PR'")
#Grupos de [1] [5] [8] [ ] ya están incluidos en las anteriores

#Grupos de [1] [6] [ ] [ ]
#Grupos de [1] [6] [7] [ ]
    elif line1 == (0,1,0,1) and line2 == (1,1,0,0): #ceros en [1] , [6] , [7] , [8]
        print("Grupo de 1 = [3]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [3],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q'R + P'QR' + PQ'")
#Grupos de [1] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [2] [ ] [ ] [ ]
#Grupos de [2] [3] [4] [ ]
    elif line1 == (1,0,1,0) and line2 == (0,0,1,1): #ceros en [2] , [3] , [4] , [5]
        print("Grupo de 1 = [1]")
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R' + QR + PQ")

    elif line1 == (1,0,1,1) and line2 == (0,0,1,0): #ceros en [2] , [3] , [4] , [6]
        print("Grupo de 2 = [7],[8]")
        print("Grupo de 2 = [7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + QR")

    elif line1 == (1,0,0,1) and line2 == (0,0,1,1): #ceros en [2] , [3] , [4] , [7]
        print("Grupo de 2 = [5],[1]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PQ")

    elif line1 == (1,0,1,1) and line2 == (0,0,0,1): #ceros en [2] , [3] , [4] , [8]
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + P'Q + QR'")

#Grupos de [2] [3] [5] [ ]
    elif line1 == (1,0,1,0) and line2 == (0,1,1,0): #ceros en [2] , [3] , [5] , [6]
        print("Grupo de 1 = [1]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R' + QR + PR")

    elif line1 == (1,0,0,0) and line2 == (0,1,1,1): #ceros en [2] , [3] , [5] , [7]
        print("Grupo de 1 = [1]")
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R' + PR + PQ")

    elif line1 == (1,0,1,0) and line2 == (0,1,0,1): #ceros en [2] , [3] , [5] , [8] #DUDAA
        print("Grupo de 1 = [3]")
        print("Grupo de 1 = [5]")
        print("Grupo de 1 = [2]")
        print("Grupo de 1 = [8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R' + P'QR + PQ'R + PQR'")

#Grupos de [2] [3] [6] [ ]
    elif line1 == (1,0,0,1) and line2 == (0,1,1,0): #ceros en [2] , [3] , [6] , [7]
        print("Grupo de 2 = [4],[8]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PR")

    elif line1 == (1,0,1,0) and line2 == (0,1,0,1): #ceros en [2] , [3] , [6] , [8] #DUDAA
        print("Grupo de 1 = [4]")
        print("Grupo de 2 = [7],[5]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + P'Q + PQ'R")

#Grupos de [2] [3] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (0,1,0,1): #ceros en [2] , [3] , [7] , [8]
        print("Grupo de 1 = [4]")
        print("Grupo de 2 = [5],[6]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PQ'R + QR'")

#Grupos de [2] [4] [5] [ ]
    elif line1 == (1,1,1,0) and line2 == (0,0,1,0): #ceros en [2] , [4] , [5] , [6]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + QR")

    elif line1 == (1,1,0,0) and line2 == (0,0,1,1): #ceros en [2] , [4] , [5] , [7]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + PQ")

    elif line1 == (1,1,1,0) and line2 == (0,0,0,1): #ceros en [2] , [4] , [5] , [8]
        print("Grupo de 1 = [6]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[7]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + P'R + PQR'")
        
#Grupos de [2] [4] [6] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,0,1,0): #ceros en [2] , [4] , [6] , [7]
        print("Grupo de 1 = [8]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + P'R' + PQR")

    elif line1 == (1,1,1,1) and line2 == (0,0,0,0): #ceros en [2] , [4] , [6] , [8]
        print("Grupo de 4 = [1],[3],[7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P'")

#Grupos de [2] [4] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,0,0,1): #ceros en [2] , [4] , [7] , [8]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [5],[6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + QR'")

#Grupos de [2] [5] [6] [ ]
    elif line1 == (1,1,0,0) and line2 == (0,1,1,0): #ceros en [2] , [5] , [6] , [7]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + PR")

    elif line1 == (1,1,1,0) and line2 == (0,1,0,0): #ceros en [2] , [5] , [6] , [8]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [3],[7]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + P'R + Q'R")

#Grupos de [2] [5] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (0,1,0,1): #ceros en [2] , [5] , [7] , [8]
        print("Grupo de 1 = [6]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [3],[4]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + Q'R + PQR'")

#Grupos de [2] [6] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (0,1,0,0): #ceros en [2] , [6] , [7] , [8]
        print("Grupo de 2 = [3],[4]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + Q'R")
#Grupos de [2] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [3] [ ] [ ] [ ]
#Grupos de [3] [4] [5] [ ]
    elif line1 == (1,0,1,0) and line2 == (1,0,1,0): #ceros en [3] , [4] , [5] , [6]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [7],[8]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + QR")

    elif line1 == (1,0,0,0) and line2 == (1,0,1,1): #ceros en [3] , [4] , [5] , [7]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [8],[6]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + PQ")

    elif line1 == (1,0,1,0) and line2 == (1,0,0,1): #ceros en [3] , [4] , [5] , [8]
        print("Grupo de 1 = [7]")
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + P'QR + PR'")

#Grupos de [3] [4] [6] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,0,1,0): #ceros en [3] , [4] , [6] , [7]
        print("Grupo de 1 = [8]")
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + Q'R' + PQR")

    elif line1 == (1,0,1,1) and line2 == (1,0,0,0): #ceros en [3] , [4] , [6] , [8]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [7],[5]")
        print("Funcion simplificada, S(P, Q, R) = P'Q + Q'R'")

#Grupos de [3] [4] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,0,0,1): #ceros en [3] , [4] , [7] , [8]
        print("Grupo de 4 = [5],[6],[1],[2]")
        print("Funcion simplificada, S(P, Q, R) = R'")

#Grupos de [3] [5] [6] [ ]
    elif line1 == (1,0,0,0) and line2 == (1,1,1,0): #ceros en [3] , [5] , [6] , [7]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [4],[8]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + PR")

    elif line1 == (1,0,1,0) and line2 == (1,1,0,0): #ceros en [3] , [5] , [6] , [8]
        print("Grupo de 1 = [7]")
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [2],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + P'QR + PQ'")

#Grupos de [3] [5] [7] [ ]
    elif line1 == (1,0,0,0) and line2 == (1,1,0,1): #ceros en [3] , [5] , [7] , [8]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [2],[4]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = Q'R' + PQ' + PR'")

#Grupos de [3] [6] [7] [ ]
    elif line1 == (1,0,0,1) and line2 == (1,1,0,0): #ceros en [3] , [6] , [7] , [8]
        print("Grupo de 2 = [5],[1]")
        print("Grupo de 2 = [2],[4]")
        print("Funcion simplificada, S(P, Q, R) = P'R' + PQ'")
#Grupos de [3] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [4] [ ] [ ] [ ]
#Grupos de [4] [5] [6] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,0,1,0): #ceros en [4] , [5] , [6] , [7]
        print("Grupo de 1 = [8]")
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [1],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + Q'R' + PQR")

    elif line1 == (1,1,1,0) and line2 == (1,0,0,0): #ceros en [4] , [5] , [6] , [8]
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [3],[7]")
        print("Funcion simplificada, S(P, Q, R) = P'R + Q'R'")

#Grupos de [4] [5] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,0,0,1): #ceros en [4] , [5] , [7] , [8]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [6],[2]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + PR'")

#Grupos de [4] [6] [7] [ ]
    elif line1 == (1,1,0,1) and line2 == (1,0,0,0): #ceros en [4] , [6] , [7] , [8]
        print("Grupo de 2 = [1],[3]")
        print("Grupo de 2 = [1],[2]")
        print("Grupo de 2 = [5],[1]")
        print("Funcion simplificada, S(P, Q, R) = P'Q' + P'R' + Q'R'")
#Grupos de [4] [6] [8] [ ] ya están incluidos en las anteriores

#Grupos de [5] [ ] [ ] [ ]
#Grupos de [5] [6] [7] [ ]
    elif line1 == (1,1,0,0) and line2 == (1,1,0,0): #ceros en [5] , [6] , [7] , [8]
        print("Grupo de 4 = [1],[2],[3],[4]")
        print("Funcion simplificada, S(P, Q, R) = Q'")
#Grupos de [5] [7] [ ] [ ] ya están incluidos en las anteriores

#No hay grupos de [6] [ ] [ ] [ ], [7] [ ] [ ] [ ], [8] [ ] [ ] [ ] porque ya están dentro de las anteriores

# Grupos de 3 de 1 - TODO IMPLEMENTAR EL RESTO DE 3
#de tres unos-------------------------------------------
     #juntos
    elif line1 == (1,1,1,0) and line2 == (0,0,0,0):
         print("Grupo de 2 = [1],[3]")
         print("Grupo de 2 = [3],[5]")
         print("Funcion simplificada, f(P , Q, R) = P'Q' + P'R ")
    elif line1 == (0,1,1,1) and line2 == (0,0,0,0):
         print("Grupo de 2 = [3],[7]")
         print("Grupo de 2 = [7],[5]")
         print("Funcion simplificada, f(P , Q, R) = P'R + P'Q ")
    elif line1 == (0,0,0,0) and line2 == (1,1,1,0):
         print("Grupo de 2 = [2],[4]")
         print("Grupo de 2 = [4],[8]")
         print("Funcion simplificada, f(P , Q, R) = PQ' + PR ")
    elif line1 == (0,0,0,0) and line2 == (0,1,1,1):
         print("Grupo de 2 = [4],[8]")
         print("Grupo de 2 = [8],[6]")
         print("Funcion simplificada, f(P , Q, R) = PR + PQ ")
    #en forma ed L normal
    elif line1 == (1,0,0,0) and line2 == (1,1,0,0):
         print("Grupo de 2 = [1],[2]")
         print("Grupo de 2 = [2],[4]")
         print("Funcion simplificada, f(P , Q, R) = Q'R' + PQ' ")
    elif line1 == (0,1,0,0) and line2 == (0,1,1,0):
         print("Grupo de 2 = [3],[4]")
         print("Grupo de 2 = [4],[8]")
         print("Funcion simplificada, f(P , Q, R) = Q'R + PR ")
    elif line1 == (0,0,1,0) and line2 == (0,0,1,1):
         print("Grupo de 2 = [7],[8]")
         print("Grupo de 2 = [8],[6]")
         print("Funcion simplificada, f(P , Q, R) = QR + PQ ")
    elif line1 == (0,0,0,1) and line2 == (0,0,1,1):
         print("Grupo de 2 = [5],[6]")
         print("Grupo de 2 = [8],[6]")
         print("Funcion simplificada, f(P , Q, R) = QR' + PQ ")
    elif line1 == (0,0,1,0) and line2 == (0,1,1,0):
         print("Grupo de 2 = [7],[8]")
         print("Grupo de 2 = [4],[8]")
         print("Funcion simplificada, f(P , Q, R) = QR + PR ")
    elif line1 == (0,1,0,0) and line2 == (1,1,0,0):
         print("Grupo de 2 = [3],[4]")
         print("Grupo de 2 = [2],[4]")
         print("Funcion simplificada, f(P , Q, R) = Q'R + PQ' ")
    #en forma ed L invertida
    elif line1 == (1,1,0,0) and line2 == (1,0,0,0):
         print("Grupo de 2 = [1],[3]")
         print("Grupo de 2 = [1],[2]")
         print("Funcion simplificada, f(P , Q, R) = P'Q' + Q'R' ")
    elif line1 == (0,1,1,0) and line2 == (0,1,0,0):
         print("Grupo de 2 = [3],[4]")
         print("Grupo de 2 = [3],[7]")
         print("Funcion simplificada, f(P , Q, R) = P'R + Q'R ")
    elif line1 == (0,0,1,1) and line2 == (0,0,1,0):
         print("Grupo de 2 = [7],[5]")
         print("Grupo de 2 = [7],[8]")
         print("Funcion simplificada, f(P , Q, R) = P'Q + QR ")
    elif line1 == (0,0,1,1) and line2 == (0,0,0,1):
         print("Grupo de 2 = [7],[5]")
         print("Grupo de 2 = [5],[6]")
         print("Funcion simplificada, f(P , Q, R) = P'Q + QR' ")
    elif line1 == (0,1,1,0) and line2 == (0,0,1,0):
         print("Grupo de 2 = [3],[7]")
         print("Grupo de 2 = [7],[8]")
         print("Funcion simplificada, f(P , Q, R) =  P'R + QR ")
    elif line1 == (1,1,0,0) and line2 == (0,1,0,0):
         print("Grupo de 2 = [1],[3]")
         print("Grupo de 2 = [3],[4]")
         print("Funcion simplificada, f(P , Q, R) = P'Q' + Q'R ")
 #en forma ed L con espacio---I--
  #----------------------------II
    elif line1 == (1,0,0,0) and line2 == (0,1,1,0):
         print("Grupo de 1 = [1]")
         print("Grupo de 2 = [4],[8]")
         print("Funcion simplificada, f(P , Q, R) =  P'Q'R' + PR ")
    elif line1 == (0,1,0,0) and line2 == (0,0,1,1):
         print("Grupo de 1 = [3]")
         print("Grupo de 2 = [8],[6]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R + PQ ")
    elif line1 == (0,0,0,1) and line2 == (0,1,1,0):
         print("Grupo de 1 = [5]")
         print("Grupo de 2 = [4],[8]")
         print("Funcion simplificada, f(P , Q, R) = P'QR' + PR ")
    elif line1 == (0,0,1,0) and line2 == (1,1,0,0):
         print("Grupo de 1 = [7]")
         print("Grupo de 2 = [2],[4]")
         print("Funcion simplificada, f(P , Q, R) = P'QR + PQ' ")
  #en forma ed L con espacio---I-- inversas
  #---------------------------- II       
    elif line1 == (1,1,0,0) and line2 == (0,0,1,0):
         print("Grupo de 1 = [8]")
         print("Grupo de 2 = [1],[3]")
         print("Funcion simplificada, f(P , Q, R) =  P'Q' + PQR ")
    elif line1 == (0,1,1,0) and line2 == (0,0,0,1):
         print("Grupo de 1 = [6]")
         print("Grupo de 2 = [3],[7]")
         print("Funcion simplificada, f(P , Q, R) = P'R + PQR' ")
    elif line1 == (0,0,1,1) and line2 == (0,1,0,0):
         print("Grupo de 1 = [4]")
         print("Grupo de 2 = [7],[5]")
         print("Funcion simplificada, f(P , Q, R) = P'Q + PQ'R ")
    elif line1 == (0,1,1,0) and line2 == (1,0,0,0):
         print("Grupo de 1 = [2]")
         print("Grupo de 2 = [3],[7]")
         print("Funcion simplificada, f(P , Q, R) = P'R + PQ'R' ")
 #en forma ed L con doble espacio---I--
  #----------------------------     --II 

    elif line1 == (1,1,0,0) and line2 == (0,0,0,1):
         print("Grupo de 1 = [6]")
         print("Grupo de 2 = [1],[3]")
         print("Funcion simplificada, f(P , Q, R) =  P'Q' + PQR' ")
    elif line1 == (0,0,1,1) and line2 == (1,0,0,0):
         print("Grupo de 1 = [2]")
         print("Grupo de 2 = [7],[5]")
         print("Funcion simplificada, f(P , Q, R) = P'Q + PQ'R' ")
    elif line1 == (0,0,0,1) and line2 == (1,1,0,0):
         print("Grupo de 1 = [5]")
         print("Grupo de 2 = [2],[4]")
         print("Funcion simplificada, f(P , Q, R) = P'QR' + PQ' ")
    elif line1 == (1,0,0,0) and line2 == (0,0,1,1):
         print("Grupo de 1 = [1]")
         print("Grupo de 2 = [8],[6]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R' + PQ ")
#especiales....en L
    elif line1 == (1,0,0,0) and line2 == (1,0,0,1):
         print("Grupo de 2 = [1],[2]")
         print("Grupo de 2 = [2],[6]")
         print("Funcion simplificada, f(P , Q, R) = Q'R' + PR' ")
    elif line1 == (1,0,0,1) and line2 == (1,0,0,0):
         print("Grupo de 2 = [1],[2]")
         print("Grupo de 2 = [1],[5]")
         print("Funcion simplificada, f(P , Q, R) = P'R' + Q'R' ")
    elif line1 == (1,0,0,1) and line2 == (0,0,0,1):
         print("Grupo de 2 = [1],[5]")
         print("Grupo de 2 = [5],[6]")
         print("Funcion simplificada, f(P , Q, R) = P'R' + QR' ")
    elif line1 == (0,0,0,1) and line2 == (1,0,0,1):
         print("Grupo de 2 = [2],[6]")
         print("Grupo de 2 = [5],[6]")
         print("Funcion simplificada, f(P , Q, R) = QR' + PR' ")
# separados los tres
    elif line1 == (1,0,1,0) and line2 == (0,1,0,0):
         print("Grupo de 1 = [1]")
         print("Grupo de 1 = [3]")
         print("Grupo de 1 = [4]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R' + P'QR + PQ'R ")
    elif line1 == (0,1,0,1) and line2 == (0,0,1,0):
         print("Grupo de 1 = [3]")
         print("Grupo de 1 = [8]")
         print("Grupo de 1 = [5]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R + P'QR' + PQR ")
    elif line1 == (0,1,0,0) and line2 == (1,0,1,0):
         print("Grupo de 1 = [3]")
         print("Grupo de 1 = [2]")
         print("Grupo de 1 = [8]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R + PQ'R' + PQR ")
    elif line1 == (0,0,1,0) and line2 == (0,1,0,1):
         print("Grupo de 1 = [7]")
         print("Grupo de 1 = [4]")
         print("Grupo de 1 = [6]")
         print("Funcion simplificada, f(P , Q, R) = P'QR + PQ'R + PQR' ")

# Grupos de 2 de 1
#------------juntos
    elif line1 == (1,1,0,0) and line2 == (0,0,0,0):
         print("Grupo de 2 = [1],[3]")
         print("Funcion simplificada, f(P , Q, R) = P'Q' ")
    elif line1 == (0,1,1,0) and line2 == (0,0,0,0):
         print("Grupo de 2 = [3],[7]")
         print("Funcion simplificada, f(P , Q, R) =  P'R ")
    elif line1 == (0,0,1,1) and line2 == (0,0,0,0):
         print("Grupo de 2 = [7],[5]")
         print("Funcion simplificada, f(P , Q, R) = P'Q ")
    elif line1 == (0,0,0,0) and line2 == (1,1,0,0):
         print("Grupo de 2 = [2],[4]")
         print("Funcion simplificada, f(P , Q, R) = PQ'")
    elif line1 == (0,0,0,0) and line2 == (0,1,1,0):
         print("Grupo de 2 = [4],[8]")
         print("Funcion simplificada, f(P , Q, R) = PR ")
    elif line1 == (0,0,0,0) and line2 == (0,0,1,1):
         print("Grupo de 2 = [8],[6]")
         print("Funcion simplificada, f(P , Q, R) = PQ ")
         #---------
    elif line1 == (1,0,0,0) and line2 == (1,0,0,0):
         print("Grupo de 2 = [1],[2]")
         print("Funcion simplificada, f(P , Q, R) = Q'R' ")
    elif line1 == (0,1,0,0) and line2 == (0,1,0,0):
         print("Grupo de 2 = [3],[4]")
         print("Funcion simplificada, f(P , Q, R) = Q'R")
    elif line1 == (0,0,1,0) and line2 == (0,0,1,0):
         print("Grupo de 2 = [7],[8]")
         print("Funcion simplificada, f(P , Q, R) = QR ")
    elif line1 == (0,0,0,1) and line2 == (0,0,0,1):
         print("Grupo de 2 = [5],[6]")
         print("Funcion simplificada, f(P , Q, R) = QR' ")
         #---------intercalados
    elif line1 == (1,0,0,0) and line2 == (0,1,0,0):
         print("Grupo de 1 = [1]")
         print("Grupo de 1 = [4]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R' + PQ'R ")
    elif line1 == (0,1,0,0) and line2 == (0,0,1,0):
         print("Grupo de 1 = [3]")
         print("Grupo de 1 = [8]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R + PQR ")
    elif line1 == (0,0,1,0) and line2 == (0,0,0,1):
         print("Grupo de 1 = [7]")
         print("Grupo de 1 = [6]")
         print("Funcion simplificada, f(P , Q, R) = P'QR + PQR' ")
         #---------
    elif line1 == (0,1,0,0) and line2 == (1,0,0,0):
         print("Grupo de 1 = [3]")
         print("Grupo de 1 = [2]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R + PQ'R' ")
    elif line1 == (0,0,1,0) and line2 == (0,1,0,0):
         print("Grupo de 1 = [7]")
         print("Grupo de 1 = [4]")
         print("Funcion simplificada, f(P , Q, R) = P'QR + PQ'R ")
    elif line1 == (0,0,0,1) and line2 == (0,0,1,0):
         print("Grupo de 1 = [8]")
         print("Grupo de 1 = [5]")
         print("Funcion simplificada, f(P , Q, R) = P'QR' + PQR ")
         #---------
    elif line1 == (1,0,1,0) and line2 == (0,0,0,0):
         print("Grupo de 1 = [1]")
         print("Grupo de 1 = [7]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R' + P'QR ")
    elif line1 == (0,1,0,1) and line2 == (0,0,0,0):
         print("Grupo de 1 = [3]")
         print("Grupo de 1 = [5]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R + P'QR' ")
    elif line1 == (0,0,0,0) and line2 == (1,0,1,0):
         print("Grupo de 1 = [2]")
         print("Grupo de 1 = [4]")
         print("Funcion simplificada, f(P , Q, R) = PQ'R' + PQR ")        
    elif line1 == (0,0,0,0) and line2 == (0,1,0,1):
         print("Grupo de 1 = [8]")
         print("Grupo de 1 = [6]")
         print("Funcion simplificada, f(P , Q, R) = PQ'R + PQR' ")
     #---------intercal de doble espacio
    elif line1 == (1,0,0,0) and line2 == (0,0,1,0):
         print("Grupo de 1 = [1]")
         print("Grupo de 1 = [8]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R' + PQR ")
    elif line1 == (0,1,0,0) and line2 == (0,0,0,1):
         print("Grupo de 1 = [3]")
         print("Grupo de 1 = [6]")
         print("Funcion simplificada, f(P , Q, R) = P'Q'R + PQR' ")
    elif line1 == (0,0,1,0) and line2 == (1,0,0,0):
         print("Grupo de 1 = [7]")
         print("Grupo de 1 = [2]")
         print("Funcion simplificada, f(P , Q, R) = P'QR + PQ'R' ")
    elif line1 == (0,0,0,1) and line2 == (0,1,0,0):
         print("Grupo de 1 = [5]")
         print("Grupo de 1 = [4]")
         print("Funcion simplificada, f(P , Q, R) = P'QR' + PQ'R ")
     #--------Esquinas  
    elif line1 == (0,0,0,1) and line2 == (1,0,0,0):
         print("Grupo de 1 = [5]")
         print("Grupo de 1 = [2]")
         print("Funcion simplificada, f(P , Q, R) = P'QR' + PQ'R' ")
    elif line1 == (1,0,0,0) and line2 == (0,0,0,1):
         print("Grupo de 1 = [1]")
         print("Grupo de 1 = [6]")
         print("Funcion simplificada, f(P , Q, R) =P'Q'R' + PQR' ")
     #--------Especiales
    elif line1 == (1,0,0,1) and line2 == (0,0,0,0):
         print("Grupo de 2 = [1],[5]")
         print("Funcion simplificada, f(P , Q, R) = P'R' ")   
    elif line1 == (0,0,0,0) and line2 == (1,0,0,1):
         print("Grupo de 2 = [2],[6]")
         print("Funcion simplificada, f(P , Q, R) = PR' ")

# Grupos de 1 de 1
    elif line1 == (1,0,0,0) and line2 == (0,0,0,0):  #caso en [1]
        print("Grupo de 1 = [1]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R'")

    elif line1 == (0,0,0,0) and line2 == (1,0,0,0):  #caso en [2]
        print("Grupo de 1 = [2]")
        print("Funcion simplificada, S(P, Q, R) = PQ'R'")

    elif line1 == (0,1,0,0) and line2 == (0,0,0,0):  #caso en [3]
        print("Grupo de 1 = [3]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R")

    elif line1 == (0,0,0,0) and line2 == (0,1,0,0):  #caso en [4]
        print("Grupo de 1 = [4]")
        print("Funcion simplificada, S(P, Q, R) = PQ'R")

    elif line1 == (0,0,0,1) and line2 == (0,0,0,0):  #caso en [5]
        print("Grupo de 1 = [5]")
        print("Funcion simplificada, S(P, Q, R) = P'QR'")

    elif line1 == (0,0,0,0) and line2 == (0,0,0,1):  #caso en [6]
        print("Grupo de 1 = [6]")
        print("Funcion simplificada, S(P, Q, R) = P'Q'R")

    elif line1 == (0,0,1,0) and line2 == (0,0,0,0):  #caso en [7]
        print("Grupo de 1 = [7]")
        print("Funcion simplificada, S(P, Q, R) = P'QR")

    elif line1 == (0,0,0,0) and line2 == (0,0,1,0):  #caso en [8]
        print("Grupo de 1 = [8]")
        print("Funcion simplificada, S(P, Q, R) = PQR") 



