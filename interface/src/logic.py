#Karnaugh Map Minimization with a Graphical User Interface provided by Tkinter.
#Developed by Mouzakitis Nikolaos,Crete,2016-2017.

from tkinter import *

global mlist
tvar = StringVar
tvar = ""
lh = 2
lw = 2
m1 = None
m2 = None
m3 = None
m4 = None
m5 = None
m6 = None
m7 = None
m8 = None
m9 = None
m10 = None
m11 = None
m12= None
m13 = None
m14 = None
m15 = None
m16 = None
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt9 = 0
cnt10 = 0
cnt11 = 0
cnt12 = 0
cnt13 = 0
cnt14 = 0
cnt15 = 0
cnt16= 0

def minimization(k):
    global la

    mini = []
    combo = []

    multicombo2 = [] #usado para resolver los bug las combinaciones sobrepuestas, para que tenga la mejor minimizacion
    multicombo4 = []

    zero_cnt = 0
    prod = 1
    appended = 0  # usado para contar el numero de veces que aplicamos cuadrados en el mapa

    for i in range(0, 16):

        prod *= k[i]

        if (k[i] == 0):

            zero_cnt += 1

    if (prod == 1):

        print("F(P,Q,R,S) = 1\n")
        la = "F = 1"
        return

    if (zero_cnt == 16):

        print("F(P,Q,R,S) = 0\n")
        la = "F = 0"
        return

    for i in range(0, 16):

        combo_value = 0  # funciona como una bandera para saber la mayor cantidad de cuadrados para cada termino medio que combinamos
        combo_flag = 0

        if (k[i] == 0):

            combo.append(0)
            combo_flag = 1

        else:

            for j in range(0, 4):

                if (combo_value > 8):

                    break

                if (k[i] and k[driver_8[i][j][0] + i] and k[driver_8[i][j][1] + i] and k[driver_8[i][j][2] + i] and k[
                        driver_8[i][j][3] + i] and k[driver_8[i][j][4] + i] and k[driver_8[i][j][5] + i] and k[
                        driver_8[i][j][6] + i]):

                    combo_value = 8
                    combo.append(8)
                    combo_flag = 1
                    break

            for j in range(0, 6):

                if (combo_value > 4):

                    break

                if ((k[i] and k[driver_4[i][j][0] + i] and k[driver_4[i][j][1] + i] and k[driver_4[i][j][2] + i])):

                    combo_value = 4
                    combo.append(4)
                    combo_flag = 1
                    break

            for j in range(0, 4):

                if ((k[i] and k[i + driver_2[i][j]])):

                    if (combo_value > 2):

                        break

                    else:

                        combo.append(2)
                        combo_flag = 1

                        break

            if (combo_flag == 0):

                combo.append(1)

