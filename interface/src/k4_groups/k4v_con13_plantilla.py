def k4v13(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

        # Grupo horizontales de 3
        # [1][1][1]
    if          line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S\n"

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'Q'R\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'QR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + P'QS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + P'QR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQR'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQR' + PQS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQS + PQR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 0, 1):
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQ'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 0):
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S + PQ'R\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS'\n"


        # Grupos de [1][0][1][1]
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + P'QR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + P'QR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Grupo de 2 = { [12], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQS' + PQR\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 0):
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Grupo de 2 = { [16], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S' + PQ'R\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQ'RS'\n"

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R\n"

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQ'RS'\n"


        # Grupos de [1][0][0][1]
        #           [1]
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'R'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + P'QR'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + P'QS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [8], [4] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + P'QR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + QR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PQR'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS + PQS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS' + PQR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S' + PQS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R' + PR'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S + PRS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R + PRS'\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 2 = { [13], [1] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQ'S'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 2 = { [14], [2] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [15], [3] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + Q'RS\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [16], [4] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + Q'RS'\n"


   
        # Grupos de [1][0][0][0]
        #           [1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Grupo de 2 = { [6], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'QR'\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + P'QS\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + P'QR\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + PQR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S' + PQR'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PQS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS + PQR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS' + PQ'R'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R' + PR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S + PR'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R + PRS\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PRS'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [13], [1] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S'\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 2 = { [14], [2] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + Q'R'S\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [15], [3] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + Q'RS\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [16], [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + P'QR'S'\n"


        # Grupos de [1][0][0][0]
        #           [0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QS\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQR'S'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S' + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S + PQR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R + PQR'S\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS' + PQRS\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQRS'\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQ'R'S'\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQ'R'S\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQ'RS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'RS'\n"


        # Grupos de [1][0][0][0]
        #           [0][0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQR'S'\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S' + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R + PQR'S'\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS' + PQR'S\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQRS\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQRS'\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQ'R'S'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQ'R'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'RS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'RS'\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQR'S'\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQS\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S' + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS' + PQR'S'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR'S\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQRS\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQRS'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQ'R'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'R'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'RS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'RS'\n"



        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQS\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQ'RS'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR'S'\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQR'S\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQRS\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'R'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'R'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'RS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS' + PQR'S\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQS\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S' + PQRS'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQ'RS'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS'\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQR'S'\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQR'S\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQRS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'R'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'R'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS + PQR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'\n"
        
        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQRS'\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQ'RS'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'QRS'\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQR'S'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQR'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + PQRS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'R'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S + PQR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQS\n"



        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][1]
        #           [1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQRS'\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQ'R'\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + PQ'S\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQ'R\n"
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQ'RS'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'RS\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'RS'\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + QR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + QR'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + QRS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + QRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S + PQR'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PRS + PQS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PRS' + PQR\n"

        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        #           [1][1][0][0]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQ'R'\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQ'S\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + PQ'R\n"
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + Q'RS'\n"
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S'\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'R'S\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'RS\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + P'QS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + QR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + QR'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + QRS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS' + PQS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S' + PQR'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S + PQS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PRS + PQR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S' + PRS'\n"


         # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        #           [0][1][1][0]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [14], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'S\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R\n"
    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQ'RS'\n"
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [2] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S'\n"
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [2], [3] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'QR'S'\n"
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [3], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'QR'S\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + P'QRS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [6] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR' + P'QS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [6], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS + PQR'S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [7], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR + PQR'S\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQR'S' + PQRS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [9], [10] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQR' + PQS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [10], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQS\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [11], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQR\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQ'RS + PQRS'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 0):
        label +=  "Grupo de 2 = { [13], [14] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQ'S'\n"



    # Grupos con espacios separados

        # x espacios 1 separado
        # Grupos de [1][0][1][0]
        #           [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 1 - 1 - 11

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + P'Q'RS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + P'QR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + P'QR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S' + P'QRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + P'QRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS' + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PRS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [11]  }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQ'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [16]  }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQ'RS'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1]  }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + Q'RS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [2]  }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + Q'RS'\n"


        # Grupos de [1][0][0][1]
        #           [0][1][0][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 2 - 1 - 10

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1]  }\n"
        label +=  "Grupo de 1 = { [4]  }\n"
        label +=  "Grupo de 1 = { [6]  }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'QR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2]  }\n"
        label +=  "Grupo de 1 = { [5]  }\n"
        label +=  "Grupo de 1 = { [7]  }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + P'QRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + P'QS + P'QR\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5]  }\n"
        label +=  "Grupo de 1 = { [8]  }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6]  }\n"
        label +=  "Grupo de 1 = { [9]  }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQR'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [8]  }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQ'RS + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQ'RS' + PQRS\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'S'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQ'RS'\n"

        # Grupos de [1][0][0][0]
        #           [1][0][1][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 3 - 1 - 9 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'QRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + P'QRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS' + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PR'S + PQ'RS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PRS\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PRS'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'Q'RS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'Q'RS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + P'QR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + P'QR'S\n"

        # Grupos de [1][0][0][0]
        #           [0][1][0][1]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 4 - 1 - 8 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + P'QRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQR'S\n"
#hay dos 10
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [6 }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQ'RS' + PQR'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS + PQR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS' + PQRS\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQRS'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQ'R'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'RS'\n"

        # Grupos de [1][0][0][0]
        #           [0][0][1][0]
        #           [1][0][0][0]
        #           [0][0][0][0]
        # 5 - 1 - 7 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S + PQ'RS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQR'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS' + PQR'S\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQRS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'RS'\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [0][1][0][0]
        #           [0][0][0][0]
        # 6 - 1 - 6 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S' + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S + PQ'RS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQ'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS' + PQR'S'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQR'S\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS' + PQR'S'\n"
