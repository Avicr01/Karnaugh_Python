from tkinter import *
from tkinter import filedialog, messagebox
import tkinter
from PIL import ImageTk, Image
from numpy.core.numeric import array_equal
from src.k2v import kmaps2 
from src.k3v import kmaps3 
from src.k4v import kmaps4 
import grouping as gp


import random 
import numpy as np

interface = Tk()

#----Instancias de imagenes ---------------

PicTable2 = ImageTk.PhotoImage(file="interface/images/2v.png")
PicTable3 = ImageTk.PhotoImage(file="interface/images/3v.png")
PicTable4 = ImageTk.PhotoImage(file="interface/images/4v.png")
PicK2 = ImageTk.PhotoImage(file="interface/images/kar2.png")
PicK3 = ImageTk.PhotoImage(file="interface/images/kar3.png")
PicK4 = ImageTk.PhotoImage(file="interface/images/kar4.png")
#-----------------Positions------------------------------
def Posicion(j,i):
    if   i == 0 and j == 0:
        return 0
    if   i == 1 and j == 0:
        return 1
    if   i == 2 and j == 0:
        return 2
    if   i == 3 and j == 0:
        return 3
    if   i == 0 and j == 1:
        return 4
    if   i == 1 and j == 1:
        return 5
    if   i == 2 and j == 1:
        return 6
    if   i == 3 and j == 1:
        return 7
    if   i == 0 and j == 2:
        return 8
    if   i == 1 and j == 2:
        return 9
    if   i == 2 and j == 2:
        return 10
    if   i == 3 and j == 2:
        return 11
    if   i == 0 and j == 3:
        return 12
    if   i == 1 and j == 3:
        return 13
    if   i == 2 and j == 3:
        return 14
    if   i == 3 and j == 3:
        return 15

#---- Color aleatorio de los cuadrados ---------------

def rancolor():
    return "#" + ''.join(random.choice('0123456789AB') for j in range(6))

#------------Funcion evaluar mapas de Karnaugh -------------

