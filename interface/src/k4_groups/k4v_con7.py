def k4v7(listing):
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
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + a'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [4], [5], [8]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + a'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + bc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + bc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c' + b'cd' ")


    #1	2	3	4   5   a  x
    #7	<=	a	<=	15		
    #8	<=	x	<=	16		

    # a = 7


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 4 = { [1], [4], [5], [8]}")
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + a'c ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + bc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + abc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3] ,[4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = f(a, b, c, d) = a'b' + a'c'd' + bcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [15], [3] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [16], [4] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + a'cd + b'cd' ")


    # a = 8
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + bc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 2 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + abc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + bcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [4], [8]}")
        print("Grupo de 2 = { [16], [4] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd' + b'cd' ")


    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc' + a'c'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 1 = { [11] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + bc'd' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd' + a'c'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [5], [9], [13]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [14], [2] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + bc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [15], [3] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + bc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [16], [4] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + bc'd' ")


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + abd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + abc'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + abc'd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + ac'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd + abc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd' + abc'd ")

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + abc ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + abcd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) =  a'b' + a'c'd' + b'c'd + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + acd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd' + abcd ")


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + abcd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'cd + abcd'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + acd' ")


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [2], [13], [14]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd' + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [4], [13], [16]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'd'")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [14], [15]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c'd + b'cd' ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd' + b'c ")


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
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + a'c ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + bc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + bcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [6], [7]}")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'd + b'cd' ")


    # a = 8
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + bc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + bcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + a'cd' + b'cd' ")


    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc' + a'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + abc'd' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + abd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + ac'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd' + abc'd' ")


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd + a'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + bc'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + bc'd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [6], [10], [14]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + bc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + bc'd")

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + abc ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd' + abcd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + acd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [3], [16] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd' + abcd ")


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd' + abcd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'cd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + acd' ")


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [2], [13], [14]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd' + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [4], [13], [16]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'd' ")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [14], [15]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c'd + b'cd' ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c'd + b'c ")


    ## b = 7
    
    # a = 8
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + abc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + bcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + bcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [7], [8]}")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'c + b'cd' ")


    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + abc' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [7], [11] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc'd' + bcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + abd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + ac'd'")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd' + abc'd' ")


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd + a'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + abc'd + abcd'")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd' + abc'd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + ac'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd + abc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd' + abc'd ")

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc + a'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [7], [11] }")
        print("Grupo de 2 = { [13], [1] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + bcd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [7], [11] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + bcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [7], [11], [15]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [7], [11] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + bcd ")


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd' + abcd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'cd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + acd' ")


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [2], [13], [14]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd' + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [1], [4], [13], [16]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'd' ")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [2], [3], [14], [15]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c'd + b'cd' ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}")
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd + b'c ")


    ## b = 8
    
    # a = 9

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + abc' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + abc'd' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd' + a'cd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + ac'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd' + abc'd' ")


    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + abd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc'd + bcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd' + abc'd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + ac'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [15], [3] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd + abc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd' + abc'd ")

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc + a'cd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd' + abcd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'c'd + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + acd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [8] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + a'cd' + b'cd' + abcd ")


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + bcd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + bcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [8], [12] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + bcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [4], [8], [12], [16]}") 
        print("Funcion simplificada, f(a, b, c, d) = a'b' + cd' ")


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [2], [13], [14]}") 
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd' ")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [2], [3], [14], [15]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + b'cd' ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c ")


    ## b = 9
    
    # a = 10


    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc' + abd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [10] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc' + abd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc' + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc' + ac'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + abc' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + abc' ")

    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [12] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd' + abc ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [13] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + ac'd' + abcd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + abc'd' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [11], [15] }")
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc'd' + acd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + abc'd' + abcd ")


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [12] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd' + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [12] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = 'b' + b'c'd + abd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [12] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + abd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [12] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd' + b'cd' ")


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [2], [13], [14]}") 
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + ac'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [9], [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + ac'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [4], [13], [16]}") 
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + ac'd' ")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [2], [3], [14], [15]}")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd + abc'd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + b'cd' + abc'd' ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c + abc'd' ")


    ## b = 10
    
    # a = 11

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [10], [11] }")
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd + abc ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) =  a'b' + b'c'd' + abd ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd + b'c'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abd + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + abd ")


    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + abc'd + abcd' ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [10], [14] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + ac'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd + abc'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [12], [16] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc'd + acd' ")


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [2], [13], [14]}") 
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + ac'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + b'cd + abc'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [4], [13], [16]}")
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + abc'd")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd + ac'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [10], [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'cd' + ac'd ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [3], [4], [15], [16]}") 
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c + abc'd ")


    ## b = 11
    
    # a = 12

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + abc ")
    
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + abc ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc + b'cd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [11], [12] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + abc + b'cd' ")


    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [2], [13], [14]}") 
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + abcd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + acd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [4], [13], [16]}") 
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + abcd ")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [2], [3], [14], [15]}") 
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd + acd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [2], [14] }")
        print("Grupo de 2 = { [4], [16] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + b'cd' + abcd ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [3], [4], [15], [16]}") 
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c + acd ")


    ## b = 12
    
    # a = 13

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [5], [13], [14]}")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd' + b'cd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [4], [13], [16]}") 
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + acd' ")


    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [2], [3], [14], [15]}")
        print("Grupo de 1 = { [12] }") 
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd + abcd' ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 2 = { [12], [16] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c'd + acd' ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c + acd' ")

    ## b = 13
    
    # a = 14

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [2], [13], [14]}")
        print("Grupo de 4 = { [2], [3], [14], [15]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + b'd ")

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [2], [13], [14]}")
        print("Grupo de 4 = { [1], [4], [13], [16]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'c' + b'd' ")

    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [4], [13], [16]}")
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd' + b'c ")

    ## b = 14
    
    # a = 15

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 4 = { [1], [2], [3], [4]}") 
        print("Grupo de 4 = { [1], [4], [13], [16]}")
        print("Grupo de 4 = { [3], [4], [15], [16]}")
        print("Funcion simplificada, f(a, b, c, d) = a'b' + b'd + b'c ")


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
        print("Grupo de 4 = { [5], [6], [7], [8]}") 
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + a'b ")
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + bc'd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + bc'd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + bcd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + abcd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'd + a'c' + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + b'c'd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + b'cd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [3], [6], [7]}") 
        print("Grupo de 2 = { [4], [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'd + ab'cd' ")


    # a = 8
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + bc'd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + bc'd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + abcd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bcd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b'd + a'c' + a'bd' + b'c'd' ")
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + b'c'd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'bd' + b'cd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [8] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + a'bd' + ab'cd' ")


    # a = 9

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [5], [6], [9], [10]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bc'")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bc'd' + abcd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Grupo de 2 = { [9], [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + abd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 4 = { [1], [5], [9], [13]}")
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b'd + a'c' + c'd' ")
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Grupo de 2 = { [2], [14] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + b'c'd + bc'd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}")
        print("Grupo de 2 = { [5], [9] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + b'cd + bc'd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [5], [9] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + ab'cd' + bc'd' ")


    # a = 10


    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + abd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + bc'd + abcd' ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [1], [13] }")
        print("Funcion simplificada, f(a, b, c, d) = a'b'd + a'c' + b'c'd' + bc'd ")
    
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 4 = { [2], [6], [10], [14]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + c'd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 2 = { [3], [15] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + b'cd + bc'd ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 4 = { [1], [2], [5], [6]}") 
        print("Grupo de 2 = { [2], [3] }")
        print("Grupo de 2 = { [6], [10] }")
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, f(a, b, c, d) = a'c' + a'b'd + ab'cd' + bc'd ")
