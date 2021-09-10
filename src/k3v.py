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
    listing = [ ]
    var = " "
    for i in range (0,7):
      print("variables para [", i , "]");
      listing.append(int(input(var)))
    return listing
 

#Para todos los ceros
def k3v (listing):
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
    
    line1 = ()
    line2 = ()
    line1 = (listing[0],listing[2],listing[6],listing[4])
    line2 = (listing[1],listing[3],listing[7],listing[5])
    # Todos de 0
    if line1 == (0, 0, 0, 0) and line2 == (0, 0, 0, 0):
        print("No hay grupos")
        print("Funcion simplificada, S( P , Q , R )  = 0")

    # Todos de 1
    elif line1 == (1, 1, 1, 1) and line2 == (1, 1, 1, 1):
        print("Grupo de 8 = [1], [2], [3], [4], [5], [6], [7], [8]")
        print("Funcion simplificada, S( P , Q , R )  = 1")

    # Grupos de 7 de 1
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
# Grupos de 6 de 1
# Grupos de 5 de 1
# Grupos de 4 de 1
# Grupos de 3 de 1
# Grupos de 2 de 1
# Grupos de 1 de 1
    elif line1 == (1,0,0,0) and line2 == (0,0,0,0):
        print("Grupo de 1 = [1]")
        print("Funcion simplificada, f(P, Q, R) = P'Q'R'")





