def k4v2(listing):
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
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'")
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S'")
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) =  P'QRS' + PQR'S'")
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQRS'")
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS'")

        # Grupos de [1] [0] [1]

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS")
    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, f(P, Q, R, S) =  P'Q'R'S + P'Q'RS'")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) =P'Q'RS + P'QR'S'")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR'S' + PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR'S + PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQ'RS'")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS'")

        # Grupos de [1] [0] [0] [1]

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S'")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14 }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S'")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS'")

        # Grupos de [1] [0] [0] [0]
        #           [1] [0] [0] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS'")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 2 = { [13], [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 2 = { [14], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 2 = { [15], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 2 = { [16], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS'")

        # Grupos de [1] [0] [0] [0]
        #           [0] [1] [0] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS'")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQRS")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQRS'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S'")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS'")

        # Grupos de [1] [0] [0] [0]
        #           [0] [0] [1] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS'")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S'")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'S")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQRS")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQRS'")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S'")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS'")

        # Grupos de [1] [0] [0] [0]
        #           [0] [0] [0] [1]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S'")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'S'")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQRS")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQRS'")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS'")

        # Grupos de [1] [0] [0] [0]
        #           [0] [0] [0] [0]
        #           [1] [0] [0] [0]
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQRS")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS'")



# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Para grupos de 1 unos
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS'")