def calcular(arr, ventana, Hventana, var):
    label = ""
    listing = []
    for i in range(len(arr)):
        listing.append(arr[i].get())
    print("\n")

    # Canvas
    canvas = tkinter.Canvas(ventana, height=400, width=500)

    # Funcion de Mapas de Karnaugh
    if var == 2:
        label= kmaps2(listing, label)

        canvas.place(x = 280, y = 92)
        canvas_label = tkinter.Canvas(ventana, height=300, width=250)

        # Dibujar el mapa  de 2222222222222222222222222222222222
        karnaugh_img = canvas.create_image((0,0), image=PicK2, anchor=tkinter.N + tkinter.W)
        fila1 = "{}          {}".format(listing[0], listing[1])
        fila2 = "\n\n{}          {}".format(listing[2], listing[3])
        label_arr = canvas.create_text((120, 110), text=fila1+fila2, font="Calibri 18 bold")
        
        # Poner la funcion simplificada 
        canvas_label.place(x = 40, y = 280)
        label_fun = canvas_label.create_text((120, 30), text=label)
        
        # Crear grupos 
        count = sum(map(lambda x: x == 1, listing))
        
        if count == 1:
            for x in range(0, len(listing)):
                if listing[x] == 1:
                    if x == 0:
                        canvas.create_rectangle(70, 60, 110, 100, outline=rancolor())
                    elif x == 1:
                        canvas.create_rectangle(70+60, 60, 110+60, 100, outline=rancolor())
                    elif x == 2:
                        canvas.create_rectangle(70, 60+60, 110, 100+60, outline=rancolor())
                    elif x == 3:
                        canvas.create_rectangle(70+60, 60+60, 110+60, 100+60, outline=rancolor())
        elif count == 4: 
            canvas.create_rectangle(70, 60, 110+60, 100+60, outline=rancolor())
        elif count == 2: 
            # Horizontal 
            if listing[0] + listing[1] == 2:
                canvas.create_rectangle(70, 60, 110+60, 100, outline=rancolor())
            elif listing[2] + listing[3] == 2:
                canvas.create_rectangle(70, 60+60, 110+60, 100+60, outline=rancolor())
            # Vertical
            elif listing[0] + listing[2] == 2:
                canvas.create_rectangle(70, 60, 110, 100+60, outline=rancolor())
            elif listing[1] + listing[3] == 2:
                canvas.create_rectangle(70+60, 60, 110+60, 100+60, outline=rancolor())
            # Impares
            elif listing[0] + listing[3] == 2:
                canvas.create_rectangle(70, 60, 110, 100, outline='red')
                canvas.create_rectangle(70+60, 60+60, 110+60, 100+60, outline='blue')
            elif listing[1] + listing[2] == 2:
                canvas.create_rectangle(70+60, 60, 110+60, 100, outline='red')
                canvas.create_rectangle(70, 60+60, 110, 100+60, outline='blue')
        elif count == 3:
            # Horizontal 
            if listing[0] + listing[1] == 2:
                canvas.create_rectangle(70, 60, 110+60, 100, outline='blue')
            if listing[2] + listing[3] == 2:
                canvas.create_rectangle(70, 60+60, 110+60, 100+60, outline='blue')
            # Vertical
            if listing[0] + listing[2] == 2:
                canvas.create_rectangle(70, 60, 110, 100+60, outline='red')
            if listing[1] + listing[3] == 2:
                canvas.create_rectangle(70+60, 60, 110+60, 100+60, outline='red')

    elif var == 3:
        label = kmaps3(listing, label)

        canvas.place(x = 280, y = 92)
        canvas_label = tkinter.Canvas(ventana, height=300, width=400)

        # Dibujar el mapa
        karnaugh_img = canvas.create_image((0,0), image=PicK3, anchor=tkinter.N + tkinter.W)
        fila1 = "{}            {}            {}           {}".format(listing[0], listing[1], listing[3], listing[2])
        fila2 = "\n\n{}            {}            {}           {}".format(listing[4], listing[5], listing[7], listing[6])
        
        # Suma de cada linea
        line1 = listing[0] + listing[1] + listing[3] + listing[2]
        line2 = listing[4] + listing[5] + listing[7] + listing[6]

        # Arreglos 
        arr1 = np.array([listing[0] , listing[1] , listing[3] , listing[2]])
        arr2 = np.array([listing[4] , listing[5] , listing[7] , listing[6]])
        arr = np.append(arr1, arr2)
        arr2d = np.vstack((arr1, arr2))
        print(arr2d)

        label_tuple = canvas.create_text((205, 110), text=fila1+fila2, font="Calibri 18 bold")
        
        # Poner la funcion simplificada 
        canvas_label.place(x = 300, y = 280)
        label_fun = canvas_label.create_text((150, 60), text=label)
        
        # Crear grupos 
        count = sum(map(lambda x: x == 1, listing))
        
        x1 = 80
        x2 = 120 
        y1 = 60 
        y2 = 100
        hor = 72
        ver = 60
        if count == 1:
            for i in range(0, len(listing)):
                if arr[i] == 1:
                    print(i)
                    if line1 == 1:
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(0), y2+ver*(0), outline=rancolor())
                    else:
                        canvas.create_rectangle(((i-4)*hor)+x1+hor*(0), y1+ver*(1), ((i-4)*hor)+x2+hor*(0), y2+ver*(1), outline=rancolor())

        elif count == 2 or count == 3: 
            for j in range(0, 4):
                for i in range(0, 2):
                    # De uno 
                    if arr2d[i, j] == 1 and arr2d[i - 1, j] == 0 and arr2d[i, j - 3] == 0 and arr2d[i, j - 1] == 0:
                        canvas.create_rectangle((j*hor)+x1+hor*(0), y1+ver*(i), (j*hor)+x2+hor*(0), y2+ver*(i), outline=rancolor())

                    # Verticales de 2
                    if arr2d[i, j] == 1 and arr2d[i - 1, j] == 1 and arr2d[i, j - 3] == 0 and arr2d[i, j - 1] == 0:
                        canvas.create_rectangle((j*hor)+x1+hor*(0), y1+ver*(0), (j*hor)+x2+hor*(0), y2+ver*(1), outline=rancolor())
                        
            for j in range(0, 3):
                for i in range(0, 2):
                    # Horizontales de 2
                    if arr2d[i, j] == 1 and arr2d[i, j - 1] == 0 and arr2d[i, j - 2] == 0 and arr2d[i, j - 3] == 1:
                        canvas.create_rectangle((j*hor)+x1+hor*(0), y1+ver*(i), (j*hor)+x2+hor*(1), y2+ver*(i), outline=rancolor())

            if listing[0] + listing[2] == 2:
                canvas.create_rectangle(x1, y1, x2, y2, outline='red')
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
            elif listing[4] + listing[6] == 2:
                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')

            for i in range(0, 2):
                for j in range(0, 2):
                    if np.array_equal(arr2d[j][i:i+3], [1, 1, 1]):
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(j), (i*hor)+x2+hor*(1), y2+ver*(j), outline=rancolor())
                        canvas.create_rectangle(((i+1)*hor)+x1+hor*(0), y1+ver*(j), ((i+1)*hor)+x2+hor*(1), y2+ver*(j), outline=rancolor())

            if count == 3:
                for i in range(0, 2):
                    if np.array_equal(arr2d[i][:], [1, 1, 0, 1]):
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(i), x2+hor*(1), y2+ver*(i), outline=rancolor())
                    if np.array_equal(arr2d[i][:], [1, 0, 1, 1]):
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(i), x2+hor*(3), y2+ver*(i), outline=rancolor())

        elif count == 5 or count == 4:
            sq4 = 0
            sqEXT = 0
            vertices = 0

            # Horizontal grupos de 4 
            if line1 == 4:
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
            if line2 == 4:
                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())

            # Cuadrado
            for i in range (0,3): 
                if np.array_equal(arr1[i:i+2], [1, 1]) and np.array_equal(arr2[i:i+2], [1, 1]):
                    canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(1), y2+ver*(1), outline= rancolor())
                    sq4 = 1
            
            if np.array_equal(arr1, [1, 0, 0, 1]) and np.array_equal(arr2, [1, 0, 1, 1]):
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
            elif np.array_equal(arr1, [1, 0, 0, 1]) and np.array_equal(arr2, [1, 1, 0, 1]):
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
            elif np.array_equal(arr1, [1, 1, 0, 1]) and np.array_equal(arr2, [1, 0, 0, 1]):
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
            elif np.array_equal(arr1, [1, 0, 1, 1]) and np.array_equal(arr2, [1, 0, 0, 1]):
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
            elif np.array_equal(arr1, [1, 0, 0, 1]) and not np.array_equal(arr2, [1, 0, 0, 1]):
                canvas.create_rectangle(x1, y1, x2, y2, outline='red')
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                vertices = 1
            elif np.array_equal(arr2, [1, 0, 0, 1]) and not np.array_equal(arr1, [1, 0, 0, 1]):
                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                vertices = 1

            for j in range(0, 4):
                for i in range(0, 2):
                    # De uno 
                    if arr2d[i, j] == 1 and arr2d[i - 1, j] == 0 and arr2d[i, j - 3] == 0 and arr2d[i, j - 1] == 0:
                        canvas.create_rectangle((j*hor)+x1+hor*(0), y1+ver*(i), (j*hor)+x2+hor*(0), y2+ver*(i), outline=rancolor())

                    # Verticales de 2
                    if arr2d[i, j] == 1 and arr2d[i - 1, j] == 1 and arr2d[i, j - 3] == 0 and arr2d[i, j - 1] == 0:
                        canvas.create_rectangle((j*hor)+x1+hor*(0), y1+ver*(0), (j*hor)+x2+hor*(0), y2+ver*(1), outline=rancolor())
                        
            for j in range(0, 3):
                for i in range(0, 2):
                    # Horizontales de 2
                    if arr2d[i, j] == 1 and arr2d[i, j - 1] == 0 and arr2d[i, j - 2] == 0 and arr2d[i, j - 3] == 1 and sq4 == 0:
                        canvas.create_rectangle((j*hor)+x1+hor*(0), y1+ver*(i), (j*hor)+x2+hor*(1), y2+ver*(i), outline=rancolor())


            if count == 4:
                # Patrones de tres juntos 
                if np.array_equal(arr1, [1, 1, 1, 0]):
                    if (arr2[0] == arr2[2] == 0):
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                    elif arr2[0] == 1:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                    elif arr2[2] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())

                if np.array_equal(arr2, [1, 1, 1, 0]):
                    if arr1[0] == arr1[2] == 0:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())
                    elif arr1[0] == 1:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())
                    elif arr1[2] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())

                if np.array_equal(arr1, [0, 1, 1, 1]):
                    if arr2[1] == arr2[3] == 0:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                    elif arr2[1] == 1:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    elif arr2[3] == 1:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())

                if np.array_equal(arr2, [0, 1, 1, 1]):
                    if arr1[1] == arr1[3] == 0:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())
                    elif arr1[1] == 1:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    elif arr1[3] == 1:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())
                        
                
                # Patrones separados
                if np.array_equal(arr1, [1, 0, 1, 1]):
                    if (arr2[0] == arr2[2] == 0):
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")
                    elif arr2[0] == 1:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    elif arr2[2] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline="red")

                if np.array_equal(arr2, [1, 0, 1, 1]): # Este es mi ejemplo
                    if arr1[0] == arr1[2] == 0:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline="red")
                    elif arr1[0] == 1:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    elif arr1[2] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline="red")

                if np.array_equal(arr1, [1, 1, 0, 1]):
                    if arr2[1] == arr2[3] == 0:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")
                    elif arr2[1] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")
                    elif arr2[3] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())

                if np.array_equal(arr2, [1, 1, 0, 1]):
                    if arr1[1] == arr1[3] == 0:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")
                    elif arr1[1] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")
                    elif arr1[3] == 1:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())

                for i in range(0, 2):
                    for j in range(0, 2):
                        if np.array_equal(arr1[i:i+3], [1, 0, 1]) and np.array_equal(arr2[i:i+3], [1, 0, 1]):
                            canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(0), y2+ver*(1), outline=rancolor())
                            canvas.create_rectangle((i*hor)+x1+hor*(2), y1+ver*(0), (i*hor)+x2+hor*(2), y2+ver*(1), outline=rancolor())
                
                            

            if count == 5:
                # Patrones de tres juntos 

                if np.array_equal(arr1, [0, 1, 1, 1]):
                    if sq4 == 0:
                        if arr2[0] + arr2[2] == 2 or arr2[0] + arr2[1] == 2 or vertices == 1:
                            canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                            canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                        elif arr2[1] + arr2[3] == 2:
                            canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                    else:
                        if arr2[1] + arr2[2] == 2 and arr1[3] == 1:
                            canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                        if arr2[2] + arr2[3] == 2 and arr1[2] == 1:
                                canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())

                if np.array_equal(arr2, [0, 1, 1, 1]):
                    if sq4 == 0:
                        if arr1[0] + arr1[2] == 2 or arr1[0] + arr1[1] == 2 or vertices == 1:
                            canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                            canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())
                        elif arr1[1] + arr1[3] == 2:
                            canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())
                    else:
                        if arr1[1] + arr1[2] == 2 and arr2[3] == 1:
                            canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        if arr1[2] + arr1[3] == 2 and arr2[2] == 1:
                                canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())

                if np.array_equal(arr1, [1, 1, 1, 0]):
                    if sq4 == 0:
                        if arr2[1] + arr2[3] == 2 or arr2[2] + arr2[3] == 2 or vertices == 1:
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                            canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                        elif arr2[0] + arr2[2] == 2:
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                    else:
                        if arr2[1] + arr2[2] == 2 and arr1[0] == 1:
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                        if arr2[0] + arr2[1] == 2 and arr1[2] == 1:
                                canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())

                if np.array_equal(arr2, [1, 1, 1, 0]):
                    if sq4 == 0:
                        if arr1[1] + arr1[3] == 2 or arr1[2] + arr1[3] == 2 or vertices == 1:
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                            canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())
                        elif arr1[0] + arr1[2] == 2:
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                    else:
                        if arr1[1] + arr1[2] == 2 and arr2[0] == 1:
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        if arr1[0] + arr1[1] == 2 and arr2[2] == 1:
                                canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())

                # Patrones separados
                if np.array_equal(arr1, [1, 0, 1, 1]):
                    if np.array_equal(arr2, [1, 0, 0, 1]):
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    elif sq4 == 1 or np.array_equal(arr2, [1, 0, 1, 0]):
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                            canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")
                    else:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")

                if np.array_equal(arr2, [1, 0, 1, 1]):
                    if np.array_equal(arr1, [1, 0, 0, 1]):
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    elif sq4 == 1 or np.array_equal(arr1, [1, 0, 1, 0]):
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline="red")
                            canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline="red")
                    else:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline="red")

                if np.array_equal(arr1, [1, 1, 0, 1]):
                    if np.array_equal(arr2, [1, 0, 0, 1]):
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                    elif sq4 == 1 or np.array_equal(arr2, [0, 1, 0, 1]):
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                            canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")
                    else:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline="red")

                if np.array_equal(arr2, [1, 1, 0, 1]):
                    if np.array_equal(arr1, [1, 0, 0, 1]):
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                    elif sq4 == 1 or np.array_equal(arr1, [0, 1, 0, 1]):
                            canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline="red")
                            canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline="red")
                    else:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline="red")
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline="red")
                    
        elif count == 6:
            # Horizontal grupos de 4 
            if line1 == 4:
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
            if line2 == 4:
                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())

            if listing[0] + listing[2] + listing[4] + listing[6] == 4:
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                
            # Cuadrados grupos de 4
            for i in range(0,3): 
                if np.array_equal(arr1[i:i+2], [1, 1]) and  np.array_equal(arr2[i:i+2], [1, 1]):
                    canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(1), y2+ver*(1), outline=rancolor())

            # Verticales
            for i in range(0, 2):
                if (np.array_equal(arr1[i:i+3], [1, 0, 1]) and line2 == 4) or (np.array_equal(arr2[i:i+3], [1, 0, 1]) and line1 == 4):
                    canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(0), y2+ver*(1), outline=rancolor())
                    canvas.create_rectangle((i*hor)+x1+hor*(2), y1+ver*(0), (i*hor)+x2+hor*(2), y2+ver*(1), outline=rancolor())

                if (np.array_equal(arr1[i:i+3], [1, 0, 1]) and line2 == 4) or (np.array_equal(arr2[i:i+3], [1, 0, 1]) and line1 == 4):
                    canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(0), y2+ver*(1), outline=rancolor())
                    canvas.create_rectangle((i*hor)+x1+hor*(2), y1+ver*(0), (i*hor)+x2+hor*(2), y2+ver*(1), outline=rancolor())

            # Separadas
            for row in range(0, 2):
                for col in range(0, 3):
                    if arr2d[row][col] == 1 and arr2d[row][col-1] == 0 and arr2d[row][col+1] == 0 and arr2d[row-1][col] == 0:
                            canvas.create_rectangle(((col)*hor)+x1+hor*(0), ((row)*ver)+y1+ver*(0), ((col)*hor)+x2+hor*(0), ((row)*ver)+y2+ver*(0), outline=rancolor())
            
            # Casos especiales
            if arr2d[1][0] == 0 and arr2d[0][1] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline='blue')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='blue')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())

            if arr2d[0][0] == 0 and arr2d[1][1] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())

            if arr2d[0][2] == 0 and arr2d[1][3] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(0), outline='blue')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='blue')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())

            if arr2d[1][2] == 0 and arr2d[0][3] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())

            if arr2d[1][0] == 0 and arr2d[0][3] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())

            if arr2d[0][0] == 0 and arr2d[1][3] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())

            if arr2d[0][1] == 0 and arr2d[1][2] == 0:
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())

            if arr2d[1][1] == 0 and arr2d[0][2] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())

            # Puros grupos de 2
            if arr2d[0][0] == 0 and arr2d[1][2] == 0:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline=rancolor())

            if arr2d[1][0] == 0 and arr2d[0][2] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())

            if arr2d[0][1] == 0 and arr2d[1][3] == 0:
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline=rancolor())

            if arr2d[1][1] == 0 and arr2d[0][3] == 0:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline=rancolor())
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())

        elif count == 7:
            for x in range(0, len(listing)):
                if listing[x] == 0:
                    if x == 0:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    elif x == 1:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    elif x == 2:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    elif x == 3:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline=rancolor())
                    elif x == 4:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    elif x == 5:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    elif x == 6:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())
                    elif x == 7:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline=rancolor())
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline=rancolor())

        elif count == 8: 
            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')

    elif var == 4:
        count = sum(map(lambda x: x == 1, listing))

        canvas.place(x = 280, y = 92)

        canvas_label = tkinter.Canvas(ventana, height=300, width=400)
        canvas_label.place(x = 300, y = 500)

        # Dibujar el mapa de cuatro 4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        karnaugh_img = canvas.create_image((0,0), image=PicK4, anchor=tkinter.N + tkinter.W)
        fila1 = "{}            {}             {}          {}".format(listing[0], listing[1], listing[3], listing[2])
        fila2 = "\n\n{}             {}            {}          {}".format(listing[4], listing[5], listing[7], listing[6])
        fila3 = "\n\n{}             {}            {}          {}".format(listing[12], listing[13], listing[15], listing[14])
        fila4 = "\n\n{}             {}            {}          {}".format(listing[8], listing[9], listing[11], listing[10])
        

        # Suma de cada linea
        line1 = listing[0] + listing[1] + listing[3] + listing[2]
        line2 = listing[4] + listing[5] + listing[7] + listing[6]
        line3 = listing[12] + listing[13] + listing[15] + listing[14]
        line4 = listing[8] + listing[9] + listing[11] + listing[10]
        
        col1 = listing[0] + listing[4] + listing[12] + listing[8]
        col2 = listing[1] + listing[5] + listing[13] + listing[9]
        col3 = listing[3] + listing[7] + listing[15] + listing[11]
        col4 = listing[2] + listing[6] + listing[14] + listing[10]

        # Arreglos 
        arr1 = np.array([listing[0] , listing[1] , listing[3] , listing[2]])
        arr2 = np.array([listing[4] , listing[5] , listing[7] , listing[6]])
        arr3 = np.array([listing[12] , listing[13] , listing[15] , listing[14]])
        arr4 = np.array([listing[8] , listing[9] , listing[11] , listing[10]])
        arr2d = np.vstack((arr1, arr2))
        arr2d = np.vstack((arr2d, arr3))
        arr2d = np.vstack((arr2d, arr4))
        print(arr2d)
        

        kmaps4(listing)


        label_arr = canvas.create_text((210, 175), text=fila1+fila2+fila3+fila4, font="Calibri 18 bold")
        
        # Crear grupos 
        x1 = 85
        x2 = 125 
        y1 = 70 
        y2 = 110
        hor = 72
        ver = 60
        #creacion de iterador
        iterador = 0
        counter = line1 + line2 + line3 + line4
        
        GroupsPos = { }
        
        # Banderas
        grupo3v = False 
        grupo3h = False 
        grupo4v = False 
        grupo4h = False 
        grupo4h2 = False 
        grupo4c = False
        grupo6v = False 
        grupo6h = False 
        grupo8v = False 
        grupo8h = False 
        grupo12v = False 
        grupo12h = False 

        # Grupos solitarios
        # Leyenda: row, column
        # Leyenda: fila, columna
        
        if counter == 16:
            canvas.create_rectangle(0*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*3, outline=rancolor())
            label = "F = 0   "
            arr2d = np.zeros((4, 4), dtype=int)


        for j in range(0, 4):
            for i in range(0, 4):
                # De uno 
                if arr2d[i, j] == 1 and arr2d[i - 1, j] == 0 and arr2d[i - 3, j] == 0 and arr2d[i, j - 3] == 0 and arr2d[i, j - 1] == 0:
                    canvas.create_rectangle(j*hor+x1, y1+ver*i, j*hor+x2, y2+ver*i, outline=rancolor())
                    arr2d[i, j] = 0
                    label += gp.agrupador(1, [Posicion(i,j)])

            # Grupos de 2
               # Verticales de 2
                if arr2d[i, j] == 1 and arr2d[i - 1, j] == 1 \
                    and arr2d[i, j - 3] == 0 and arr2d[i, j - 1] == 0 \
                    and arr2d[i-1, j - 3] == 0 and arr2d[i-1, j - 1] == 0 \
                    and arr2d[i - 2, j] == 0 and arr2d[i - 3, j] == 0:
                    if i == 0:
                        canvas.create_rectangle(x1+hor*j, y1+ver*(0), x2+hor*j, y2+ver*(0), outline='red')
                        canvas.create_rectangle(x1+hor*j, y1+ver*(3), x2+hor*j, y2+ver*(3), outline='red')

                        label += gp.agrupador(2,[ j , (j+12)])
                        #print([ j , (j+12)])
                    else:
                        canvas.create_rectangle(j*hor+x1, y1+ver*(i - 1), j*hor+x2, y2+ver*i, outline=rancolor())
                    
                    arr2d[i, j] = 0
                    arr2d[i-1, j] = 0
                    label += gp.agrupador(2, [Posicion(i-1,j), Posicion(i,j)])
                    #print([Posicion(i-1,j), Posicion(i,j)])

               # Horizontales de 2
                if arr2d[i, j] == 1 and arr2d[i, j-1] == 1 \
                    and arr2d[i - 3, j] == 0 and arr2d[i - 1, j] == 0 \
                    and arr2d[i - 3, j-1] == 0 and arr2d[i - 1, j-1] == 0 \
                    and arr2d[i, j - 2] == 0 and arr2d[i, j - 3] == 0:
                    if j == 0:
                        canvas.create_rectangle(x1+hor*0, y1+ver*(i), x2+hor*0, y2+ver*(i), outline='red')
                        canvas.create_rectangle(x1+hor*3, y1+ver*(i), x2+hor*3, y2+ver*(i), outline='red')
                        label += gp.agrupador(2,[(i+3*i),(i+3*i)+3])
                        #print([(i+3*i),(i+3*i)+3])
                    else:
                        canvas.create_rectangle((j - 1)*hor+x1, y1+ver*i, j*hor+x2, y2+ver*i, outline=rancolor())
                    arr2d[i, j] = 0
                    arr2d[i, j-1] = 0
                    label += gp.agrupador(2, [Posicion(i,j-1), Posicion(i,j)])
                    #print([Posicion(i,j-1), Posicion(i,j)])
                    
                iterador+=1

        contador8s = 0
        for i in range(0, 4):
            tmp = np.ones((4), dtype=int)
            tmp2 = np.zeros((4), dtype=int)
            if counter >= 12:
                if np.array_equal(tmp, arr2d[i][:]) and \
                    np.array_equal(tmp, arr2d[i-1][:]) and grupo12h == False and grupo8h == False:
                            contador8s += 1
                if np.array_equal(tmp, arr2d[:, i]) and \
                    np.array_equal(tmp, arr2d[:, i-1]) and grupo12v == False and grupo8v == False:
                        contador8s += 1
            if counter < 12:
           # Horizontales de 8
                if np.array_equal(tmp, arr2d[i][:]) and \
                    np.array_equal(tmp, arr2d[i-1][:]) and grupo12h == False and grupo8h == False:
                        contador8s += 1
                        grupo8h = True
                        if i == 0:
                            canvas.create_rectangle(x1+hor*0, y1+ver*(0), x2+hor*3, y2+ver*(0), outline='red')
                            canvas.create_rectangle(x1+hor*0, y1+ver*(3), x2+hor*3, y2+ver*(3), outline='red')
                            label+= gp.agrupador(8, [0,1,2,3,12,13,14,15])
                        else:
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i - 1), 3*hor+x2, y2+ver*i, outline=rancolor())
                        if np.array_equal(tmp2, arr2d[i-2][:]) and \
                        np.array_equal(tmp2, arr2d[i-3][:]):
                            arr2d[i][:] = [0, 0, 0, 0]
                            arr2d[i-1][:] = [0, 0, 0, 0]
                        label+=gp.agrupador(8,[(0+4*(i-1)) , (1+4*(i-1)) ,(2+4*(i-1)) , (3+4*(i-1)) , (4+4*(i-1)) , (5+4*(i-1)) , (6+4*(i-1)) , (7+4*(i-1))])
                        print([(0+4*(i-1)) , (1+4*(i-1)) ,(2+4*(i-1)) , (3+4*(i-1)) , (4+4*(i-1)) , (5+4*(i-1)) , (6+4*(i-1)) , (7+4*(i-1))])
                        print("individual")
                    
           # Verticales de 8
                if np.array_equal(tmp, arr2d[:, i]) and \
                    np.array_equal(tmp, arr2d[:, i-1]) and grupo12v == False and grupo8v == False:
                        contador8s += 1
                        if i == 0:
                            canvas.create_rectangle(x1+hor*0, y1+ver*(0), x2+hor*0, y2+ver*(3), outline='#93ac53')
                            canvas.create_rectangle(x1+hor*3, y1+ver*(0), x2+hor*3, y2+ver*(3), outline='#93ac53')
                            label+= gp.agrupador(8, [0,3,4,7,8,11,12,15])
                        else:
                            canvas.create_rectangle((i-1)*hor+x1, y1+ver*(0), i*hor+x2, y2+ver*3, outline=rancolor())

                        grupo8v = True
                        if np.array_equal(tmp2, arr2d[:][i-2]) and \
                        np.array_equal(tmp2, arr2d[:][i-3]):
                            arr2d[:][i-2] = [0, 0, 0, 0]
                            arr2d[:][i-3] = [0, 0, 0, 0]
                        label += gp.agrupador(8, [0+1*(i-1),1+1*(i-1),4+1*(i-1),5+1*(i-1),8+1*(i-1),9+1*(i-1),12+1*(i-1),13+1*(i-1)])
                        print([0+1*(i-1),1+1*(i-1),4+1*(i-1),5+1*(i-1),8+1*(i-1),9+1*(i-1),12+1*(i-1),13+1*(i-1)])
                        print("individual")


        for j in range(0, 4):
            for i in range(0, 4):
            # Horizontales de 6
                if counter < 12 or ((counter == 12 or counter == 13) and contador8s < 2):
                    if arr2d[i, j] == 1 and arr2d[i, j-1] == 1 and arr2d[i, j-2] and arr2d[i, j-3] == 0 and \
                       arr2d[i-1, j] == 1 and arr2d[i-1, j-1] == 1 and arr2d[i-1, j-2] and arr2d[i-1, j-3] == 0 and \
                           grupo12h == False and grupo8h == False and grupo6h == False:
                        print("HELP")
                        if i == 0 and j == 0:
                            canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(2*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="green")
                            canvas.create_rectangle(2*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="green")
                        elif i == 0 and j == 1:
                            canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(0*hor+x1, y1+ver*0, 1*hor+x2, y2+ver*0, outline="green")
                            canvas.create_rectangle(0*hor+x1, y1+ver*3, 1*hor+x2, y2+ver*3, outline="green")
                        elif i == 0:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(0), j*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="red")
                        elif j == 0:
                            canvas.create_rectangle(2*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline=rancolor())
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="red")
                        elif j == 1:
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 1*hor+x2, y2+ver*i, outline=rancolor())
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="red")
                        else:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i-1), j*hor+x2, y2+ver*i, outline=rancolor())
                            canvas.create_rectangle((j-2)*hor+x1, y1+ver*(i-1), (j-1)*hor+x2, y2+ver*i, outline=rancolor())

                    tmp_arr = np.zeros((4, 4), dtype=int)
                    tmp_arr[i, j] = 1
                    tmp_arr[i, j-1] = 1
                    tmp_arr[i, j-2] = 1
                    tmp_arr[i-1, j] = 1
                    tmp_arr[i-1, j-1] = 1
                    tmp_arr[i-1, j-2] = 1
                    if np.array_equal(tmp_arr, arr2d):
                        arr2d[i, j] = 0
                        arr2d[i, j-1] = 0
                        arr2d[i, j-2] = 0
                        arr2d[i-1, j] = 0
                        arr2d[i-1, j-1] = 0
                        arr2d[i-1, j-2] = 0

                # Verticales de 6
                    if arr2d[i, j] == 1 and arr2d[i-1, j] == 1 and arr2d[i-2, j] and arr2d[i-3, j] == 0 and \
                       arr2d[i, j-1] == 1 and arr2d[i-1, j-1] == 1 and arr2d[i-2, j-1] and arr2d[i-3, j-1] == 0 and \
                           grupo12h == False and grupo8h == False and grupo6h == False:
                        print("HELP 2")
                        if i == 0 and j == 0:
                            canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(0*hor+x1, y1+ver*2, 0*hor+x2, y2+ver*3, outline="green")
                            canvas.create_rectangle(3*hor+x1, y1+ver*2, 3*hor+x2, y2+ver*3, outline="green")
                        elif i == 1 and j == 0:
                            canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="red")
                            canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*1, outline="green")
                            canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*1, outline="green")
                        elif j == 0:
                            canvas.create_rectangle((0)*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="red")
                            canvas.create_rectangle((3)*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="red")
                        elif i == 0:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(2), j*hor+x2, y2+ver*3, outline=rancolor())
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(0), j*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(3), j*hor+x2, y2+ver*3, outline="red")
                        elif i == 1:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(0), j*hor+x2, y2+ver*1, outline=rancolor())
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(0), j*hor+x2, y2+ver*0, outline="red")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(3), j*hor+x2, y2+ver*3, outline="red")
                        else:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i-1), j*hor+x2, y2+ver*i, outline=rancolor())
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i-2), (j)*hor+x2, y2+ver*(i-1), outline=rancolor())

                    tmp_arr = np.zeros((4, 4), dtype=int)
                    tmp_arr[i, j] = 1
                    tmp_arr[i, j-1] = 1
                    tmp_arr[i, j-2] = 1
                    tmp_arr[i-1, j] = 1
                    tmp_arr[i-1, j-1] = 1
                    tmp_arr[i-1, j-2] = 1
                    if np.array_equal(tmp_arr, arr2d):
                        arr2d[i, j] = 0
                        arr2d[i, j-1] = 0
                        arr2d[i, j-2] = 0
                        arr2d[i-1, j] = 0
                        arr2d[i-1, j-1] = 0
                        arr2d[i-1, j-2] = 0
                        


            # Grupos de 3
