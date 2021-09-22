def k4v14(listing):
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
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = R + Q + P")

# [1] [3]
    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [6], [10], [14] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = R'S + RS' + Q + P")

# [1] [4]
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = S + Q + P")

# [1] [5]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = S + R + P")

# [1] [6]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [14], [15], [2], [3] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q'S + R + QS' + P")

# [1] [7]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [14], [15], [2], [3] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P + Q'S + RS' + QR'")

# [1] [8]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [3], [4], [15], [16] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = S + Q'R + QR' + P")

# [1] [9]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [7], [8] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = S + R + P'Q + PQ'")

# [1] [10]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = R + P'S + QS' + PQ'")

# [1] [11]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 4 = { [15], [16], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'S + Q'R + QS' + PR'")

# [1] [12]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [3], [4], [7], [8] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S + P'R + QR' + PQ'")

# [1] [13]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S + R + Q")

# [1] [14]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = P'S + R + Q + PS'")

# [1] [15]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = Q + P'S + RS' + PR'")

# [1] [16]
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [3], [4], [7], [8] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S + P'R + Q + PR'")

#Ceros en [2] [ ]
# [2] [3]
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S' + Q + P")

# [2] [4]
    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [5], [9], [13] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R'S' + RS + Q + P")

# [2] [5]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [4], [13], [16] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = Q'S' + R + QS + P")

# [2] [6]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S' + R + P")

# [2] [7]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [3], [4], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S' + Q'R + QR' + P")

# [2] [8]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [4], [13], [16] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = P + Q'S' + RS + QR'")

# [2] [9]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R + P'S' + QS + PQ'")

# [2] [10]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [7], [8] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S' + R + P'Q + PQ'")

# [2] [11]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [3], [4], [7], [8] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S' + P'R + QR' + PQ'")

# [2] [12]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 4 = { [15], [16], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'S' + Q'R + QS + PR'")

# [2] [13]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'S' + R + Q + PS")

# [2] [14]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = S' + R + Q")

# [2] [15]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [3], [4], [7], [8] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = S' + P'R + Q + PR'")

# [2] [16]
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q + P'S' + RS + PR'")

#Ceros en [3] [ ]
# [3] [4]
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + Q + P")

# [3] [5]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = P + Q'R' + RS' + QS")

# [3] [6]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = Q'R' + S' + QR + P")

# [3] [7]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + S' + P")

# [3] [8]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [1], [4], [13], [16] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + Q'S' + QS + P")

# [3] [9]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 4 = { [1], [4], [13], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = P'R' + Q'S' + QR + PS")

# [3] [10]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S' + P'R' + QR + PQ'")

# [3] [11]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [7], [8] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + S' + P'Q + PQ'")

# [3] [12]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + P'S' + QS + PQ'")

# [3] [13]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = Q + P'R' + RS' + PS")

# [3] [14]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = P'R' + S' + Q + PR")

# [3] [15]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = R' + S' + Q")

# [3] [16]
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + P'S' + Q + PS")

#Ceros en [4] [ ]
# [4] [5]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = Q'R' + S + QR + P")

# [4] [6]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = P + Q'R' + RS + QS'")

# [4] [7]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [14], [15], [2], [3] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + Q'S + QS' + P")

# [4] [8]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = R' + S + P")

# [4] [9]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        
        print("Funcion simplificada, f(P, Q, R, S) = S + P'R' + QR + PQ'")

# [4] [10]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [14], [15], [2], [3] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'R' + Q'S + QR + PS'")

# [4] [11]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Funcion simplificada, f(P, Q, R, S) = R' + P'S + QS' + PQ'")

# [4] [12]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [7], [8] }")
        print("Grupo de 4 = { [13], [14], [15], [16] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Funcion simplificada, f(P, Q, R, S) = R' + S + P'Q + PQ'")

# [4] [13]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'R' + S + Q + PR")

# [4] [14]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q + P'R' + RS + PS'")

# [4] [15]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = R' + P'S + Q + PS'")

# [4] [16]
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = R' + S + Q")

#Ceros en [5] [ ]
# [5] [6]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R + P")

# [5] [7]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [6], [10], [14] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R'S + RS' + P")

# [5] [8]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + S + P")

# [5] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + S + R")

# [5] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'S + R + PS'")

# [5] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'S + RS' + PR'")

# [5] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [3], [4], [7], [8] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + S + P'R + PR'")

# [5] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [9], [10], [11], [12] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + S + R + PQ")

# [5] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = R + P'Q' + QS + PS'")

# [5] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [2], [6], [10], [14] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + R'S + QR + PS'")

