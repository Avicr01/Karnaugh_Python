def k4v13(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    # Para grupos de 13 unos
        # Grupo horizontales de 3
        # [1][1][1]
    if          line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = RS' + Q + P\n"

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R'S' + Q + P\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + QR + P + R'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + QR + P + Q'S\n"


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + RS' + P\n"


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R'S' + P\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + PR + R'S\n"


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + PR + P'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + RS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'S'\n"


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R + QR' + Q'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n" 
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R + QR' + RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + RS' + Q\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + R'S' + Q\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n" 
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R + Q + PR' + P'S\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R + Q + PR' + RS\n"


        # Grupos de [1][0][1][1]
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R'S + Q + P\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + QR + P + R'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + QR + P + Q'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'S + QS' + P + Q'R'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R'S + P\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R'S' + RS + PS + PR\n"


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + PR + P'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S + PS' + P'R'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'S + Q'R + QR'S' + RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R + QR' + RS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'S' + QS + R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + R'S + Q\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'S + P'R + Q + PR'S' + RS\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R + Q + PR' + RS'\n"

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'S' + Q + PS + R'S'\n"


        # Grupos de [1][0][0][1]
        #           [1]
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S + QR + P\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'S' + R + P\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + S' + P\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R' + Q'S + P\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S + PR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S' + R\n"
        
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + P'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + S + Q'R\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + R + QS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + S' + QR'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + QS\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S + P'R + Q\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R + Q + PS'\n"

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S' + Q + PR'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R' + Q + PS\n"
   
        # Grupos de [1][0][0][0]
        #           [1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'S + R + P\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S' + Q'R + P\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R' + Q'S' + P\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S + P'R' + PR + Q'R'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S + R\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S' + P'R\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + P'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S + Q'R + QR' + P'Q'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + R + QS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [8], [12], [1], [5], [9], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + S' + QR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + QS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [5], [6], [7], [8] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S + P'R + PR' + P'Q\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R + Q + PS\n"

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = S' + Q + PR\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = R' + Q + PS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + S + QR + PR'\n"


        # Grupos de [1][0][0][0]
        #           [0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'S + QS' + P + Q'R\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R + QR' + P + Q'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'S' + P'R' + QS + PR + Q'R'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + P'S + QR + PQ'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S + PS' + P'R\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R + PR' + P'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'S' + Q'R + QR' + PS + P'Q'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + QR' + P'S + PR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'S' + QS + RS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + QR + R'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R + PR' + Q'S + QS' + P'S\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R + QR' + PQ' + RS\n"

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + QR + R'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + Q + PR + R'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + P'S + QR + PS' + R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + QR + RS + PR'\n"

        # Grupos de [1][0][0][0]
        #           [0][0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R + QR' + P + Q'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PR + P'R'S' + Q'R + QS + PQ'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + P'S' + QR + PQ'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + P'S + QS' + PQ'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R + PR' + P'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R + P'Q' + QR'S' + P'R + PS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + QR' + P'S' + PR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + P'R' + QS + PS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + QR + R'S\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 2 = { [13], [14] }\n"
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R + P'S + QS' + PQ'R' + RS\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R + QR' + PQ' + RS'\n"

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'S' + QS + PQ' + R'S'\n"

    return label