# creando multicombo2 y multicombo4 conteniendo la cantidad de diferentes combinaciones de 2 y 4 que los terminos medios pueden tener.

    # Evaluas los multicombos
    for i in range(0, 16):
        multicombo2_cnt = 0
        multicombo4_cnt = 0

        combo_value = 0  # funciona como una bandera para saber la mayor cantidad de cuadrados para cada termino medio que combinamos
        combo_flag = 0

        if (k[i] == 0):

            combo_flag = 1
            multicombo2.append(0)
            multicombo4.append(0)
        else:

            for j in range(0, 4):

                if (combo_value > 8):
                    break

                if (k[i] and k[driver_8[i][j][0] + i] and k[driver_8[i][j][1] + i] and k[
                                driver_8[i][j][2] + i] and k[
                                driver_8[i][j][3] + i] and k[driver_8[i][j][4] + i] and k[driver_8[i][j][5] + i] and k[
                                driver_8[i][j][6] + i]):
                    combo_value = 8
                    #combo.append(8)
                    combo_flag = 1


            for j in range(0, 6):

                if (combo_value > 4):
                    break

                if (k[i] and k[driver_4[i][j][0] + i] and k[driver_4[i][j][1] + i] and k[driver_4[i][j][2] + i]):
                    combo_value = 4
                    multicombo4_cnt += 1
                    combo_flag = 1


            for j in range(0, 4):

                if ((k[i] and k[i + driver_2[i][j]])):

                    if (combo_value > 2):

                        break

                    else:
                        multicombo2_cnt +=1
                        combo_flag = 1



            multicombo2.append(multicombo2_cnt)
            multicombo4.append(multicombo4_cnt)




                # Calculando los aces libres en el mapa y la posicion con el mas grande valor combinable
                # los aces libres no son en realidad aces libres, pero lo son solo en el inicio del programa

    print(multicombo4)
    already_combined = []
    already_combined = combo
    free_aces = 0
    for element in k:

        if (element == 1):

            free_aces += 1

    k_max = combo[0]
    max_thesis = 0

    for i in range(0, 16):

        if (combo[i] > k_max):

            k_max = combo[i]
            max_thesis = i

    if (k_max == 1):

        print("No hay minimizacion para esta funcion.")
        la = "No es posible minimizarla"
        return
    

    # El codigo de la minimizacion procede desde aqui
    map_copy = k
    solution = ""
    timer = 0

    for t in range(0,16):       # priminimizacion combinando los terminos medios con el menos valor en multicombo2 en primer lugar
        if (multicombo2[t] == 1):               # ya que no se pueden combinar de otra manera

            for j in range(0, 4):

                if ((k[t] and k[t + driver_2[t][j]]) and ((already_combined[t] != 0)  ) ):

                    duo = []
                    duo.append(t)
                    duo.append(t + driver_2[t][j])
                    duo.sort() # solo lo ordenas
                    print("Combinando los siguientes cuadrados: ", duo)
                    solution += solver(duo)
                    zero[t] = 1
                    zero[t + driver_2[t][j]] = 1
                    already_combined[duo[0]] = 0
                    already_combined[duo[1]] = 0
                    free_aces -= 2
                    break

    for t in range(0,16):
        if (multicombo2[t] == 2):

            for j in range(0, 4):

                # Si ya esta combinado
                if ((k[t] and k[t + driver_2[t][j]]) and ((already_combined[t] != 0) and (already_combined[t+driver_2[t][j]] != 0 ) ) ):

                    duo = []
                    duo.append(t)
                    duo.append(t + driver_2[t][j])
                    duo.sort()
                    print("Combinando los siguientes cuadrados: ", duo)
                    solution += solver(duo)
                    zero[t] = 1
                    zero[t + driver_2[t][j]] = 1
                    already_combined[duo[0]] = 0
                    already_combined[duo[1]] = 0
                    free_aces -= 2
                    break


    for t in range(0,16):

        if(multicombo4[t] == 1):
            for j in range(0, 6):

                if ((k[t] and k[driver_4[t][j][0] + t] and k[driver_4[t][j][1] + t] and k[driver_4[t][j][2] + t] and (already_combined[t] != 0)  )):

                    quatro = []
                    mini.append(
                        [t, driver_4[t][j][0] + t, driver_4[t][j][1] + t,
                         driver_4[t][j][2] + t])
                    appended += 1
                    quatro.append(t)
                    quatro.append(driver_4[t][j][0] + t)
                    quatro.append(driver_4[t][j][1] + t)
                    quatro.append(driver_4[t][j][2] + t)
                    print("se combinan los siguientes cuadrados: ", quatro)
                    print("Ya esta combinado: ",already_combined)
                    quatro.sort()
                    solution += solver(quatro)
                    zero[t] = 1
                    zero[driver_4[t][j][0] + t] = 1
                    zero[driver_4[t][j][1] + t] = 1
                    zero[driver_4[t][j][2] + t] = 1
                    already_combined[quatro[0]] = 0
                    already_combined[quatro[1]] = 0
                    already_combined[quatro[2]] = 0
                    already_combined[quatro[3]] = 0
                    free_aces -= 4
                    break

    for xl in range(2,6):

        for t in range(0, 16):

            if (multicombo4[t] == xl):

                for j in range(0, 6):
                
                    if ((k[t] and k[driver_4[t][j][0] + t] and k[driver_4[t][j][1] + t] and  k[driver_4[t][j][2] + t] and ( (already_combined[t] != 0) ^ (already_combined[driver_4[t][j][0] + t] != 0) ^ (already_combined[driver_4[t][j][1] + t] != 0) ^ (already_combined[driver_4[t][j][2] + t] != 0)  ))):

                        quatro = []
                        mini.append(
                        [t, driver_4[t][j][0] + t, driver_4[t][j][1] + t,
                         driver_4[t][j][2] + t])
                        appended += 1
                        quatro.append(t)
                        quatro.append(driver_4[t][j][0] + t)
                        quatro.append(driver_4[t][j][1] + t)
                        quatro.append(driver_4[t][j][2] + t)
                        print("se combinan los siguientes cuadrados: ", quatro)
                        quatro.sort()
                        solution += solver(quatro)
                        zero[t] = 1
                        zero[driver_4[t][j][0] + t] = 1
                        zero[driver_4[t][j][1] + t] = 1
                        zero[driver_4[t][j][2] + t] = 1
                        already_combined[quatro[0]] = 0
                        already_combined[quatro[1]] = 0
                        already_combined[quatro[2]] = 0
                        already_combined[quatro[3]] = 0
                        free_aces -= 4
                        print("Ya esta combinado: ",already_combined)
                        break



    while (max(already_combined) >= 1):

        print("\nLA MINIMIZACION CORRE\n")
        print(combo)
        for i in range(0, 16):
             if (   (combo[i] == 2 )   and (timer > 2)   ):

                for j in range(0, 4):

                    if ((k[i] and k[i + driver_2[i][j]]) and (already_combined[i] != 0) and zero[i + driver_2[i][j]] == 0 ):

                        duo = []
                        duo.append(i)
                        duo.append(i + driver_2[i][j])
                        duo.sort()
                        print("Combining the following squares: ", duo)
                        solution += solver(duo)
                        zero[i] = 1
                        zero[i + driver_2[i][j]] = 1
                        already_combined[duo[0]] = 0
                        already_combined[duo[1]] = 0
                        free_aces -= 2

             elif (combo[i] == 1):

                solution += solver([i])
                already_combined[i] = 0

        if (k_max == 8):  # minimization for eight squares combination.

            for j in range(0, 4):

                if (map_copy[max_thesis] and map_copy[driver_8[max_thesis][j][0] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][1] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][2] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][3] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][4] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][5] + max_thesis] and map_copy[driver_8[max_thesis][j][6] + max_thesis]):

                    octo = []
                    octo.append(max_thesis)
                    octo.append(driver_8[max_thesis][j][0] + max_thesis)
                    octo.append(driver_8[max_thesis][j][1] + max_thesis)
                    octo.append(driver_8[max_thesis][j][2] + max_thesis)
                    octo.append(driver_8[max_thesis][j][3] + max_thesis)
                    octo.append(driver_8[max_thesis][j][4] + max_thesis)
                    octo.append(driver_8[max_thesis][j][5] + max_thesis)
                    octo.append(driver_8[max_thesis][j][6] + max_thesis)
                    octo.sort()
                    print("Combining the following squares  :", octo)
                    solution += solver(octo)
                    zero[max_thesis] = 1
                    zero[driver_8[max_thesis][j][0] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][1] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][2] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][3] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][4] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][5] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][6] + max_thesis] = 1
                    already_combined[octo[0]] = 0
                    already_combined[octo[1]] = 0
                    already_combined[octo[2]] = 0
                    already_combined[octo[3]] = 0
                    already_combined[octo[4]] = 0
                    already_combined[octo[5]] = 0
                    already_combined[octo[6]] = 0
                    already_combined[octo[7]] = 0
                    free_aces -= 8
                    break

        elif (k_max == 2):  # minimization for two squares combination.




            for j in range(0, 4):


                if ((map_copy[max_thesis] and map_copy[max_thesis + driver_2[max_thesis][j]]) and ((already_combined[max_thesis] != 0)  ) ):


                    duo = []
                    duo.append(max_thesis)
                    duo.append(max_thesis + driver_2[max_thesis][j])
                    duo.sort()
                    print("Combining the following squares: ", duo)
                    solution += solver(duo)
                    zero[max_thesis] = 1
                    zero[max_thesis + driver_2[max_thesis][j]] = 1
                    already_combined[duo[0]] = 0
                    already_combined[duo[1]] = 0
                    free_aces -= 2
                    break

        elif (k_max == 4):  # minimization for four squares combination.

            for j in range(0, 6):

                if ((map_copy[max_thesis] and map_copy[driver_4[max_thesis][j][0] + max_thesis] and map_copy[
                        driver_4[max_thesis][j][1] + max_thesis] and map_copy[
                        driver_4[max_thesis][j][2] + max_thesis])):

                    quatro = []
                    mini.append(
                        [max_thesis, driver_4[max_thesis][j][0] + max_thesis, driver_4[max_thesis][j][1] + max_thesis,
                         driver_4[max_thesis][j][2] + max_thesis])
                    appended += 1
                    quatro.append(max_thesis)
                    quatro.append(driver_4[max_thesis][j][0] + max_thesis)
                    quatro.append(driver_4[max_thesis][j][1] + max_thesis)
                    quatro.append(driver_4[max_thesis][j][2] + max_thesis)
                    print("Combining the following squares : ", quatro)
                    quatro.sort()
                    solution += solver(quatro)
                    zero[max_thesis] = 1
                    zero[driver_4[max_thesis][j][0] + max_thesis] = 1
                    zero[driver_4[max_thesis][j][1] + max_thesis] = 1
                    zero[driver_4[max_thesis][j][2] + max_thesis] = 1
                    already_combined[quatro[0]] = 0
                    already_combined[quatro[1]] = 0
                    already_combined[quatro[2]] = 0
                    already_combined[quatro[3]] = 0
                    free_aces -= 4
                    break


        if (max(already_combined) < 2):

            break

        timer += 1
        max_thesis = 0      # calculation of the new k_max and max_thesis
        k_max = already_combined[0]
        found_flag = 0

        for i in range(0, 16):

            if (zero[i] == 0):

                if (k_max < already_combined[i]):

                    k_max = already_combined[i]
                    max_thesis = i
                    found_flag = 1

            else:

                pass

        if (found_flag != 1):

            for i in range(0, 16):

                if (k_max < already_combined[i]):

                    k_max = already_combined[i]
                    max_thesis = i

                else:

                    pass

    print("\nMinimos resultados:\n\nF(P,Q,R,S)=", solution[:-2])
    la = solution[:-2]