#                # Horizontales de 3
#                if arr2d[i,j]==1 and arr2d[i-1,j]==1 and arr2d[i-2,j]==1 \
#                    and arr2d[i,j-3]==0 and arr2d[i,j-1]==0\
#                    and arr2d[i-1,j-3]==0 and arr2d[i-1,j-1]==0\
#                    and arr2d[i-2,j-3]==0 and arr2d[i-2,j-3]==0\
#                    and arr2d[i-3,j]==0:
#                    if i == 0:
#                        canvas.create_rectangle(x1+hor*j, y1+ver*(0), x2+hor*j, y2+ver*(0),outline='red')
#                        canvas.create_rectangle(x1+hor*j, y1+ver*(3), x2+hor*j, y2+ver*(3),outline='red')
#                        canvas.create_rectangle(x1+hor*j, y1+ver*(2), x2+hor*j, y2+ver*(3),outline='green')
#                    elif i == 1:
#                        canvas.create_rectangle(x1+hor*j, y1+ver*(0), x2+hor*j, y2+ver*(1),outline='orange')
#                        canvas.create_rectangle(x1+hor*j, y1+ver*(3), x2+hor*j, y2+ver*(3),outline='blue')
#                        canvas.create_rectangle(x1+hor*j, y1+ver*(0), x2+hor*j, y2+ver*(0),outline='blue')
#                    else:
#                        canvas.create_rectangle(j*hor+x1, y1+ver*(i-1), j*hor+x2, y2+ver*i,outline=rancolor())
#                        canvas.create_rectangle(j*hor+x1, y1+ver*(i-2), j*hor+x2, y2+ver*(i-1),outline=rancolor())
#                    grupo3h = True
#                    arr2d[i, j] = 0
#                    arr2d[i-1, j] = 0
#                    arr2d[i-2, j] = 0
#
#                # Verticales de 3
#                if arr2d[i,j]==1 and arr2d[i,j-1]==1 and arr2d[i,j-2]==1\
#                    and arr2d[i-3,j]==0 and arr2d[i-1,j]==0\
#                    and arr2d[i-3,j-1]==0 and arr2d[i-1,j-1]==0\
#                    and arr2d[i-3,j-2]==0 and arr2d[i-1,j-2]==0\
#                    and arr2d[i,j-3]==0:
#                    if j == 1:
#                        canvas.create_rectangle(x1+hor*0, y1+ver*i, x2+hor*0, y2+ver*i,outline='red')
#                        canvas.create_rectangle(x1+hor*3, y1+ver*i, x2+hor*3, y2+ver*i,outline='red')
#                        canvas.create_rectangle(x1+hor*0, y1+ver*i, x2+hor*1, y2+ver*i,outline='green')
#                    elif j == 0:
#                        canvas.create_rectangle(x1+hor*2, y1+ver*i, x2+hor*3, y2+ver*i,outline='orange')
#                        canvas.create_rectangle(x1+hor*0, y1+ver*i, x2+hor*0, y2+ver*i,outline='blue')
#                        canvas.create_rectangle(x1+hor*3, y1+ver*i, x2+hor*3, y2+ver*i,outline='blue')
#                    else :
#                        canvas.create_rectangle((j-1)*hor+x1, y1+ver*i, j*hor+x2, y2+ver*i,outline=rancolor())
#                        canvas.create_rectangle((j-2)*hor+x1, y1+ver*i, (j-1)*hor+x2, y2+ver*i,outline=rancolor())
#                    grupo3v = True
#                    arr2d[i, j] = 0
#                    arr2d[i, j-1] = 0
#                    arr2d[i, j-2] = 0

        # Multicombo
        counterM = 0
        contadorM8 = 0
        for j in range(0, 4):
            for i in range(0, 4):
                if counter >= 12:
                # Horizontales de 8
                    tmp = np.ones((4), dtype=int)
                    if np.array_equal(tmp, arr2d[i][:]) and \
                        np.array_equal(tmp, arr2d[i-1][:]):
                        if i == 0:
                            canvas.create_rectangle(x1+hor*0, y1+ver*(0), x2+hor*3, y2+ver*(0), outline='red')
                            canvas.create_rectangle(x1+hor*0, y1+ver*(3), x2+hor*3, y2+ver*(3), outline='red')
                            label+= gp.agrupador(8, [0,1,2,3,12,13,14,15])
                        else:
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i - 1), 3*hor+x2, y2+ver*i, outline=rancolor())
                        grupo8h = True
                        contadorM8 += 1
                        label+=gp.agrupador(8,[(0+4*(i-1)) , (1+4*(i-1)) ,(2+4*(i-1)) , (3+4*(i-1)) , (4+4*(i-1)) , (5+4*(i-1)) , (6+4*(i-1)) , (7+4*(i-1))])
                        print([(0+4*(i-1)) , (1+4*(i-1)) ,(2+4*(i-1)) , (3+4*(i-1)) , (4+4*(i-1)) , (5+4*(i-1)) , (6+4*(i-1)) , (7+4*(i-1))])
                        print("multicombos")
                        #label += gp.agrupador(4, [])
                        if counter == 14:
                            print("EVALUA 13 HOR")
                            if (col1 + col3 == 8 and col2 + col4 == 6):
                                canvas.create_rectangle((0)*hor+x1, y1+ver*(0), 0*hor+x2, y2+ver*3, outline=rancolor())
                                canvas.create_rectangle((2)*hor+x1, y1+ver*(0), 2*hor+x2, y2+ver*3, outline=rancolor())

                            elif (col2 + col4 == 8 and col1 + col3 == 6):
                                canvas.create_rectangle((1)*hor+x1, y1+ver*(0), 1*hor+x2, y2+ver*3, outline=rancolor())
                                canvas.create_rectangle((3)*hor+x1, y1+ver*(0), 3*hor+x2, y2+ver*3, outline=rancolor())
                    
               # Verticales de 8
                    if np.array_equal(tmp, arr2d[:, i]) and \
                        np.array_equal(tmp, arr2d[:, i-1]):
                        if i == 0:
                            canvas.create_rectangle(x1+hor*0, y1+ver*(0), x2+hor*0, y2+ver*(3), outline='#93ac53')
                            canvas.create_rectangle(x1+hor*3, y1+ver*(0), x2+hor*3, y2+ver*(3), outline='#93ac53')
                            label+= gp.agrupador(8, [0,3,4,7,8,11,12,15])
                        else:
                            canvas.create_rectangle((i-1)*hor+x1, y1+ver*(0), i*hor+x2, y2+ver*3, outline=rancolor())
                        contadorM8 += 1
                        grupo8v = True
                        label += gp.agrupador(8, [0+1*(i-1),1+1*(i-1),4+1*(i-1),5+1*(i-1),8+1*(i-1),9+1*(i-1),12+1*(i-1),13+1*(i-1)])
                        print([0+1*(i-1),1+1*(i-1),4+1*(i-1),5+1*(i-1),8+1*(i-1),9+1*(i-1),12+1*(i-1),13+1*(i-1)])
                        print("multicombos")
                        #label += gp.agrupador(4, [[i, j], [i-1, j-1]])

                        if counter == 14:
                            print("EVALUA 13 VER")
                            if (fila1 + fila3 == 8 and fila2 + fila4 == 6):
                                canvas.create_rectangle((0)*hor+x1, y1+ver*(0), 3*hor+x2, y2+ver*0, outline=rancolor())
                                canvas.create_rectangle((0)*hor+x1, y1+ver*(2), 3*hor+x2, y2+ver*2, outline=rancolor())

                            elif (fila2 + fila4 == 8 and fila1 + fila3 == 6):
                                canvas.create_rectangle((0)*hor+x1, y1+ver*(1), 3*hor+x2, y2+ver*1, outline=rancolor())
                                canvas.create_rectangle((0)*hor+x1, y1+ver*(3), 3*hor+x2, y2+ver*3, outline=rancolor())
                if counter < 14:     
                    tmp2 = np.zeros((4), dtype=int)
               # Horizontales de 4
                    if np.array_equal(tmp, arr2d[i][:]) \
                        and grupo12h == False and grupo8h == False and grupo4h == False and grupo6h == False and grupo6v == False:
                        canvas.create_rectangle(0*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i), outline=rancolor())
                        label += gp.agrupador(4, [0,1,2,3])
                        print([0,1,2,3])
                        print("EVALUA")
                    
                        if np.array_equal(tmp2, arr2d[i-1][:]) and \
                            np.array_equal(tmp2, arr2d[i-3][:]):
                                arr2d[i][:] = np.zeros((4), dtype=int)
                                label += gp.agrupador(4, [0+4*(i-1),1+4*(i-1),2+4*(i-1),3+4*(i-1)])
                                print([0+4*(i),1+4*(i),2+4*(i),3+4*(i)])

               # Verticales de 4
                    if np.array_equal(tmp, arr2d[:, i]) \
                        and grupo12v == False and grupo8v == False and grupo6h == False and grupo6v == False:
                        canvas.create_rectangle(i*hor+x1, y1+ver*(0), i*hor+x2, y2+ver*(3), outline=rancolor())
                        label += gp.agrupador(4, [0+1*i,4+1*i,8+1*i,12+1*i])
                        print([0+1*i,4+1*i,8+1*i,12+1*i])
                        #label += gp.agrupador(4, [[i, j], [i-1, j-1]])
                        print("EVALUA VERTICAL")

                        if np.array_equal(tmp2, arr2d[:, i-1]) and \
                            np.array_equal(tmp2, arr2d[:, i-3]):
                                arr2d[:][i] = np.zeros((4), dtype=int)

                # Cuadrados de 4
                if arr2d[i, j] == 1 and arr2d[i-1, j] == 1 and arr2d[i, j-1] == 1 and arr2d[i-1, j-1] == 1 \
                    and grupo12h == False and grupo12v == False and grupo8h == False and grupo8v == False \
                    and grupo6h == False and grupo6v == False and grupo4c == False:
                    if counter < 12: 
                        if i == 0 and j == 0:
                            canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="#F83838")
                            canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="#F83838")
                            canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="#F83838")
                            canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="#F83838")
                        elif i == 0:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="orange")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="orange")
                        elif j == 0:
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="orange")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="orange")
                        else:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i-1), j*hor+x2, y2+ver*i, outline=rancolor())

                        grupo4c = True

                        if count == 10:
                            grupo4c == False

                    tmp_arr = np.zeros((4, 4), dtype=int)
                    tmp_arr[i, j] = 1
                    tmp_arr[i, j-1] = 1
                    tmp_arr[i-1, j] = 1
                    tmp_arr[i-1, j-1] = 1
                    
                    if np.array_equal(tmp_arr, arr2d):
                        arr2d = tmp_arr

                flagH2 = False
                flagV2 = False 
                flagMV2 = False
                flagMH2 = False

                # Cachitos de 2
                # Verticales de 4 abajo
                if arr2d[i, j] == 1 and arr2d[i-1, j-1] == 1 and arr2d[i-1, j] == 1 and arr2d[i, j-1] == 1  \
                and ((arr2d[i-2, j] == 0 and arr2d[i-2, j-1] == 0) or (arr2d[i-3, j] == 0 or arr2d[i-3, j-1] == 0)) \
                and (arr2d[i-1, j-2] == 0 or arr2d[i-1, j-3] == 0) \
                and flagV2 == False and flagMV2 == False and counterM <= 2 and contadorM8 == 0:
                    if i == 0 and j == 0:
                        canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="#F83838")
                        canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="#F83838")
                        canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="#F83838")
                        canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="#F83838")
                    elif i == 0:
                        if j == 1 or j == 3: 
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="orange")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="orange")
                        else:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="#FFAEBC")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="#FFAEBC")
                    elif j == 0:
                        if i == 1 or i == 3: 
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="orange")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="orange")
                        else:
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="#FFAEBC")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="#FFAEBC")
                    else:
                        canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i-1), j*hor+x2, y2+ver*i, outline=rancolor())
                    flagMV2 == True
                    counter += 1
                    if grupo4h == True or grupo4v == True:
                        counter += 2

                # Verticales de 4 arriba
                if arr2d[i, j] == 1 and arr2d[i-3, j-1] == 1 and arr2d[i-3, j] == 1 and arr2d[i, j-1] == 1  \
                and ((arr2d[i-2, j] == 0 and arr2d[i-2, j-1] == 0) or (arr2d[i-1, j] == 0 or arr2d[i-1, j-1] == 0)) \
                and (arr2d[i-3, j-2] == 0 or arr2d[i-3, j-3] == 0) \
                and flagV2 == False and flagMV2 == False and counterM <= 2 and contadorM8 == 0:
                    if i == 3 and j == 0:
                        canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="#F83838")
                        canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="#F83838")
                        canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="#F83838")
                        canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="#F83838")
                    elif i == 3:
                        if j == 1 or j == 3: 
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="#85D2D0")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="#85D2D0")
                        else:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="#887BB0")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="#887BB0")
                    elif j == 0:
                        if i == 3 or i == 3: 
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i+1), outline="orange")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i+1), outline="orange")
                        else:
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i+1), outline="#FFAEBC")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i+1), outline="#FFAEBC")
                    else:
                        canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i), j*hor+x2, y2+ver*(i+1), outline=rancolor())
                    flagMV2 == True
                    counterM += 1
                    if grupo4h == True or grupo4v == True:
                        counterM += 2
                    if counter >= 12:
                        coutnerM = 3

                # Horizontales de 4 derecha (Evalua todos los horizontales? :o)
                if arr2d[i, j] == 1 and arr2d[i-1, j-1] == 1 and arr2d[i, j-1] == 1 and arr2d[i-1, j] == 1  \
                and ((arr2d[i, j-2] == 0 and arr2d[i-1, j-2] == 0) or (arr2d[i, j-3] == 0 or arr2d[i-1, j-3] == 0)) \
                and (arr2d[i-2, j-1] == 0 or arr2d[i-3, j-1] == 0) \
                and flagV2 == False and flagMV2 == False and counterM <= 2:
                    print("EVALUA")
                    if i == 0 and j == 0:
                        print("PRIMERA")
                        canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="#F83838")
                        canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="#F83838")
                        canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="#F83838")
                        canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="#F83838")
                    elif i == 0:
                        print("SEGUNDA")
                        if i == 1 or i == 3: 
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="#85D2D0")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="#85D2D0")
                        else:
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="#FFAEBC")
                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="#FFAEBC")
                    elif j == 0:
                        print("TERCERA")
                        if j == 1 or j == 3: 
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="orange")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="orange")
                        else:
                            canvas.create_rectangle(0*hor+x1, y1+ver*(i-1), 0*hor+x2, y2+ver*i, outline="#887BB0")
                            canvas.create_rectangle(3*hor+x1, y1+ver*(i-1), 3*hor+x2, y2+ver*i, outline="#887BB0")
                    else:
                        print("CUARTA")
                        canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i-1), j*hor+x2, y2+ver*i, outline=rancolor())
                    flagMV2 == True
                    counterM += 1
                    if grupo4h == True or grupo4v == True:
                        counterM += 2
                    if counter >= 12:
                        coutnerM = 3

