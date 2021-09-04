from colorama import Fore, Back, Style

def tabla2(listing):
    print(Fore.RED + " P  Q ")
    print("------|")
    print(Fore.RESET +" 0  0 " + Fore.RED + "| [1]")
    print(Fore.RESET +" 0  1 " + Fore.RED + "| [2]")
    print(Fore.RESET +" 1  0 " + Fore.RED + "| [3]")
    print(Fore.RESET +" 1  1 " + Fore.RED + "| [4]")

    posib =  4
    var =  " "

    for i in range (0, posib):
        print(Fore.RESET + "Variables para " + Fore.RED + "[ ", i ," ]" + Fore.RESET);
        listing.append(int(input(var)))

    return listing


def k2v(listing):
    posib = 4
    var = " "
    line1 = ()
    line2 = ()

    line1 = (listing[0], listing[1])
    line2 = (listing[2], listing[3])

    print("\n")

    print(Fore.LIGHTYELLOW_EX + "  P \ Q      0      1")
    print("         |---------------")
    print("    0    |  ", listing[0] ,"  |  ",listing[1]," |")
    print("         |---------------")
    print("    1    |  ", listing[2] ,"  |  ",listing[3]," |")

    print("\n")

    print(Fore.LIGHTBLUE_EX + "  P \ Q      0      1")
    print("         |---------------")
    print("    0    |  [1]  |  [2]  |")
    print("         |---------------")
    print("    1    |  [3]  |  [4]  |")

    print("\n" + Fore.WHITE)

# Para todos ceros 
    if line1 == (0, 0) and line2 == (0, 0):
        print("No hay grupos")
        print("Funcion simplificada, S(P, Q) = 0")

# Para todos unos
    elif line1 == (1, 1) and line2 == (1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Funcion simplificada, S(P, Q) = 1")

# Para tres unos
    elif line1 == (0, 1) and line2 == (1, 1):
        print("Grupo de 2 = { [3], [4] }")
        print("Grupo de 2 = { [2], [4] }")
        print("Funcion simplificada, S(P, Q) = Q + P")
    elif line1 == (1, 0) and line2 == (1, 1):
        print("Grupo de 2 = { [1], [3] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, S(P, Q) = Q' + P")
    elif line1 == (1, 1) and line2 == (0, 1):
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 2 = { [2], [4] }")
        print("Funcion simplificada, S(P, Q) = P' + Q")
    elif line1 == (1, 1) and line2 == (1, 0):
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 2 = { [1], [3] }")
        print("Funcion simplificada, S(P, Q) = P' + Q'")

# Para dos unos - adj 
    elif line1 == (1, 1) and line2 == (0, 0):
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, S(P, Q) = P'")
    elif line1 == (0, 0) and line2 == (1, 1):
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, S(P, Q) = P")
    elif line1 == (1, 0) and line2 == (1, 0):
        print("Grupo de 2 = { [1], [3] }")
        print("Funcion simplificada, S(P, Q) = Q'")
    elif line1 == (0, 1) and line2 == (0, 1):
        print("Grupo de 2 = { [2], [4] }")
        print("Funcion simplificada, S(P, Q) = Q")

# Para dos unos - sep 
    elif line1 == (1, 0) and line2 == (0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, S(P, Q) = P'Q' + PQ")
    elif line1 == (0, 1) and line2 == (0, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, S(P, Q) = P'Q + PQ'")

# Para unos
    elif line1 == (1, 0) and line2 == (0, 0):
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, S(P, Q) = P'Q'")
    elif line1 == (0, 1) and line2 == (0, 0):
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, S(P, Q) = P'Q")
    elif line1 == (0, 0) and line2 == (1, 0):
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, S(P, Q) = P'Q")
    elif line1 == (0, 0) and line2 == (0, 1):
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, S(P, Q) = PQ")

    print("\n")