def solver(arg):

    sol = ""

    if (len(arg) == 1):

        if(arg == [0]):
            sol += " P'Q'R'S' "
        elif (arg == [1]):
            sol += " P'Q'R'S "
        elif (arg == [2]):
            sol += " P'Q'RS' "
        elif (arg == [3]):
            sol += " P'Q'RS "
        elif (arg == [4]):
            sol += " P'QR'S' "
        elif (arg == [5]):
            sol += " P'QR'S "
        elif (arg == [6]):
            sol += " P'QRS' "
        elif (arg == [7]):
            sol += " P'QRS "
        elif (arg == [8]):
            sol += " PQ'R'S' "
        elif (arg == [9]):
            sol += " PQ'R'S "
        elif (arg == [10]):
            sol += " PQ'RS' "
        elif (arg == [11]):
            sol += " PQ'RS "
        elif (arg == [12]):
            sol += " PQR'S' "
        elif (arg == [13]):
            sol += " PQR'S "
        elif (arg == [14]):
            sol += " PQRS' "
        elif (arg == [15]):
            sol += " PQRS "

    if (len(arg) == 2 ):

        if(arg == [0,1]):
            sol += " P'Q'R' "
        elif(arg == [0,2]):
            sol += " P'Q'S' "
        elif arg == [0, 4]:
            sol += " P'R'S' "
        elif(arg == [0,8]):
            sol += " Q'R'S' "
        elif(arg == [1,3]):
            sol += " P'Q'S "
        elif(arg == [1,5]):
            sol += " P'R'S "
        elif(arg == [1,9]):
            sol += " Q'R'S "
        elif(arg == [2,3]):
            sol += " P'Q'R "
        elif(arg == [3,7]):
            sol += " P'RS "
        elif(arg == [3,11]):
            sol += " Q'RS "
        elif(arg == [2,6]):
            sol += " P'RS' "
        elif(arg == [2,10]):
            sol += " Q'RS' "
        elif(arg == [4,5]):
            sol += " P'QR' "
        elif (arg == [4, 12]):
            sol += " QR'S' "
        elif(arg == [4,6]):
            sol += " P'QS' "
        elif(arg == [5,7]):
            sol += " P'QS "
        elif(arg == [5,13]):
            sol += " QR'S "
        elif(arg == [6,7]):
            sol += " P'QR "
        elif(arg == [7,15]):
            sol += " QRS "
        elif(arg == [6,14]):
            sol += " QRS' "
        elif(arg == [12,13]):
            sol += " PQR' "
        elif(arg == [8,12]):
            sol += " PR'S' "
        elif(arg == [12,14]):
            sol += " PQS' "
        elif(arg == [9,13]):
            sol += " PR'S "
        elif(arg == [13,15]):
            sol += " PQS "
        elif(arg == [11,15]):
            sol += " PRS "
        elif(arg == [14,15]):
            sol += " PQR "
        elif(arg == [10,14]):
            sol += " PRS' "
        elif (arg == [8, 9]):
            sol += " PQ'R' "
        elif (arg == [8,10]):
            sol += " PQ'S' "
        elif (arg == [9,11]):
            sol += " PQ'S "
        elif (arg == [10, 11]):
            sol += " PQ'R "

    if( len (arg) == 4):
        if( arg == [0,1,2,3]):
            sol += " P'Q' "
        elif( arg == [0,1,4,5]):
            sol += " P'R' "
        elif( arg == [0,4,8,12]):
            sol += " R'S' "
        elif( arg == [0,1,8,9]):
            sol += " Q'R'"
        elif( arg == [0,2,8,10]):
            sol += " Q'S' "
        elif(arg == [0,2,4,6]):
            sol += " P'S' "
        elif( arg == [1,5,9,13]):
            sol += " R'S "
        elif( arg == [1,3,5,7]):
            sol += " P'S "
        elif(arg == [1,3,9,11]):
            sol += " Q'S "
        elif(arg == [2,3,6,7]):
            sol += " P'R "
        elif(arg == [2,3,10,11]):
            sol += " Q'R "
        elif(arg == [3,7,11,15]):
            sol += " RS "
        elif(arg == [2,6,10,14]):
            sol += " RS' "
        elif(arg == [4,5,6,7]):
            sol += " P'Q "
        elif(arg == [4,5,12,13]):
            sol += " QR' "
        elif(arg == [4,6,12,14]):
            sol += " QS' "
        elif(arg == [5,7,13,15]):
            sol += " QS "
        elif(arg == [6,7,14,15]):
            sol += " QR "
        elif(arg == [12,13,14,15]):
            sol += " PQ "
        elif(arg == [8,9,12,13]):
            sol += " PR' "
        elif(arg == [8,10,12,14]):
            sol += " PS' "
        elif(arg == [9,11,13,15]):
            sol += " PS "
        elif(arg == [10,11,14,15]):
            sol += " PR "
        elif(arg == [8,9,10,11]):
            sol += " PQ' "

    if (len(arg) == 8):
        if(arg == [0,1,2,3,4,5,6,7]):
            sol += " P' "
        elif(arg == [0,1,2,3,8,9,10,11]):
            sol += " Q' "
        elif(arg == [0,2,4,6,8,10,12,14]):
            sol += " S' "
        elif(arg == [0,1,4,5,8,9,12,13]):
            sol += " R' "
        elif(arg == [1,3,5,7,9,11,13,15]):
            sol += " S "
        elif(arg == [4,5,6,7,12,13,14,15]):
            sol += " Q "
        elif(arg == [2,3,6,7,10,11,14,15]):
            sol += " R "
        elif(arg == [8,9,10,11,12,13,14,15]):
            sol += " P "


    return sol + " + "