#                # Horizontales de 4 izquierda
#                if arr2d[i, j] == 1 and arr2d[i-3, j-1] == 1 and arr2d[i-3, j] == 1 and arr2d[i, j-1] == 1  \
#                and ((arr2d[i-2, j] == 0 and arr2d[i-2, j-1] == 0) or (arr2d[i-1, j] == 0 or arr2d[i-1, j-1] == 0)) \
#                and (arr2d[i-3, j-2] == 0 or arr2d[i-3, j-3] == 0) \
#                and flagV2 == False and flagMV2 == False:
#                    if i == 3 and j == 0:
#                        canvas.create_rectangle(0*hor+x1, y1+ver*0, 0*hor+x2, y2+ver*0, outline="#F83838")
#                        canvas.create_rectangle(3*hor+x1, y1+ver*0, 3*hor+x2, y2+ver*0, outline="#F83838")
#                        canvas.create_rectangle(0*hor+x1, y1+ver*3, 0*hor+x2, y2+ver*3, outline="#F83838")
#                        canvas.create_rectangle(3*hor+x1, y1+ver*3, 3*hor+x2, y2+ver*3, outline="#F83838")
#                    elif i == 3:
#                        if j == 1 or j == 3: 
#                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="orange")
#                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="orange")
#                        else:
#                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*0, j*hor+x2, y2+ver*0, outline="#FFAEBC")
#                            canvas.create_rectangle((j-1)*hor+x1, y1+ver*3, j*hor+x2, y2+ver*3, outline="#FFAEBC")
#                    elif j == 0:
#                        if i == 3 or i == 3: 
#                            canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i+1), outline="orange")
#                            canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i+1), outline="orange")
#                        else:
#                            canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i+1), outline="#FFAEBC")
#                            canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i+1), outline="#FFAEBC")
#                    else:
#                        canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i), j*hor+x2, y2+ver*(i+1), outline=rancolor())
#                    flagMV2 == True
#                if arr2d[i, j] == 1 and arr2d[i-3, j] == 1 and (arr2d[i-1, j] == 0 or arr2d[i-2, j] == 0) \
#                    and arr2d[i-3, j-1] == 0 and arr2d[i-3, j-3] == 0 and flagV2 == False:
#                    if i == 3:
#                        canvas.create_rectangle(j*hor+x1, y1+ver*(0), j*hor+x2, y2+ver*(0), outline="blue")
#                        canvas.create_rectangle(j*hor+x1, y1+ver*(3), j*hor+x2, y2+ver*(3), outline="blue")
#                    else:
#                        canvas.create_rectangle(j*hor+x1, y1+ver*(i), j*hor+x2, y2+ver*(i+1), outline=rancolor())
#                    flagMV2 == True
#                # Horizontales de 4
#                if arr2d[i, j] == 1 and arr2d[i, j-1] == 1 and (arr2d[i, j-2] == 0 or arr2d[i, j-3] == 0) \
#                    and arr2d[i-1, j-1] == 0 and arr2d[i-3, j-1] == 0 and flagH2 == False:
#                    if j == 0:
#                        canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i), outline="blue")
#                        canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i), outline="blue")
#                    else:
#                        canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i), j*hor+x2, y2+ver*(i), outline=rancolor())
#                    flagMH2 == True
#                if arr2d[i, j] == 1 and arr2d[i, j-3] == 1 and (arr2d[i, j-1] == 0 or arr2d[i, j-2] == 0) \
#                    and arr2d[i-1, j-3] == 0 and arr2d[i-3, j-3] == 0 and flagH2 == False:
#                    if j == 3:
#                        canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i), outline="blue")
#                        canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i), outline="blue")
#                    else:
#                        canvas.create_rectangle(j*hor+x1, y1+ver*(i), (j+1)*hor+x2, y2+ver*(i), outline=rancolor())
#                    flagMH2 == True

                # Cachitos de 1
                # Verticales de 2
                if arr2d[i, j] == 1 and arr2d[i-1, j] == 1 and (arr2d[i-2, j] == 0 or arr2d[i-3, j] == 0) \
                    and arr2d[i-1, j-1] == 0 and arr2d[i-1, j-3] == 0 and flagV2 == False and flagMV2 == False:
                    if i == 0:
                        canvas.create_rectangle(j*hor+x1, y1+ver*(0), j*hor+x2, y2+ver*(0), outline="blue")
                        canvas.create_rectangle(j*hor+x1, y1+ver*(3), j*hor+x2, y2+ver*(3), outline="blue")
                    else:
                        canvas.create_rectangle(j*hor+x1, y1+ver*(i-1), j*hor+x2, y2+ver*(i), outline=rancolor())
                    flagV2 == True
                if arr2d[i, j] == 1 and arr2d[i-3, j] == 1 and (arr2d[i-1, j] == 0 or arr2d[i-2, j] == 0) \
                    and arr2d[i-3, j-1] == 0 and arr2d[i-3, j-3] == 0 and flagV2 == False and flagMV2 == False:
                    if i == 3:
                        canvas.create_rectangle(j*hor+x1, y1+ver*(0), j*hor+x2, y2+ver*(0), outline="blue")
                        canvas.create_rectangle(j*hor+x1, y1+ver*(3), j*hor+x2, y2+ver*(3), outline="blue")
                    else:
                        canvas.create_rectangle(j*hor+x1, y1+ver*(i), j*hor+x2, y2+ver*(i+1), outline=rancolor())
                    flagV2 == True
                # Horizontales de 2
                if arr2d[i, j] == 1 and arr2d[i, j-1] == 1 and (arr2d[i, j-2] == 0 or arr2d[i, j-3] == 0) \
                    and arr2d[i-1, j-1] == 0 and arr2d[i-3, j-1] == 0 and flagH2 == False and flagMH2 == False:
                    if j == 0:
                        canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i), outline="blue")
                        canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i), outline="blue")
                    else:
                        canvas.create_rectangle((j-1)*hor+x1, y1+ver*(i), j*hor+x2, y2+ver*(i), outline=rancolor())
                    flagH2 == True
                if arr2d[i, j] == 1 and arr2d[i, j-3] == 1 and (arr2d[i, j-1] == 0 or arr2d[i, j-2] == 0) \
                    and arr2d[i-1, j-3] == 0 and arr2d[i-3, j-3] == 0 and flagH2 == False and flagMH2 == False:
                    if j == 3:
                        canvas.create_rectangle(0*hor+x1, y1+ver*(i), 0*hor+x2, y2+ver*(i), outline="blue")
                        canvas.create_rectangle(3*hor+x1, y1+ver*(i), 3*hor+x2, y2+ver*(i), outline="blue")
                    else:
                        canvas.create_rectangle(j*hor+x1, y1+ver*(i), (j+1)*hor+x2, y2+ver*(i), outline=rancolor())
                    flagH2 == True