##################################################################################

        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [1][0][1][0]
        #           [0][0][0][0]
        # 7 - 1 - 5 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S' + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQ'RS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQ'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQ'RS'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQR'S'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS' + PQR'S\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][1][0][1]
        #           [0][0][0][0]
        # 8 - 1 - 4 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQ'RS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQ'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQ'RS'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QRS'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'S' + PQRS\n"

        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][1][0]
        #           [1][0][0][0]
        # 9 - 1 - 3 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQ'R'S\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQ'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + PQ'RS'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'RS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'RS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + QR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + QR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + QRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + QRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PRS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PRS' + PQR'S\n"

        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][1]
        #           [0][1][0][0]
        # 10 - 1 - 2 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQ'RS'\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQ'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQ'RS'\n"

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QR'S\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + P'QRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S' + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQR'S' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S' + PQRS\n"

        # x espacios 2 separado

        # Grupos de [1][0][0][1]
        #           [0][0][1][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 2 - 2 - 9

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'QRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S' + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S' + PQR'S\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'S'\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'RS'\n"

        # Grupos de [1][0][0][0]
        #           [1][0][0][1]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 3 - 2 - 8

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'QS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + PQR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S' + PQS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PQ'S' + PR'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PRS'\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + Q'R'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'QR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + P'QR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + P'QRS\n"


        # Grupos de [1][0][0][0]
        #           [0][1][0][0]
        #           [1][0][0][0]
        #           [0][0][0][0]
        # 4 - 2 - 7

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQR'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S' + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQR'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS' + PQRS\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQ'R'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'RS'\n"


        # Grupos de [1][0][0][0]
        #           [0][0][1][0]
        #           [0][1][0][0]
        #           [0][0][0][0]
        # 5 - 2 - 6

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS' + PQR'S\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS' + PQR'S'\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [0][0][1][0]
        #           [0][0][0][0]
        # 6 - 2 - 5

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S' + PQR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S + PQRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS' + PQR'S'\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS' + PQR'S\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [1][0][0][1]
        #           [0][0][0][0]
        # 7 - 2 - 4

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [1], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQ'RS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQ'RS'\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [1], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQR'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS' + PQRS\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][1][0][0]
        #           [1][0][0][0]
        # 8 - 2 - 3

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + PQRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Grupo de 2 = { [13], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQ'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + PQ'RS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + PQ'RS'\n"

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [4] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'RS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + QR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + QR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + QRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [8] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QS' + QRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS' + PRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [9], [12] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = PRS' + PQS'\n"


        # x espacios 3 espacios
        # Grupos de [1][0][0][0]
        #           [1][0][0][0]
        #           [1][0][0][0]
        #           [0][0][0][0]
        # 3 - 3- 7

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + QR'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + QR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + QRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + QRS'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S' + PR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS + PRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Grupo de 2 = { [15], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS' + PRS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Grupo de 2 = { 9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PR'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + PR'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + PRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + PRS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + Q'R'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + Q'R'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + Q'RS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + Q'RS'\n"


        # Grupos de [1][0][0][0]
        #           [0][1][0][0]
        #           [0][1][0][0]
        #           [0][0][0][0]
        # 4 - 3- 6


    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + QR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + QRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + QRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QRS + PRS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'QRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + PQR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQRS\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + PQ'R'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S' + PQ'RS'\n"


        # Grupos de [1][0][0][0]
        #           [0][0][1][0]
        #           [0][0][1][0]
        #           [0][0][0][0]
        # 5 - 3- 5

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + QRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + QRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PRS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'QRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'QRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQR'S\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S' + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PQ'RS'\n"


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [0][0][0][1]
        #           [0][0][0][0]
        # 6 - 3- 4

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 2 = { [8], [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + QRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 2 = { [9], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 2 = { [10], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PR'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 2 = { [11], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PRS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 2 = { [12], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PRS'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 2 = { [1], [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'QR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 2 = { [2], [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'QRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 2 = { [3], [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS + P'QRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 2 = { [4], [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQR'S'\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 2 = { [1], [5] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 2 = { [2], [6] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'R'S + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Grupo de 2 = { [3], [7] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS + PQRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Grupo de 2 = { [4], [8] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'RS' + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Grupo de 2 = { [5], [9] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S' + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Grupo de 2 = { [6], [10] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QR'S + PQ'RS\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Grupo de 2 = { [7], [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = QRS + PQ'RS'\n"


        # x espacios 4 espacios
        # Grupos de [1][0][0][0]
        #           [0][1][0][0]
        #           [0][0][1][0]
        #           [0][0][0][0]
        # 4 - 4- 5
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQ'R'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS' + PQRS\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQ'R'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS + PQR'S\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [11] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS' + PQRS\n"

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label +=  "Grupo de 1 = { [1] }\n"
        label +=  "Grupo de 1 = { [6] }\n"
        label +=  "Grupo de 1 = { [12] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label +=  "Grupo de 1 = { [2] }\n"
        label +=  "Grupo de 1 = { [7] }\n"
        label +=  "Grupo de 1 = { [13] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQ'R'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label +=  "Grupo de 1 = { [3] }\n"
        label +=  "Grupo de 1 = { [8] }\n"
        label +=  "Grupo de 1 = { [14] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQ'R'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label +=  "Grupo de 1 = { [4] }\n"
        label +=  "Grupo de 1 = { [9] }\n"
        label +=  "Grupo de 1 = { [15] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS + PQR'S'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label +=  "Grupo de 1 = { [5] }\n"
        label +=  "Grupo de 1 = { [10] }\n"
        label +=  "Grupo de 1 = { [16] }\n"
        label +=  "Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS' + PQR'S\n"

    return label