global v
zero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k_map = []
combo = []

free_aces = 0
solution = ""
driver_2 = []
driver_4 = []
driver_8 = []
# -------------SETTING UP THE LIST driver_2------------------------------------------------------
driver_2.append([1, 2, 4, 8])
driver_2.append([-1, 2, 4, 8])
driver_2.append([1, -2, 4, 8])
driver_2.append([-1, -2, 4, 8])
driver_2.append([-4, 1, 2, 8])
driver_2.append([-1, -4, 2, 8])
driver_2.append([-2, -4, 1, 8])
driver_2.append([-4, -2, -1, 8])
driver_2.append([-8, 1, 2, 4])
driver_2.append([-8, -1, 2, 4])
driver_2.append([-8, -2, 1, 4])
driver_2.append([-8, -2, -1, 4])
driver_2.append([-8, -4, 1, 2])
driver_2.append([-8, -4, -1, 2])
driver_2.append([-8, -4, -2, 1])
driver_2.append([-8, -4, -2, -1])
# -------------SETTING UP THE LIST driver_4------------------------------------------------------
driver_4.append([[1, 2, 3], [4, 8, 12], [1, 4, 5], [2, 4, 6], [2, 8, 10], [1, 8, 9]])
driver_4.append([[-1, 1, 2], [4, 8, 12], [-1, 3, 4], [2, 4, 6], [-1, 7, 8], [2, 8, 10]])
driver_4.append([[-2, -1, 1], [4, 8, 12], [-2, 6, 8], [1, 4, 5], [-2, 2, 4], [1, 8, 9]])
driver_4.append([[-1, -2, -3], [4, 8, 12], [-1, 3, 4], [-2, 2, 4], [-2, 6, 8], [-1, 7, 8]])
driver_4.append([[1, 2, 3], [-4, 4, 8], [1, 8, 9], [-4, -3, 1], [-4, -2, 2], [2, 8, 10]])
driver_4.append([[-1, 1, 2], [-4, 4, 8], [2, 8, 10], [-4, -2, 2], [-5, -4, -1], [-1, 7, 8]])
driver_4.append([[-4, 4, 8], [-2, -1, 1], [-4, -3, 1], [1, 8, 9], [-2, 6, 8], [-6, -4, -2]])
driver_4.append([[-4, 4, 8], [-3, -2, -1], [-2, 6, 8], [-6, -4, -2], [-5, -4, -1], [-1, 7, 8]])
driver_4.append([[-8, -4, 4], [1, 2, 3], [-8, -6, 2], [6, 4, 2], [5, 4, 1], [-8, -7, 1]])
driver_4.append([[-8, -4, 4], [-1, 1, 2], [-1, 3, 4], [-9, -8, -1], [-8, -6, 2], [6, 4, 2]])
driver_4.append([[-2, -1, 1], [-8, -4, 4], [-10, -8, -2], [-2, 2, 4], [1, 4, 5], [-8, -7, 1]])
driver_4.append([[-3, -2, -1], [-4, -8, 4], [-9, -8, -1], [-1, 3, 4], [-2, 2, 4], [-10, -8, -2]])
driver_4.append([[1, 2, 3], [-12, -8, -4], [-4, -3, 1], [-4, -2, 2], [-8, -6, 2], [-8, -7, 1]])
driver_4.append([[-1, 1, 2], [-12, -8, -4], [-8, -6, 2], [-5, -4, -1], [-4, -2, 2], [-9, -8, -1]])
driver_4.append([[1, -1, -2], [-12, -8, -4], [1, -3, -4], [-6, -4, -2], [1, -7, -8], [-10, -8, -2]])
driver_4.append([[-3, -2, -1], [-12, -8, -4], [-5, -4, -1], [-6, -4, -2], [-10, -8, -2], [-9, -8, -1]])
# -------------SETTING UP THE LIST driver_8------------------------------------------------------
driver_8.append([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 8, 9, 10, 11], [1, 4, 5, 8, 9, 12, 13], [2, 4, 6, 8, 10, 12, 14]])
driver_8.append(
        [[-1, 1, 2, 3, 4, 5, 6], [-1, 1, 2, 7, 8, 9, 10], [-1, 3, 4, 7, 8, 11, 12], [2, 4, 6, 8, 10, 12, 14]])