#                        if grupo3h:
#                            if arr_tmp[i, j] != arr2d[i, j] and arr_tmp[i-1, j] != arr2d[i-1, j] and \
#                            arr2d[i, j+2] == 0 and arr2d[i, j+3] == 0:
#                                if grupo3h:
#                                    
#                                print(0)


        # Poner la funcion simplificada 
        largo = len(label)
        label_2 = label[:largo -3]
        label_fun = canvas_label.create_text((200, 50), text=label_2)


        print(label)



#------------Funcion que abre una nueva ventana -------------

def openK3Window():
    K3Window = Toplevel(interface) 

    Hventana = 380
    K3Window.geometry("670x380")
    K3Window.resizable(0, 0)
    K3Window.title("Mapas de Karnaugh con 3 Variables")
    K3Window.iconbitmap("interface/map.ico")

    LabelInstruc = Label(K3Window, text="Marque en los checkbox de la tabla de verdad las variables que sean unos. " + \
                                        "Deje en blanco las variables que sean cero. " + \
                                        "Después, presione calcular y revise la consola."\
                        , wraplength=620, anchor = "w").place(x=20, y=20)
    
    # Poner imagen
    table_image = Label(K3Window, image=PicTable3).place(x=30, y=90)

    #---------------- Boton Checkbox ----------------------

    arr = []
    for i in range(8):
        option = IntVar()
        arr.append(option)

    # Spacing vertical de 27
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[0], onvalue=1, offvalue=0).place(x=175, y=122)
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[1], onvalue=1, offvalue=0).place(x=175, y=122+27*1)
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[2], onvalue=1, offvalue=0).place(x=175, y=122+27*2)
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[3], onvalue=1, offvalue=0).place(x=175, y=122+27*3)
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[4], onvalue=1, offvalue=0).place(x=175, y=122+27*4)
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[5], onvalue=1, offvalue=0).place(x=175, y=122+27*5)
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[6], onvalue=1, offvalue=0).place(x=175, y=122+27*6)
    Checkbutton(K3Window, text="¿Es 1?", variable=arr[7], onvalue=1, offvalue=0).place(x=175, y=122+27*7)


    #---------------- Boton Calcular ----------------------

    buttonCalc = Button(K3Window,text="Calcular", command=lambda: calcular(arr, K3Window, Hventana, 3)).place(x=75, y=60)


