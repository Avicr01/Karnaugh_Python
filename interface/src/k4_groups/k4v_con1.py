def k4v1(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    if          line1 == (1, 0, 0, 0) \
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