driver_8.append(
        [[-2, -1, 1, 2, 3, 4, 5], [-2, -1, 1, 6, 7, 8, 9], [1, 4, 5, 8, 9, 12, 13], [-2, 2, 4, 6, 8, 10, 12]])
driver_8.append(
        [[-3, -2, -1, 1, 2, 3, 4], [-3, -2, -1, 5, 6, 7, 8], [-2, 2, 4, 6, 8, 10, 12], [-1, 3, 4, 7, 8, 11, 12]])
driver_8.append(
        [[-4, -3, -2, -1, 1, 2, 3], [1, 2, 3, 8, 9, 10, 11], [-4, -2, 2, 4, 6, 8, 10], [-4, -3, 1, 4, 5, 8, 9]])
driver_8.append(
        [[-5, -4, -3, -2, -1, 1, 2], [-1, 1, 2, 7, 8, 9, 10], [-5, -4, -1, 3, 4, 7, 8], [-4, -2, 2, 4, 6, 8, 10]])
driver_8.append(
        [[-6, -5, -4, -3, -2, -1, 1], [-2, -1, 1, 6, 7, 8, 9], [-4, -3, 1, 4, 5, 8, 9], [-6, -4, -2, 2, 4, 6, 8]])
driver_8.append(
        [[-7, -6, -5, -4, -3, -2, -1], [-3, -2, -1, 5, 6, 7, 8], [-5, -4, -1, 3, 4, 7, 8], [-6, -4, -2, 2, 4, 6, 8]])