def openK2Window():
    K2Window = Toplevel(interface) 

    Hventana = 380
    K2Window.geometry("500x350")
    K2Window.resizable(0, 0)
    K2Window.title("Mapas de Karnaugh con 2 Variables")
    K2Window.iconbitmap("interface/map.ico")

    LabelInstruc = Label(K2Window, text="Marque en los checkbox de la tabla de verdad las variables que sean unos. " + \
                                        "Deje en blanco las variables que sean cero. " + \
                                        "Después, presione calcular y revise la consola."\
                        , wraplength=450, anchor = "w").place(x=20, y=20)
    
    # Poner imagen
    table_image = Label(K2Window, image=PicTable2).place(x=30, y=90)

    #---------------- Boton Checkbox ----------------------

    arr = []
    for i in range(4):
        option = IntVar()
        arr.append(option)

    # Spacing vertical de 27
    Checkbutton(K2Window, text="¿Es 1?", variable=arr[0], onvalue=1, offvalue=0).place(x=145, y=135)
    Checkbutton(K2Window, text="¿Es 1?", variable=arr[1], onvalue=1, offvalue=0).place(x=145, y=135+35*1)
    Checkbutton(K2Window, text="¿Es 1?", variable=arr[2], onvalue=1, offvalue=0).place(x=145, y=135+35*2)
    Checkbutton(K2Window, text="¿Es 1?", variable=arr[3], onvalue=1, offvalue=0).place(x=145, y=135+35*3)

    #---------------- Boton Calcular ----------------------

    buttonCalc = Button(K2Window,text="Calcular", command=lambda: calcular(arr, K2Window, Hventana, 2)).place(x=150, y=100)


