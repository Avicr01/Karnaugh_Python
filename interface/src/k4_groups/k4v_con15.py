def k4v15(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    if          line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S + R + Q + P\n"
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"

        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S' + R + Q + P\n"
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + S' + Q + P\n"
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + S + Q + P\n"
# ---
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S + R + P\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"

        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S' + R + P\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + S' + P\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + S + P\n"
# --- 
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + S + R\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"

        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + S' + R\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R' + S'\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R' + S\n"
# --- 
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S + R + Q\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"

        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S' + R' + Q\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + S' + Q\n"
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + S + Q\n"

    return label
