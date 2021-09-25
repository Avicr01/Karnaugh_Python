def k4v14(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])


#GRUPOS DE CATORCE UNOS (dos ceros)
#GRUPOS DE CEROS
#Ceros en [1] [ ]
# [1] [2]
    if          line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R + Q + P\n"

# [1] [3]
    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R'S + RS' + Q + P\n"

# [1] [4]
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S + Q + P\n"

# [1] [5]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S + R + P\n"

# [1] [6]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q'S + R + QS' + P\n"

# [1] [7]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P + Q'S + RS' + QR'\n"

# [1] [8]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [3], [4], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S + Q'R + QR' + P\n"

# [1] [9]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [7], [8] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S + R + P'Q + PQ'\n"

# [1] [10]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R + P'S + QS' + PQ'\n"

# [1] [11]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'S + Q'R + QS' + PR'\n"

# [1] [12]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S + P'R + QR' + PQ'\n"

# [1] [13]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S + R + Q\n"

# [1] [14]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = P'S + R + Q + PS'\n"

# [1] [15]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = Q + P'S + RS' + PR'\n"

# [1] [16]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S + P'R + Q + PR'\n"

#Ceros en [2] [ ]
# [2] [3]
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S' + Q + P\n"

# [2] [4]
    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R'S' + RS + Q + P\n"

# [2] [5]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = Q'S' + R + QS + P\n"

# [2] [6]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S' + R + P\n"

# [2] [7]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [3], [4], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S' + Q'R + QR' + P\n"

# [2] [8]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = P + Q'S' + RS + QR'\n"

# [2] [9]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R + P'S' + QS + PQ'\n"

# [2] [10]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [7], [8] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S' + R + P'Q + PQ'\n"

# [2] [11]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S' + P'R + QR' + PQ'\n"

# [2] [12]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'S' + Q'R + QS + PR'\n"

# [2] [13]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'S' + R + Q + PS\n"

# [2] [14]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S' + R + Q\n"

# [2] [15]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S' + P'R + Q + PR'\n"

# [2] [16]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q + P'S' + RS + PR'\n"

#Ceros en [3] [ ]
# [3] [4]
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + Q + P\n"

# [3] [5]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = P + Q'R' + RS' + QS\n"

# [3] [6]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + S' + QR + P\n"

# [3] [7]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + S' + P\n"

# [3] [8]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + Q'S' + QS + P\n"

# [3] [9]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + Q'S' + QR + PS\n"

# [3] [10]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S' + P'R' + QR + PQ'\n"

# [3] [11]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [7], [8] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + S' + P'Q + PQ'\n"

# [3] [12]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + P'S' + QS + PQ'\n"

# [3] [13]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = Q + P'R' + RS' + PS\n"

# [3] [14]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + S' + Q + PR\n"

# [3] [15]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + S' + Q\n"

# [3] [16]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + P'S' + Q + PS\n"

#Ceros en [4] [ ]
# [4] [5]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = Q'R' + S + QR + P\n"

# [4] [6]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = P + Q'R' + RS + QS'\n"

# [4] [7]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + Q'S + QS' + P\n"

# [4] [8]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = R' + S + P\n"

# [4] [9]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        
        label += "Funcion simplificada, f(P, Q, R, S) = S + P'R' + QR + PQ'\n"

# [4] [10]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + Q'S + QR + PS'\n"

# [4] [11]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + P'S + QS' + PQ'\n"

# [4] [12]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [7], [8] }\n"
        label += "Grupo de 4 = { [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + S + P'Q + PQ'\n"

# [4] [13]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'R' + S + Q + PR\n"

# [4] [14]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q + P'R' + RS + PS'\n"

# [4] [15]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + P'S + Q + PS'\n"

# [4] [16]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + S + Q\n"

#Ceros en [5] [ ]
# [5] [6]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R + P\n"

# [5] [7]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R'S + RS' + P\n"

# [5] [8]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S + P\n"

# [5] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S + R\n"

# [5] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S + R + PS'\n"

# [5] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S + RS' + PR'\n"