# [5] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Funcion simplificada, f(P, Q, R, S) = S + P'Q' + QR + PR'")

#Ceros en [6] [ ]
# [6] [7]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [5], [9], [13], [4], [8], [12], [16] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + S' + P")

# [6] [8]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [5], [9], [13] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R'S' + RS + P")

# [6] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [5], [4], [8] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'S' + R + PS")

# [6] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + S' + R")

# [6] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [3], [4], [7], [8] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + S' + P'R + PR'")

# [6] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'S' + RS + PR'")

# [6] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = R + P'Q' + QS' + PS")

# [6] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [9], [10], [11], [12] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + S' + R + PQ")

# [6] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = S' + P'Q' + QR + PR'")

# [6] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [1], [5], [9], [13] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + R'S' + QR + PS")

#Ceros en [7] [ ]
# [7] [8]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R' + P")

# [7] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + RS' + PS")

# [7] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + S' + PR")

# [7] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R' + S'")

# [7] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [4], [8], [1], [5] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R' + P'S' + PS")

# [7] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + QR' + RS' + PS")

# [7] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = S' + P'Q' + QR' + PR")

# [7] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [9], [10], [11], [12] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + R' + S' + PQ")
        
# [7] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [10], [11], [14], [15] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Funcion simplificada, f(P, Q, R, S) = R' + P'Q' + QS' + PS")

#Ceros en [8] [ ]
# [8] [9]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + S + PR")

# [8] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [5], [6] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + P'R' + RS + PS'")

# [8] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [3], [6], [7] }")
        print("Grupo de 4 = { [12], [16], [9], [13] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R' + P'S + PS'")

# [8] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = Q' + R' + S")

# [8] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Funcion simplificada, f(P, Q, R, S) = S + P'Q' + QR' + PR")

# [8] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [1], [5], [9], [13] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + R'S' + QS + PR")

# [8] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [11], [12], [15], [16] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Funcion simplificada, f(P, Q, R, S) = R' + P'Q' + QS + PS'")

# [8] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4] }")
        print("Grupo de 4 = { [9], [10], [11], [12] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Funcion simplificada, f(P, Q, R, S) = P'Q' + R' + S + PQ")

#Ceros en [9] [ ]
# [9] [10]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q' + R")

# [9] [11]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [2], [6], [10], [14] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'S + RS'")

# [9] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q' + S")

# [9] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + S + R")

# [9] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [4], [13], [16] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'S' + R + QS")

# [9] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + RS' + QS")

# [9] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + S + QR")

#Ceros en [10] [ ]
# [10] [11]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q' + S'")

# [10] [12]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 4 = { [1], [5], [9], [13] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'S' + RS")

# [10] [13]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [14], [15], [2], [3] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'S + R + QS'")

# [10] [14]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + S' + R")

# [10] [15]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 4 = { [7], [8], [11], [12] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + S' + QR")

# [10] [16]      
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [13], [14], [1], [2] }")
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'R' + RS + QS'")

#Ceros en [11] [ ]
# [11] [12]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q' + R'")

# [11] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [14], [15], [2], [3] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'S + RS' + QR'")

# [11] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [15], [16], [3], [4] }")
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + S' + Q'R + QR'")

# [11] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R' + S'")

# [11] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [8], [12], [5], [9] }")
        print("Grupo de 4 = { [14], [15], [2], [3] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R' + Q'S + QS'")

#Ceros en [12] [ ]
# [12] [13]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [15], [16], [3], [4] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + S + Q'R + QR'")

# [12] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [5], [6], [9], [10] }")
        print("Grupo de 4 = { [1], [4], [13], [16] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + Q'S' + RS + QR'")

# [12] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [6], [7], [10], [11] }")
        print("Grupo de 4 = { [1], [4], [13], [16] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R' + Q'S' + QS")

# [12] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R' + S")

#Ceros en [13] [ ]
# [13] [14]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R + Q")

# [13] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [2], [6], [10], [14] }")
        print("Grupo de 4 = { [4], [8], [12], [16] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R'S + RS' + Q")

# [13] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + S + Q")

#Ceros en [14] [ ]
# [14] [15]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [4], [8], [12], [16], [1], [5], [9], [13] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + S' + Q")

# [14] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [5], [9], [13] }")
        print("Grupo de 4 = { [3], [7], [11], [15] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R'S' + RS + Q")

#Ceros en [15] [ ]
# [15] [16]
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Funcion simplificada, f(P, Q, R, S) = P' + R' + Q")



