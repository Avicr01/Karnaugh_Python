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
        while var != 0 and var != 1:
            print(Fore.RESET + "Variables para " + Fore.RED + "[ ", i ," ]" + Fore.RESET);
            var = int(input())
        listing.append(var)
        var = " "

    return listing


def kmaps2(listing, label):
    posib = 4
    var = " "
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
        label+="No hay grupos\n"
        label+="Funcion simplificada, S(P, Q) = 0\n"

# Para todos unos
    elif line1 == (1, 1) and line2 == (1, 1):
        label+="Grupo de 4 = { [1], [2], [3], [4] }\n"
        label+="Funcion simplificada, S(P, Q) = 1\n"

# Para tres unos
    elif line1 == (0, 1) and line2 == (1, 1):
        label+="Grupo de 2 = { [3], [4] }\n"
        label+="Grupo de 2 = { [2], [4] }\n"
        label+="Funcion simplificada, S(P, Q) = Q + P\n"
    elif line1 == (1, 0) and line2 == (1, 1):
        label+="Grupo de 2 = { [1], [3] }\n"
        label+="Grupo de 2 = { [3], [4] }\n"
        label+="Funcion simplificada, S(P, Q) = Q' + P\n"
    elif line1 == (1, 1) and line2 == (0, 1):
        label+="Grupo de 2 = { [1], [2] }\n"
        label+="Grupo de 2 = { [2], [4] }\n"
        label+="Funcion simplificada, S(P, Q) = P' + Q\n"
    elif line1 == (1, 1) and line2 == (1, 0):
        label+="Grupo de 2 = { [1], [2] }\n"
        label+="Grupo de 2 = { [1], [3] }\n"
        label+="Funcion simplificada, S(P, Q) = P' + Q'\n"

# Para dos unos - adj 
    elif line1 == (1, 1) and line2 == (0, 0):
        label+="Grupo de 2 = { [1], [2] }\n"
        label+="Funcion simplificada, S(P, Q) = P'\n"
    elif line1 == (0, 0) and line2 == (1, 1):
        label+="Grupo de 2 = { [3], [4] }\n"
        label+="Funcion simplificada, S(P, Q) = P\n"
    elif line1 == (1, 0) and line2 == (1, 0):
        label+="Grupo de 2 = { [1], [3] }\n"
        label+="Funcion simplificada, S(P, Q) = Q'\n"
    elif line1 == (0, 1) and line2 == (0, 1):
        label+="Grupo de 2 = { [2], [4] }\n"
        label+="Funcion simplificada, S(P, Q) = Q\n"

# Para dos unos - sep 
    elif line1 == (1, 0) and line2 == (0, 1):
        label+="Grupo de 1 = { [1] }\n"
        label+="Grupo de 1 = { [4] }\n"
        label+="Funcion simplificada, S(P, Q) = P'Q' + PQ\n"
    elif line1 == (0, 1) and line2 == (1, 0):
        label+="Grupo de 1 = { [2] }\n"
        label+="Grupo de 1 = { [3] }\n"
        label+="Funcion simplificada, S(P, Q) = P'Q + PQ'\n"

# Para unos
    elif line1 == (1, 0) and line2 == (0, 0):
        label+="Grupo de 1 = { [1] }\n"
        label+="Funcion simplificada, S(P, Q) = P'Q'\n"
    elif line1 == (0, 1) and line2 == (0, 0):
        label+="Grupo de 1 = { [2] }\n"
        label+="Funcion simplificada, S(P, Q) = P'Q\n"
    elif line1 == (0, 0) and line2 == (1, 0):
        label+="Grupo de 1 = { [3] }\n"
        label+="Funcion simplificada, S(P, Q) = P'Q\n"
    elif line1 == (0, 0) and line2 == (0, 1):
        label+="Grupo de 1 = { [4] }\n"
        label+="Funcion simplificada, S(P, Q) = PQ\n"

    return label