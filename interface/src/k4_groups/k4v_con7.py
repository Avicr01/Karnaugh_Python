def k4v7(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    #1	2	3	4   5   6  x
    #7	<=	x	<=	16		

    if          line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + a'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [4], [5], [8]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + a'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + bc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + bc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'cd' \n"


    #1	2	3	4   5   a  x
    #7	<=	a	<=	15		
    #8	<=	x	<=	16		

    # a = 7


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 4 = { [1], [4], [5], [8]}\n"
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + a'c \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + bc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + abc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3] ,[4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = f(a, b, c, d) = a'b' + a'c'd' + bcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 1 = { [5] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [15], [3] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [16], [4] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'cd' \n"


    # a = 8
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + bc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 2 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + abc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + bcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [4], [8]}\n"
        label += "Grupo de 2 = { [16], [4] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'cd' \n"


    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc' + a'c'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + bc'd' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd' + a'c'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [5], [9], [13]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [14], [2] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + bc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [15], [3] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + bc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [16], [4] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + bc'd' \n"


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + abd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + abc'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + abc'd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + ac'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd + abc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd' + abc'd \n"

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + abc \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + abcd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) =  a'b' + a'c'd' + b'c'd + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + acd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd' + abcd \n"


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + abcd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd + abcd'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + acd' \n"


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'd'\n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd + b'cd' \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c \n"


    #1	2	3	4   b   a  x
    #6	<=	b	<=	14		
    #7	<=	a	<=	15		
    #8	<=	x	<=	16		

    ## b = 6
    
    # a = 7


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + a'c \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + bc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + bcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'cd' \n"


    # a = 8
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + bc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + bcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'cd' \n"


    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc' + a'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + abc'd' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + abd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + ac'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd' + abc'd' \n"


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd + a'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + bc'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + bc'd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [6], [10], [14]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + bc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + bc'd\n"

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + abc \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd' + abcd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + acd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [3], [16] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd' + abcd \n"


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd' + abcd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + acd' \n"


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd' + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'd' \n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + b'cd' \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Grupo de 2 = { [2], [6] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c \n"


    ## b = 7
    
    # a = 8
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + abc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + bcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + bcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [7], [8]}\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'cd' \n"


    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + abc' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc'd' + bcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + abd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + ac'd'\n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd' + abc'd' \n"


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd + a'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + abc'd + abcd'\n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd' + abc'd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + ac'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd + abc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd' + abc'd \n"

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc + a'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Grupo de 2 = { [13], [1] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + bcd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + bcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [7], [11], [15]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + bcd \n"


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd' + abcd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + acd' \n"


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd' + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'd' \n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd + b'cd' \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n"
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Grupo de 2 = { [3], [7] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c \n"


    ## b = 8
    
    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + abc' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + abc'd' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd' + a'cd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + ac'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd' + abc'd' \n"


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + abd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc'd + bcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd' + abc'd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + ac'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [15], [3] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd + abc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd' + abc'd \n"

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc + a'cd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd' + abcd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + acd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [8] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd' + abcd \n"


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + bcd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + bcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + bcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [4], [8], [12], [16]}\n" 
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + cd' \n"


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n" 
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd' \n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + b'cd' \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c \n"


    ## b = 9
    
    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc' + abd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc' + abd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc' + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc' + ac'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + abc' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 2 = { [9], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + abc' \n"

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd' + abc \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + ac'd' + abcd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + abc'd' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc'd' + acd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [9] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + abc'd' + abcd \n"


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd' + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = 'b' + b'c'd + abd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + abd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd' + b'cd' \n"


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n" 
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + ac'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + ac'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n" 
        label += "Grupo de 2 = { [9], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + ac'd' \n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd + abc'd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + b'cd' + abc'd' \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Grupo de 1 = { [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c + abc'd' \n"


    ## b = 10
    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd + abc \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) =  a'b' + b'c'd' + abd \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd + b'c'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abd + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + abd \n"


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + abc'd + abcd' \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + ac'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + abc'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc'd + acd' \n"


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n" 
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + ac'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + b'cd + abc'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n"
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + abc'd\n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd + ac'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [10], [14] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + ac'd \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n" 
        label += "Grupo de 1 = { [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c + abc'd \n"


    ## b = 11
    
    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + abc \n"
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + abc \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc + b'cd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [11], [12] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + abc + b'cd' \n"


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n" 
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + abcd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + acd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n" 
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + abcd \n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n" 
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd + acd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + b'cd' + abcd \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n" 
        label += "Grupo de 2 = { [11], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c + acd \n"


    ## b = 12
    
    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [5], [13], [14]}\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + b'cd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n" 
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + acd' \n"


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n"
        label += "Grupo de 1 = { [12] }\n" 
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd + abcd' \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + acd' \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Grupo de 2 = { [12], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c + acd' \n"

    ## b = 13
    
    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n"
        label += "Grupo de 4 = { [2], [3], [14], [15]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + b'd \n"

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [2], [13], [14]}\n"
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + b'd' \n"

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n"
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + b'c \n"

    ## b = 14
    
    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        label += "Grupo de 4 = { [1], [2], [3], [4]}\n" 
        label += "Grupo de 4 = { [1], [4], [13], [16]}\n"
        label += "Grupo de 4 = { [3], [4], [15], [16]}\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b' + b'd + b'c \n"


    #1	2	3	c   b   a  x
    #5	<=	c	<=	13		
    #6	<=	b	<=	14		
    #7	<=	a	<=	15		
    #8	<=	x	<=	16		

    ### c = 5

    ## b = 6
    
    # a = 7


    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [5], [6], [7], [8]}\n" 
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + a'b \n"
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + bc'd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + bc'd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [7], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + bcd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + abcd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'd + a'c' + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + b'c'd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + b'cd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [3], [6], [7]}\n" 
        label += "Grupo de 2 = { [4], [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'd + ab'cd' \n"


    # a = 8
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + bc'd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + bc'd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + abcd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [8], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bcd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b'd + a'c' + a'bd' + b'c'd' \n"
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + b'c'd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'bd' + b'cd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [8] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + ab'cd' \n"


    # a = 9

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [5], [6], [9], [10]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bc'\n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Grupo de 1 = { [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bc'd' + abcd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [1], [5] }\n"
        label += "Grupo de 2 = { [9], [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + abd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 4 = { [1], [5], [9], [13]}\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b'd + a'c' + c'd' \n"
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Grupo de 2 = { [2], [14] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + b'c'd + bc'd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + b'cd + bc'd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [5], [9] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + ab'cd' + bc'd' \n"


    # a = 10


    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [10], [11] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + abd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 1 = { [12] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bc'd + abcd' \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 2 = { [1], [13] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'b'd + a'c' + b'c'd' + bc'd \n"
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 4 = { [2], [6], [10], [14]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + c'd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 2 = { [3], [15] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + b'cd + bc'd \n"

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        label += "Grupo de 4 = { [1], [2], [5], [6]}\n" 
        label += "Grupo de 2 = { [2], [3] }\n"
        label += "Grupo de 2 = { [6], [10] }\n"
        label += "Grupo de 1 = { [16] }\n"
        label += "Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + ab'cd' + bc'd \n"

    return label
