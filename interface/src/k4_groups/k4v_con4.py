def k4v4(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])
    
    #1	2	3	a	
    #4	<=	a	<=	16		

    if        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1],[2],[3],[4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S + P'R'S' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + P'R'S \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'RS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + P'QRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + PQR'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + PQR'S\n"


    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + PQRS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + PQRS'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S + Q'R'S'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + Q'R'S\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [3, [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'RS\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S + PQ'RS'\n"


    #1	2	b	a	
    #4	<=	b	<=	15		
    #5	<=	a	<=	16		

    # b == 4

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [5] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + P'R'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'R'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + P'QRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [4], [8] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'RS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + PQR'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + PQR'S\n"


    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + PQRS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + PQRS'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + Q'R'S'\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + Q'R'S\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'Q'S' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'RS'\n"

    # b == 5

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2], [5], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S' + P'QRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + QR'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S' + PQR'S\n"


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S' + PQRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S' + PQRS' \n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S' + Q'R'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [1], [5] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + Q'R'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S' + PQ'RS'\n"


    # b == 6

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [6], [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S + P'QRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + QR'S\n"


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S + PQRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S + PQRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [1], [13] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S + Q'R'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S + Q'R'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S + PQ'RS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'R'S + PQ'RS'\n"


    # b == 7

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [7], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QR\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS + PQR'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS + PQR'S\n"


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + QRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 2 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS + PQRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS + Q'R'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS + Q'R'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS + PQ'RS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [7] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS + PQ'RS'\n"


    # b == 8

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS' + PQR'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS' + PQR'S\n"


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS' + PQRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + QRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS' + Q'R'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS' + Q'R'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [8] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + P'QRS' + PQ'RS'\n"


    # b == 9

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [5], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR'\n"


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [5] }\n"
        label += "Grupo de 2 = { [7] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR'S' + PQRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [5], [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) =  P'Q'R' + PR'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S + PQR'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS + PQR'S'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS' + PQR'S'\n"


    # b == 10

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR'S + PQRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [1], [13] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = f(P, Q, R, S) = P'Q'R' + Q'R'S' + PQR'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PR'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS + PQR'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS' + PQR'S\n"


    # b == 11

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQR\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S' + PQRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S + PQRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PRS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS' + PQRS\n"


    # b == 12

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S' + PQRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S + PQRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'RS + PQRS'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PRS'\n"


    # b == 13

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [13], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R'\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 1 = { [15] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S' + PQ'RS\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [13], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'S'\n"

    # b == 14

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [14], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'S\n"

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [2] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + Q'R'S + PQ'RS'\n"

    # b == 15

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 1 = { [1], [2] }\n"
        label += "Grupo de 2 = { [15], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R' + PQ'R\n"


    #1	c	b	a	
    #2	<=	c	<=	14		
    #3	<=	b	<=	15		
    #4	<=	a	<=	16		

    ## c = 3

    # b == 4

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [5] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R + P'R'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + P'QR'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + P'RS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + PQR'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + PQR'S\n"


    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + PQRS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + PQRS'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R + Q'R'S'\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [4], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [3], [15] }\n"
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + Q'RS\n"

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 2 = { [1], [4] }\n"
        label += "Grupo de 2 = { [3], [4] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'S' + P'Q'R + Q'RS'\n"

    # b == 5

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [5], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + P'QR'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1], [5] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'RS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + P'QS'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + QR'S'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + PQR'S\n"


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + PQRS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + PQRS'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'RS + P'R'S' + Q'R'S'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [14] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [3], [15] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + Q'RS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'R'S' + P'Q'RS + PQ'RS'\n"


    # b == 6

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [5], [6] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'RS + P'QS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 2 = { [3] }\n"
        label += "Grupo de 2 = { [6] }\n"
        label += "Grupo de 2 = { [8] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QR'S + P'QRS'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 2 = { [3] }\n"
        label += "Grupo de 2 = { [6] }\n"
        label += "Grupo de 2 = { [9] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QR'S + PQR'S'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + QR'S\n"


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QR'S + PQRS\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QR'S + PQRS'\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R'S' + P'Q'RS + P'QR'S\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [14] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) =P'Q'R'S' + P'Q'RS + P'QR'S + PQ'R'S\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + Q'RS + P'QR'S\n"

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 1 = { [1] }\n"
        label += "Grupo de 1 = { [3] }\n"
        label += "Grupo de 1 = { [6] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(P, Q, R, S) = P'Q'R'S' + P'Q'RS + P'QR'S + PQ'RS'\n"

    return label
