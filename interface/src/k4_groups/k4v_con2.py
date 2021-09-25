def k4v2(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    # Grupo horizontales de 2
    # [1][1]
    if          line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'\n"
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S'\n"
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [5], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [6], [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) =  P'QRS' + PQR'S'\n"
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQR'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQR\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQRS'\n"
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 2 = { [13], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 2 = { [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 2 = { [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R\n"
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 1 = { [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS'\n"

        # Grupos de [1] [0] [1]

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS\n"
    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [2] }\n"
        label += "Grupo de 1 = { [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) =  P'Q'R'S + P'Q'RS'\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) =P'Q'RS + P'QR'S'\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [5] }\n"
        label += "Grupo de 1 = { [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQR'S' + PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQR'S + PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 1 = { [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 1 = { [13] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQ'RS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQ'RS'\n"
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 1 = { [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 1 = { [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS'\n"

        # Grupos de [1] [0] [0] [1]

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S'\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [2] }\n"
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S'\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Grupo de 1 = { [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 1 = { [14 }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 2 = { [13], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'S'\n"
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 1 = { [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 1 = { [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS'\n"

        # Grupos de [1] [0] [0] [0]
        #           [1] [0] [0] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S'\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'RS\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'RS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = QR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = QR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = QRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = QRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PRS'\n"
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 2 = { [13], [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R'S'\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 2 = { [14], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R'S\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 2 = { [15], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'RS\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 2 = { [16], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'RS'\n"

        # Grupos de [1] [0] [0] [0]
        #           [0] [1] [0] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [2] }\n"
        label += "Grupo de 1 = { [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS'\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [5] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQRS\n"
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 1 = { [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQRS'\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [13] }\n"
        label += "Grupo de 1 = { [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S'\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 1 = { [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS'\n"

        # Grupos de [1] [0] [0] [0]
        #           [0] [0] [1] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [2] }\n"
        label += "Grupo de 1 = { [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS'\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S'\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [5] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'S\n"
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 1 = { [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQRS\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 1 = { [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQRS'\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [13] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S'\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 1 = { [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS'\n"

        # Grupos de [1] [0] [0] [0]
        #           [0] [0] [0] [1]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS'\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [2] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S'\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [5] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'S'\n"
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 1 = { [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQRS\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQRS'\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [13] }\n"
        label += "Grupo de 1 = { [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 1 = { [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS'\n"

        # Grupos de [1] [0] [0] [0]
        #           [0] [0] [0] [0]
        #           [1] [0] [0] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S'\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [2] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQRS\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [5] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS'\n"



# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Para grupos de 1 unos
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S'\n"
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS\n"
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'QRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQR'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQR'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQRS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQRS'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S'\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'R'S\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS\n"
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = PQ'RS'\n"

    return label

