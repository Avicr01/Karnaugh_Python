def agrupador(group, pos):
    fun = ""
    #pos = []

    if group == 1:
        if  (pos == [0]):
            fun += " P'Q'R'S' "
        elif (pos == [1]):
            fun += " P'Q'R'S "
        elif (pos == [3]):
            fun += " P'Q'RS' "
        elif (pos == [2]):
            fun += " P'Q'RS "
        elif (pos == [4]):
            fun += " P'QR'S' "
        elif (pos == [5]):
            fun += " P'QR'S "
        elif (pos == [6]):
            fun += " P'QRS "
        elif (pos == [7]):
            fun += " P'QRS' "
        elif (pos == [8]):
            fun += " PQR'S' "
        elif (pos == [9]):
            fun += " PQR'S "
        elif (pos == [10]):
            fun += " PQRS "
        elif (pos == [11]):
            fun += " PQRS' "
        elif (pos == [12]):
            fun += " PQ'R'S' "
        elif (pos == [13]):
            fun += " PQ'R'S "
        elif (pos == [14]):
            fun += " PQ'RS "
        elif (pos == [15]):
            fun += " PQ'RS' "
        
    if group == 2:
        if  (pos == [0,1]):
            fun += " P'Q'R' "
        elif(pos == [0,3]):
            fun += " P'Q'S' "
        elif pos == [0,4]:
            fun += " P'R'S' "
        elif(pos == [0,12]):
            fun += " Q'R'S' "
        elif(pos == [1,2]):
            fun += " P'Q'S "
        elif(pos == [1,5]):
            fun += " P'R'S "
        elif(pos == [1,13]):
            fun += " Q'R'S "
        elif(pos == [2,3]):
            fun += " P'Q'R "
        elif(pos == [2,6]):
            fun += " P'RS "
        elif(pos == [2,14]):
            fun += " Q'RS "
        elif(pos == [3,7]):
            fun += " P'RS' "
        elif(pos == [3,15]):
            fun += " Q'RS' "
        elif(pos == [4,5]):
            fun += " P'QR' "
        elif (pos == [4, 8]):
            fun += " QR'S' "
        elif(pos == [4,7]):
            fun += " P'QS' "
        elif(pos == [5,6]):
            fun += " P'QS "
        elif(pos == [5,9]):
            fun += " QR'S "
        elif(pos == [7,6]):
            fun += " P'QR "
        elif(pos == [6,10]):
            fun += " QRS "
        elif(pos == [7,11]):
            fun += " QRS' "
        elif(pos == [8,9]):
            fun += " PQR' "
        elif(pos == [8,12]):
            fun += " PR'S' "
        elif(pos == [8,11]):
            fun += " PQS' "
        elif(pos == [9,13]):
            fun += " PR'S "
        elif(pos == [9,10]):
            fun += " PQS "
        elif(pos == [10,14]):
            fun += " PRS "
        elif(pos == [10,11]):
            fun += " PQR "
        elif(pos == [11,15]):
            fun += " PRS' "
        elif (pos == [12, 13]):
            fun += " PQ'R' "
        elif (pos == [12,15]):
            fun += " PQ'S' "
        elif (pos == [13,14]):
            fun += " PQ'S "
        elif (pos == [14, 15]):
            fun += " PQ'R "
    if group == 4:
        if  ( pos == [0,1,2,3]):
            fun += " P'Q' "
        elif( pos == [0,1,4,5]):
            fun += " P'R' "
        elif( pos == [0,4,8,12]):
            fun += " R'S' "
        elif( pos == [0,1,12,13]):
            fun += " Q'R'"
        elif( pos == [0,3,12,15]):
            fun += " Q'S' "
        elif(pos == [0,3,4,7]):
            fun += " P'S' "
        elif( pos == [1,5,9,13]):
            fun += " R'S "
        elif( pos == [1,2,5,6]):
            fun += " P'S "
        elif(pos == [1,2,13,14]):
            fun += " Q'S "
        elif(pos == [2,3,6,7]):
            fun += " P'R "
        elif(pos == [2,3,14,15]):
            fun += " Q'R "
        elif(pos == [2,6,10,14]):
            fun += " RS "
        elif(pos == [3,7,11,15]):
            fun += " RS' "
        elif(pos == [4,5,6,7]):
            fun += " P'Q "
        elif(pos == [4,5,8,9]):
            fun += " QR' "
        elif(pos == [4,7,8,11]):
            fun += " QS' "
        elif(pos == [5,6,9,10]):
            fun += " QS "
        elif(pos == [6,7,10,11]):
            fun += " QR "
        elif(pos == [8,9,10,11]):
            fun += " PQ "
        elif(pos == [8,8,12,13]):
            fun += " PR' "
        elif(pos == [8,11,12,15]):
            fun += " PS' "
        elif(pos == [9,10,13,14]):
            fun += " PS "
        elif(pos == [10,11,14,15]):
            fun += " PR "
        elif(pos == [12,13,15,14]):
            fun += " PQ' "
    if group == 8:
        if  (pos == [0,1,2,3,4,5,6,7]):
            fun += " P' "
        elif(pos == [0,1,2,3,12,13,14,15]):
            fun += " Q' "
        elif(pos == [0,3,4,7,8,11,12,15]):
            fun += " S' "
        elif(pos == [0,1,4,5,8,9,12,13]):
            fun += " R' "
        elif(pos == [1,2,5,6,9,10,13,14]):
            fun += " S "
        elif(pos == [4,5,6,7,8,9,10,11]):
            fun += " Q "
        elif(pos == [2,3,6,7,10,11,14,15]):
            fun += " R "
        elif(pos == [8,9,11,10,12,13,14,15]):
            fun += " P "

    return fun + " + "