def openK4Window():
    K4Window = Toplevel(interface)

    Hventana = 620 
    K4Window.geometry("740x620")
    K4Window.resizable(0, 0)
    K4Window.title("Mapas de Karnaugh con 4 Variables")
    K4Window.iconbitmap("interface/map.ico")

    LabelInstruc = Label(K4Window, text="Marque en los checkbox de la tabla de verdad las variables que sean unos. " + \
                                        "Deje en blanco las variables que sean cero. " + \
                                        "Después, presione calcular y revise la consola."\
                        , wraplength=700, anchor = "w").place(x=20, y=20)
    
    # Poner imagen
    table_image = Label(K4Window, image=PicTable4).place(x=30, y=90)

    #---------------- Boton Checkbox ----------------------

    arr = []
    for i in range(16):
        option = IntVar()
        arr.append(option)

    sep = 29
    # Spacing vertical de 27
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[0], onvalue=1, offvalue=0).place(x=175, y=122)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[1], onvalue=1, offvalue=0).place(x=175, y=122+sep*1)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[2], onvalue=1, offvalue=0).place(x=175, y=122+sep*2)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[3], onvalue=1, offvalue=0).place(x=175, y=122+sep*3)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[4], onvalue=1, offvalue=0).place(x=175, y=122+sep*4)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[5], onvalue=1, offvalue=0).place(x=175, y=122+sep*5)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[6], onvalue=1, offvalue=0).place(x=175, y=122+sep*6)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[7], onvalue=1, offvalue=0).place(x=175, y=122+sep*7)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[8], onvalue=1, offvalue=0).place(x=175, y=122+sep*8)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[9], onvalue=1, offvalue=0).place(x=175, y=122+sep*9)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[10], onvalue=1, offvalue=0).place(x=175, y=122+sep*10)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[11], onvalue=1, offvalue=0).place(x=175, y=122+sep*11)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[12], onvalue=1, offvalue=0).place(x=175, y=122+sep*12)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[13], onvalue=1, offvalue=0).place(x=175, y=122+sep*13)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[14], onvalue=1, offvalue=0).place(x=175, y=122+sep*14)
    Checkbutton(K4Window, text="¿Es 1?", variable=arr[15], onvalue=1, offvalue=0).place(x=175, y=122+sep*15)


    #---------------- Boton Calcular ----------------------

    buttonCalc = Button(K4Window,text="Calcular", command=lambda: calcular(arr, K4Window, Hventana, 4)).place(x=80, y=62)




#-------------------Icons--------------------------------

imgBoton = PhotoImage(file="interface/map_icon.png")

#-------------Informacion de Interface-----------------

interface.resizable(0,0)
interface.title("Mapas de Karnaugh")
interface.iconbitmap("interface/map.ico")

miFrame=Frame(interface,width=400,height=200)
miFrame.pack()


#-------------Mensaje Bienvenida---------------------------------


LabelWelcome=Label(miFrame,text="¡Bienvenido al programa de simplificación de Mapas de Karnaugh!")
LabelWelcome.place(x=10,y=10)

LabelInfo=Label(miFrame,text="Este programa le permite simplificar funciones booleanas.")
LabelInfo.place(x=10,y=30)

LabelOption = Label (miFrame,text="Elija su número de variables: ")
LabelOption.place(x=10,y=60)


#---------------- Botones de seleccion de variables----------------------

button2var = Button(interface,text="2 Variables", command= openK2Window)
button2var.place(x=150,y=90)

button3var = Button(interface,text="3 Variables", command=openK3Window)
button3var.place(x=150,y=120)

button4var = Button(interface,text="4 Variables", command= openK4Window)
button4var.place(x=150,y=150)

interface.mainloop()