driver_8.append(
        [[7, 6, 5, 4, 3, 2, 1], [3, 2, 1, -5, -6, -7, -8], [5, 4, 1, -3, -4, -7, -8], [6, 4, 2, -2, -4, -6, -8]])
driver_8.append(
        [[6, 5, 4, 3, 2, 1, -1], [2, 1, -1, -6, -7, -8, -9], [4, 3, -1, -4, -5, -8, -9], [6, 4, 2, -2, -4, -6, -8]])
driver_8.append(
        [[5, 4, 3, 2, 1, -1, -2], [1, -1, -2, -7, -8, -9, -10], [5, 4, 1, -3, -4, -7, -8], [4, 2, -2, -4, -6, -8, -10]])
driver_8.append([[4, 3, 2, 1, -1, -2, -3], [-1, -2, -3, -8, -9, -10, -11], [4, 2, -2, -4, -6, -8, -10],
                     [4, 3, -1, -4, -5, -8, -9]])
driver_8.append([[3, 2, 1, -1, -2, -3, -4], [3, 2, 1, -5, -6, -7, -8], [2, -2, -4, -6, -8, -10, -12],
                     [1, -3, -4, -7, -8, -11, -12]])
driver_8.append([[2, 1, -1, -2, -3, -4, -5], [2, 1, -1, -6, -7, -8, -9], [-1, -4, -5, -8, -9, -12, -13],
                     [2, -2, -4, -6, -8, -10, -12]])
driver_8.append([[1, -1, -2, -3, -4, -5, -6], [1, -1, -2, -7, -8, -9, -10], [1, -3, -4, -7, -8, -11, -12],
                     [-2, -4, -6, -8, -10, -12, -14]])
driver_8.append([[-1, -2, -3, -4, -5, -6, -7], [-1, -2, -3, -8, -9, -10, -11], [-1, -4, -5, -8, -9, -12, -13],
                     [-2, -4, -6, -8, -10, -12, -14]])


# SOLVE -> command = getMap
#getMap -> minimization(mlist)

def Mapear(lista, label):
    minimization(lista)
    la = label
    return label
