def agrupador(group, coords):
    fun = ""
    pos = []

    if group == 1:
        if(pos == [0]):
            fun += " P'Q'R'S' "
        elif (pos == [1]):
            fun += " P'Q'R'S "
        elif (pos == [2]):
            fun += " P'Q'RS' "
        elif (pos == [3]):
            fun += " P'Q'RS "
        elif (pos == [4]):
            fun += " P'QR'S' "
        elif (pos == [5]):
            fun += " P'QR'S "
        elif (pos == [6]):
            fun += " P'QRS' "
        elif (pos == [7]):
            fun += " P'QRS "
        elif (pos == [8]):
            fun += " PQ'R'S' "
        elif (pos == [9]):
            fun += " PQ'R'S "
        elif (pos == [10]):
            fun += " PQ'RS' "
        elif (pos == [11]):
            fun += " PQ'RS "
        elif (pos == [12]):
            fun += " PQR'S' "
        elif (pos == [13]):
            fun += " PQR'S "
        elif (pos == [14]):
            fun += " PQRS' "
        elif (pos == [15]):
            fun += " PQRS "
    if group == 2:
        if(pos == [0,1]):
            fun += " P'Q'R' "
        elif(pos == [0,2]):
            fun += " P'Q'S' "
        elif pos == [0, 4]:
            fun += " P'R'S' "
        elif(pos == [0,8]):
            fun += " Q'R'S' "
        elif(pos == [1,3]):
            fun += " P'Q'S "
        elif(pos == [1,5]):
            fun += " P'R'S "
        elif(pos == [1,9]):
            fun += " Q'R'S "
        elif(pos == [2,3]):
            fun += " P'Q'R "
        elif(pos == [3,7]):
            fun += " P'RS "
        elif(pos == [3,11]):
            fun += " Q'RS "
        elif(pos == [2,6]):
            fun += " P'RS' "
        elif(pos == [2,10]):
            fun += " Q'RS' "
        elif(pos == [4,5]):
            fun += " P'QR' "
        elif (pos == [4, 12]):
            fun += " QR'S' "
        elif(pos == [4,6]):
            fun += " P'QS' "
        elif(pos == [5,7]):
            fun += " P'QS "
        elif(pos == [5,13]):
            fun += " QR'S "
        elif(pos == [6,7]):
            fun += " P'QR "
        elif(pos == [7,15]):
            fun += " QRS "
        elif(pos == [6,14]):
            fun += " QRS' "
        elif(pos == [12,13]):
            fun += " PQR' "
        elif(pos == [8,12]):
            fun += " PR'S' "
        elif(pos == [12,14]):
            fun += " PQS' "
        elif(pos == [9,13]):
            fun += " PR'S "
        elif(pos == [13,15]):
            fun += " PQS "
        elif(pos == [11,15]):
            fun += " PRS "
        elif(pos == [14,15]):
            fun += " PQR "
        elif(pos == [10,14]):
            fun += " PRS' "
        elif (pos == [8, 9]):
            fun += " PQ'R' "
        elif (pos == [8,10]):
            fun += " PQ'S' "
        elif (pos == [9,11]):
            fun += " PQ'S "
        elif (pos == [10, 11]):
            fun += " PQ'R "
    if group == 4:
        if( pos == [0,1,2,3]):
            fun += " P'Q' "
        elif( pos == [0,1,4,5]):
            fun += " P'R' "
        elif( pos == [0,4,8,12]):
            fun += " R'S' "
        elif( pos == [0,1,8,9]):
            fun += " Q'R'"
        elif( pos == [0,2,8,10]):
            fun += " Q'S' "
        elif(pos == [0,2,4,6]):
            fun += " P'S' "
        elif( pos == [1,5,9,13]):
            fun += " R'S "
        elif( pos == [1,3,5,7]):
            fun += " P'S "
        elif(pos == [1,3,9,11]):
            fun += " Q'S "
        elif(pos == [2,3,6,7]):
            fun += " P'R "
        elif(pos == [2,3,10,11]):
            fun += " Q'R "
        elif(pos == [3,7,11,15]):
            fun += " RS "
        elif(pos == [2,6,10,14]):
            fun += " RS' "
        elif(pos == [4,5,6,7]):
            fun += " P'Q "
        elif(pos == [4,5,12,13]):
            fun += " QR' "
        elif(pos == [4,6,12,14]):
            fun += " QS' "
        elif(pos == [5,7,13,15]):
            fun += " QS "
        elif(pos == [6,7,14,15]):
            fun += " QR "
        elif(pos == [12,13,14,15]):
            fun += " PQ "
        elif(pos == [8,9,12,13]):
            fun += " PR' "
        elif(pos == [8,10,12,14]):
            fun += " PS' "
        elif(pos == [9,11,13,15]):
            fun += " PS "
        elif(pos == [10,11,14,15]):
            fun += " PR "
        elif(pos == [8,9,10,11]):
            fun += " PQ' "
    if group == 8:
        if(pos == [0,1,2,3,4,5,6,7]):
            fun += " P' "
        elif(pos == [0,1,2,3,8,9,10,11]):
            fun += " Q' "
        elif(pos == [0,2,4,6,8,10,12,14]):
            fun += " S' "
        elif(pos == [0,1,4,5,8,9,12,13]):
            fun += " R' "
        elif(pos == [1,3,5,7,9,11,13,15]):
            fun += " S "
        elif(pos == [4,5,6,7,12,13,14,15]):
            fun += " Q "
        elif(pos == [2,3,6,7,10,11,14,15]):
            fun += " R "
        elif(pos == [8,9,10,11,12,13,14,15]):
            fun += " P "

    return fun + " + "