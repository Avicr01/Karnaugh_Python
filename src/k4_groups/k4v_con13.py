def k4v13(listing):
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
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'Q'R")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [3], [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'QR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [6] }")
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [6] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + P'QS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [6], [7] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + P'QR")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [7], [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQR'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR' + PQS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [10], [11] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQS + PQR")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQR")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [13], [14] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 2 = { [13], [14] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQ'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 2 = { [14], [15] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S + PQ'R")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 2 = { [15], [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS'")


        # Grupos de [1][0][1][1]
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [3], [4] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + P'QR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [6] }")
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [6], [7] }")
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [7], [8] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + P'QR")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [10], [11] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 2 = { [12], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQS' + PQR")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [13], [14] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 2 = { [14], [15] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 2 = { [15], [16] }")
        print("Grupo de 2 = { [16], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S' + PQ'R")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQ'RS'")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQ'RS'")


        # Grupos de [1][0][0][1]
        #           [1]
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [1], [4] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'R'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + P'QR'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + P'QS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [8], [4] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + P'QR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + QR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PQR'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [7], [11] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS + PQS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS' + PQR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [9], [12] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S' + PQS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [10], [14] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R' + PR'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 2 = { [11], [15] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S + PRS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 2 = { [12], [16] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R + PRS'")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 2 = { [13], [1] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQ'S'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 2 = { [14], [2] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [15], [3] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + Q'RS")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [16], [4] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + Q'RS'")


   
        # Grupos de [1][0][0][0]
        #           [1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [6], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'QR'")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + P'QS")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + P'QR")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + PQR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [9] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S' + PQR'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PQS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [7], [11] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS + PQR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS' + PQ'R'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [9], [13] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R' + PR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 2 = { [10], [14] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S + PR'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 2 = { [11], [15] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R + PRS")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [12], [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PRS'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [13], [1] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S'")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 2 = { [14], [2] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + Q'R'S")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [15], [3] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + Q'RS")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [16], [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + P'QR'S'")


        # Grupos de [1][0][0][0]
        #           [0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QS")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQR'S'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S' + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S + PQR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R + PQR'S")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS' + PQRS")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQRS'")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQ'R'S'")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQ'R'S")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQ'RS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'RS'")


        # Grupos de [1][0][0][0]
        #           [0][0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQR'S'")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S' + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R + PQR'S'")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS' + PQR'S")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQRS")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQRS'")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQ'R'S'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQ'R'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'RS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'RS'")


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQR'S'")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQS")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S' + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS' + PQR'S'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR'S")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQRS")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQRS'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQ'R'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'R'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'RS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'RS'")



        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQS")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQ'RS'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR'S'")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQR'S")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQRS")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + PQ'R'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'R'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'RS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS' + PQR'S")


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQS")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S' + PQRS'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQ'RS'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS'")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + PQR'S'")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQR'S")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQRS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + PQ'R'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'R'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS + PQR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'")
        
        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][1][1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQRS'")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [16] }")
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQ'RS'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'QRS'")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + PQR'S'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + PQR'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + PQRS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + PQ'R'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S + PQR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQS")



        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][1]
        #           [1]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQRS'")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQ'R'")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + PQ'S")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQ'R")
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQ'RS'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'RS")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [3], [4] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'RS'")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + QR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [6] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + QR'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [6], [7] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + QRS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [7], [8] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + QRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S + PQR'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [10], [11] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS + PQS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS' + PQR")

        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        #           [1][1][0][0]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQ'R'")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQ'S")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + PQ'R")
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + Q'RS'")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S'")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'R'S")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [3], [4] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'RS")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + P'QS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [6] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + QR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [6], [7] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + QR'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [7], [8] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + QRS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS' + PQS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S' + PQR'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 2 = { [10], [11] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S + PQS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS + PQR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 2 = { [12], [16] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S' + PRS'")


         # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        #           [0][1][1][0]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'S")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R")
    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQ'RS'")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [1], [2] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S'")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'QR'S'")
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'QR'S")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S' + P'QRS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [6] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR' + P'QS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS + PQR'S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR + PQR'S")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQR'S' + PQRS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQR' + PQS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQS")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQR")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQ'RS + PQRS'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 2 = { [13], [14] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R' + PQ'S'")



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
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + P'Q'RS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + P'QR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + P'QR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S' + P'QRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + P'QRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS' + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PRS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [11]  }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQ'RS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [16]  }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQ'RS'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1]  }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + Q'RS")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [2]  }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + Q'RS'")


        # Grupos de [1][0][0][1]
        #           [0][1][0][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 2 - 1 - 10

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1]  }")
        print("Grupo de 1 = { [4]  }")
        print("Grupo de 1 = { [6]  }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'QR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2]  }")
        print("Grupo de 1 = { [5]  }")
        print("Grupo de 1 = { [7]  }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + P'QRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + P'QS + P'QR")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5]  }")
        print("Grupo de 1 = { [8]  }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6]  }")
        print("Grupo de 1 = { [9]  }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQR'S' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [8]  }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S' + PQ'RS + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQ'RS' + PQRS")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS + PQRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'S'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQ'R'S")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQ'RS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQ'RS'")

        # Grupos de [1][0][0][0]
        #           [1][0][1][0]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 3 - 1 - 9 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'QRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + P'QRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + PQR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS' + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PR'S + PQ'RS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PRS")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PRS'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'Q'RS")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'Q'RS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + P'QR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + P'QR'S")

        # Grupos de [1][0][0][0]
        #           [0][1][0][1]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 4 - 1 - 8 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + P'QRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQR'S")