# [5] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S + P'R + PR'\n"

# [5] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + S + R + PQ\n"

# [5] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R + P'Q' + QS + PS'\n"

# [5] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + R'S + QR + PS'\n"

# [5] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S + P'Q' + QR + PR'\n"

#Ceros en [6] [ ]
# [6] [7]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [5], [9], [13], [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S' + P\n"

# [6] [8]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R'S' + RS + P\n"

# [6] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [4], [8] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S' + R + PS\n"

# [6] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S' + R\n"

# [6] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [3], [4], [7], [8] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + S' + P'R + PR'\n"

# [6] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'S' + RS + PR'\n"

# [6] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R + P'Q' + QS' + PS\n"

# [6] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + S' + R + PQ\n"

# [6] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S' + P'Q' + QR + PR'\n"

# [6] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + R'S' + QR + PS\n"

#Ceros en [7] [ ]
# [7] [8]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + P\n"

# [7] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + RS' + PS\n"

# [7] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + S' + PR\n"

# [7] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + S'\n"

# [7] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [4], [8], [1], [5] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + P'S' + PS\n"

# [7] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + QR' + RS' + PS\n"

# [7] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S' + P'Q' + QR' + PR\n"

# [7] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + R' + S' + PQ\n"
        
# [7] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + P'Q' + QS' + PS\n"

#Ceros en [8] [ ]
# [8] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + S + PR\n"

# [8] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + RS + PS'\n"

# [8] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [3], [6], [7] }\n"
        label += "Grupo de 4 = { [12], [16], [9], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + P'S + PS'\n"

# [8] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = Q' + R' + S\n"

# [8] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = S + P'Q' + QR' + PR\n"

# [8] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + R'S' + QS + PR\n"

# [8] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = R' + P'Q' + QS + PS'\n"

# [8] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4] }\n"
        label += "Grupo de 4 = { [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P'Q' + R' + S + PQ\n"

#Ceros en [9] [ ]
# [9] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R\n"

# [9] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'S + RS'\n"

# [9] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + S\n"

# [9] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S + R\n"

# [9] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'S' + R + QS\n"

# [9] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + RS' + QS\n"

# [9] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + S + QR\n"

#Ceros en [10] [ ]
# [10] [11]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + S'\n"

# [10] [12]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'S' + RS\n"

# [10] [13]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'S + R + QS'\n"

# [10] [14]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S' + R\n"

# [10] [15]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [7], [8], [11], [12] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + S' + QR\n"

# [10] [16]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [13], [14], [1], [2] }\n"
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + RS + QS'\n"

#Ceros en [11] [ ]
# [11] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'\n"

# [11] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'S + RS' + QR'\n"

# [11] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S' + Q'R + QR'\n"

# [11] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + S'\n"

# [11] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [8], [12], [5], [9] }\n"
        label += "Grupo de 4 = { [14], [15], [2], [3] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + Q'S + QS'\n"

#Ceros en [12] [ ]
# [12] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [15], [16], [3], [4] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S + Q'R + QR'\n"

# [12] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [5], [6], [9], [10] }\n"
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + Q'S' + RS + QR'\n"

# [12] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [6], [7], [10], [11] }\n"
        label += "Grupo de 4 = { [1], [4], [13], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + Q'S' + QS\n"

# [12] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + S\n"

#Ceros en [13] [ ]
# [13] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R + Q\n"

# [13] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [2], [6], [10], [14] }\n"
        label += "Grupo de 4 = { [4], [8], [12], [16] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R'S + RS' + Q\n"

# [13] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S + Q\n"

#Ceros en [14] [ ]
# [14] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + S' + Q\n"

# [14] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [5], [9], [13] }\n"
        label += "Grupo de 4 = { [3], [7], [11], [15] }\n"
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R'S' + RS + Q\n"

#Ceros en [15] [ ]
# [15] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }\n"
        label += "Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }\n"
        label += "Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }\n"

        label += "Funcion simplificada, f(P, Q, R, S) = P' + R' + Q\n"



    return label