#hay dos 10
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [6 }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQ'RS' + PQR'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'RS + PQR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS' + PQRS")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQRS'")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQ'R'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'RS'")

        # Grupos de [1][0][0][0]
        #           [0][0][1][0]
        #           [1][0][0][0]
        #           [0][0][0][0]
        # 5 - 1 - 7 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S' + PQRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S + PQ'RS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQR'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS' + PQR'S")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQRS")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'RS'")


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [0][1][0][0]
        #           [0][0][0][0]
        # 6 - 1 - 6 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S' + PQRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQR'S + PQRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S + PQ'RS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQ'RS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS' + PQR'S'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQR'S")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS' + PQR'S'")
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
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S' + PQRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQR'S + PQRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S' + PQRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQ'RS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQ'RS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQ'RS'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + PQR'S'")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS' + PQR'S")


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][1][0][1]
        #           [0][0][0][0]
        # 8 - 1 - 4 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQR'S + PQRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQ'RS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQ'RS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQ'RS'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QRS'")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + PQR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S' + PQR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS' + PQR'S' + PQRS")

        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][1][0]
        #           [1][0][0][0]
        # 9 - 1 - 3 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + PQ'R'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQ'R'S")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQ'RS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + PQ'RS'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'RS")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'RS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + QR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + QR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + QRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + QRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS' + PQR'S")

        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][0][0][1]
        #           [0][1][0][0]
        # 10 - 1 - 2 

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [13] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQ'RS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [14] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQ'RS'")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQ'RS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQ'RS'")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QR'S")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'Q'RS' + P'QRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QR'S + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + P'QRS + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + P'QRS' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S' + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'R'S + PQR'S' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQR'S + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S' + PQRS")

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
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'QRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'R'S' + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'R'S + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'RS + PQS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S' + PQR'S")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'S'")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQ'R'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQ'RS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'RS'")

        # Grupos de [1][0][0][0]
        #           [1][0][0][1]
        #           [0][0][0][0]
        #           [0][0][0][0]
        # 3 - 2 - 8

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'QS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + PQR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + PQR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [9] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S' + PQS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 2 = { [9], [13] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PQ'S' + PR'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PRS'")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + Q'R'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'QR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + P'QR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + P'QRS")


        # Grupos de [1][0][0][0]
        #           [0][1][0][0]
        #           [1][0][0][0]
        #           [0][0][0][0]
        # 4 - 2 - 7

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQR'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S' + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQ'R'S + PQR'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS' + PQRS")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQ'R'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'RS'")


        # Grupos de [1][0][0][0]
        #           [0][0][1][0]
        #           [0][1][0][0]
        #           [0][0][0][0]
        # 5 - 2 - 6

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S' + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'R'S + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQ'R'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'RS + PQR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS' + PQR'S")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQ'R'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS' + PQR'S'")


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [0][0][1][0]
        #           [0][0][0][0]
        # 6 - 2 - 5

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS' + PQRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S' + PQR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S + PQRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQ'R'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQ'RS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'RS' + PQR'S'")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [1], [4] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS' + PQR'S")


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [1][0][0][1]
        #           [0][0][0][0]
        # 7 - 2 - 4

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [1], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + PQS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PQ'R'S' + PQR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [12] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQ'R'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQ'RS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQ'RS'")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [1], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + PQR'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QR'S' + PQR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QR'S + PQRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + P'QRS + PQRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'R'S + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PQ'RS + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PQ'RS' + PQRS")


        # Grupos de [1][0][0][0]
        #           [0][0][0][0]
        #           [0][1][0][0]
        #           [1][0][0][0]
        # 8 - 2 - 3

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PQR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + PQRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 2 = { [13], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQ'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQ'R'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + PQ'RS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + PQ'RS'")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [1], [4] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'RS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + QR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + QR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + QRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QS' + QRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS' + PRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [9], [12] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = PRS' + PQS'")


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
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + QR'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + QR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + QRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + QRS'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [5], [9] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S' + PR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [7], [11] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS + PRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS' + PRS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { 9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + PR'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + PR'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + PRS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + PRS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + Q'R'S'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + Q'R'S")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + Q'RS")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + Q'RS'")


        # Grupos de [1][0][0][0]
        #           [0][1][0][0]
        #           [0][1][0][0]
        #           [0][0][0][0]
        # 4 - 3- 6


    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + QR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + QRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + QRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QRS + PRS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'QRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + PQR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + PQR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQRS")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + PQ'R'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + PQ'R'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S' + PQ'RS'")


        # Grupos de [1][0][0][0]
        #           [0][0][1][0]
        #           [0][0][1][0]
        #           [0][0][0][0]
        # 5 - 3- 5

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + QRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + QRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PRS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'QRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'QRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + PQR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQR'S")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + PQRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + PQ'R'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S' + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PQ'RS'")


        # Grupos de [1][0][0][0]
        #           [0][0][0][1]
        #           [0][0][0][1]
        #           [0][0][0][0]
        # 6 - 3- 4

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + QRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + PR'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PR'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PRS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PRS'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'QR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [7] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'R'S + P'QRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [8] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS + P'QRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [9] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = Q'RS' + PQR'S'")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [10] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S' + PQR'S")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [11] }")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'R'S + PQRS")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [12] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS + PQRS'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [13] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'RS' + PQ'R'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S' + PQ'R'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [15] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(P, Q, R, S) = QR'S + PQ'RS")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [16] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = QRS + PQ'RS'")


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
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQRS")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQRS'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQ'R'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'R'S + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S + PQ'RS' + PQRS")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QRS + PQRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS' + PQ'R'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + PQ'R'S + PQR'S'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS + PQR'S")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS' + PQRS")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [1] }")
        print("Grupo de 1 = { [6] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'QR'S + PQRS'")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [2] }")
        print("Grupo de 1 = { [7] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'R'S + P'QRS + PQ'R'S'")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [3] }")
        print("Grupo de 1 = { [8] }")
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'QRS' + PQ'R'S")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [4] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'Q'RS' + PQ'RS + PQR'S'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [5] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(P, Q, R, S) = P'QR'S' + PQ'RS' + PQR'S")


