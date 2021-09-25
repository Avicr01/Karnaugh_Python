from tkinter import *
from tkinter import filedialog, messagebox
import tkinter
from PIL import ImageTk, Image
from src.k2v import kmaps2 
from src.k3v import kmaps3 
from src.k4v import kmaps4 
from src.k4v import kmaps4 

# Grupos importados para las 4 variables
import src.k4_groups.k4v_con15 as g15
import src.k4_groups.k4v_con14 as g14
import src.k4_groups.k4v_con13 as g13
import src.k4_groups.k4v_con12 as g12
### Las iteraciones son tan grandes que tenemos que separarlos en grupos
## Para 11
#import src.k4_groups.k4v_con11 as g11
## Para 10
#import src.k4_groups.k4v_con10 as g10
## Para 9
# import src.k4_groups.k4v_con9 as g9
## Para 8
#import src.k4_groups.k4v_con8 as g8
## Para 7
# Lo completado hasta ahora
import src.k4_groups.k4v_con7 as g7
## Para 6
#import src.k4_groups.k4v_con6 as g6
## Para 5
#import src.k4_groups.k4v_con5 as g5
import src.k4_groups.k4v_con4 as g4
import src.k4_groups.k4v_con3 as g3
import src.k4_groups.k4v_con2 as g2
import src.k4_groups.k4v_con1 as g1

import os
import json

interface = Tk()

#----Instancias de imagenes ---------------

PicTable2 = ImageTk.PhotoImage(file="interface/images/2v.png")
PicTable3 = ImageTk.PhotoImage(file="interface/images/3v.png")
PicTable4 = ImageTk.PhotoImage(file="interface/images/4v.png")
PicK2 = ImageTk.PhotoImage(file="interface/images/kar2.png")
PicK3 = ImageTk.PhotoImage(file="interface/images/kar3.png")
PicK4 = ImageTk.PhotoImage(file="interface/images/kar4.png")

#------------Funcion evaluar mapas de Karnaugh-------------

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

        # Dibujar el mapa
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
                        canvas.create_rectangle(70, 60, 110, 100, outline='red')
                    elif x == 1:
                        canvas.create_rectangle(70+60, 60, 110+60, 100, outline='red')
                    elif x == 2:
                        canvas.create_rectangle(70, 60+60, 110, 100+60, outline='red')
                    elif x == 3:
                        canvas.create_rectangle(70+60, 60+60, 110+60, 100+60, outline='red')
        elif count == 4: 
            canvas.create_rectangle(70, 60, 110+60, 100+60, outline='red')
        elif count == 2: 
            # Horizontal 
            if listing[0] + listing[1] == 2:
                canvas.create_rectangle(70, 60, 110+60, 100, outline='red')
            elif listing[2] + listing[3] == 2:
                canvas.create_rectangle(70, 60+60, 110+60, 100+60, outline='red')
            # Vertical
            elif listing[0] + listing[2] == 2:
                canvas.create_rectangle(70, 60, 110, 100+60, outline='red')
            elif listing[1] + listing[3] == 2:
                canvas.create_rectangle(70+60, 60, 110+60, 100+60, outline='red')
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
        
        line1 = listing[0] + listing[1] + listing[3] + listing[2]
        line2 = listing[4] + listing[5] + listing[7] + listing[6]

        arr1 = (listing[0] , listing[1] , listing[3] , listing[2])
        arr2 = (listing[4] , listing[5] , listing[7] , listing[6])

        label_arr = canvas.create_text((205, 110), text=fila1+fila2, font="Calibri 18 bold")
        
        # Poner la funcion simplificada 
        canvas_label.place(x = 270, y = 280)
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
            for x in range(0, len(listing)):
                if listing[x] == 1:
                    if x == 0:
                        canvas.create_rectangle(x1, y1, x2, y2, outline='red')
                    elif x == 1:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
                    elif x == 2:
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                    elif x == 3:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='red')
                    elif x == 4:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
                    elif x == 5:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
                    elif x == 6:
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                    elif x == 7:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='red')
        elif count == 2: 
            if line1 == 2:
                # Horizontal 
                if listing[0] + listing[1] == 2:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
                elif listing[1] + listing[3] == 2:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='red')
                elif listing[3] + listing[2] == 2:
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                elif listing[0] + listing[2] == 2:
                    canvas.create_rectangle(x1, y1, x2, y2, outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')

                # Separacion
                elif listing[0] + listing[3] == 2:
                    canvas.create_rectangle(x1, y1, x2, y2, outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='blue')
                elif listing[1] + listing[2] == 2:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='blue')

            elif line2 == 2:
                if listing[4] + listing[5] == 2:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
                elif listing[5] + listing[7] == 2:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='red')
                elif listing[7] + listing[6] == 2:
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                elif listing[4] + listing[6] == 2:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')

                # Separacion
                elif listing[4] + listing[7] == 2:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='blue')
                elif listing[5] + listing[6] == 2:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='blue')
            elif line1 == 1 or line2 == 1:
                # Vertical
                if listing[0] + listing[4] == 2:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                elif listing[1] + listing[5] == 2:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='red')
                elif listing[3] + listing[7] == 2:
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='red')
                elif listing[2] + listing[6] == 2:
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                else:
                    for x in range(0, len(listing)):
                        if listing[x] == 1:
                            if x == 0:
                                canvas.create_rectangle(x1, y1, x2, y2, outline='red')
                            if x == 1:
                                canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
                            if x == 2:
                                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                            if x == 3:
                                canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='red')
                            if x == 4:
                                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
                            if x == 5:
                                canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
                            if x == 6:
                                canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                            if x == 7:
                                canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='red')

        elif count == 3:

            if line1 == 3 or line2 == 3:
                if listing[0] == 1:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='blue')
                elif listing[3] == 1:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='blue')
                elif listing[4] == 1:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='blue')
                else:
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='blue')

            else:
                for i in range (0,3):
                    if arr1[i] == 1 and arr1[i+1] == 1 and arr2[i] == 1:
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(1), y2+ver*(0), outline='red')
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(0), y2+ver*(1), outline='blue')
                    if arr1[i] == 1 and arr1[i+1] == 1 and arr2[i+1] == 1:
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(1), y2+ver*(0), outline='red')
                        canvas.create_rectangle((i*hor)+x1+hor*(1), y1+ver*(0), (i*hor)+x2+hor*(1), y2+ver*(1), outline='blue')
                    if arr1[i] == 1 and arr2[i] == 1 and arr2[i+1] == 1:
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(1), (i*hor)+x2+hor*(1), y2+ver*(1), outline='blue')
                    if arr1[i+1] == 1 and arr2[i] == 1 and arr2[i+1] == 1:
                        canvas.create_rectangle((i*hor)+x1+hor*(1), y1+ver*(0), (i*hor)+x2+hor*(1), y2+ver*(1), outline='red')
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(1), (i*hor)+x2+hor*(1), y2+ver*(1), outline='blue')
                
                if arr1[3] == 1 and arr1[0] == 1 and arr2[3] == 1:
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3),y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0),y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3),y2+ver*(0), outline='red')
                if arr1[0] == 1 and arr1[3] == 1 and arr2[0] == 1:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0),y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0),y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3),y2+ver*(0), outline='red')
                if arr1[3] == 1 and arr2[3] == 1 and arr2[0] == 1:
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3),y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0),y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3),y2+ver*(1), outline='red')
                if arr1[0] == 1 and arr2[3] == 1 and arr2[0] == 1:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0),y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0),y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3),y2+ver*(1), outline='red')

        elif count == 4:
            for i in range (0,3):
                    if arr1[i] == 1 and arr1[i+1] == 1 and arr2[i] == 1 and arr2[i+1] == 1:
                        canvas.create_rectangle((i*hor)+x1+hor*(0), y1+ver*(0), (i*hor)+x2+hor*(1), y2+ver*(1), outline='red')
            if arr1[3] == 1 and arr1[0] == 1 and arr2[3] == 1 and arr2[0] == 1:
                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')

#            else:
#                # Rangos de 0 a 3
#                for i in range(0, 3):
#                    if arr1[i] + arr1[i+1] == 1:
#                        if listing[0] + listing[1] == 2:
#                            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
#                        elif listing[1] + listing[3] == 2:
#                            canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='red')
#                        elif listing[3] + listing[2] == 2:
#                            canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
#                    if arr2[i] + arr2[i+1] == 1:
#                        if listing[4] + listing[5] == 2:
#                            canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
#                        elif listing[5] + listing[7] == 2:
#                            canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='red')
#                        elif listing[7] + listing[6] == 2:
#                            canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
#
#                    for j in range(0, 4):
#
#                            if arr1[i] + arr2[i] == 1:
#                        
#
#                    if arr1[x] + arr1[x+1] == 1:
#                        if line1 == 2:
#                            # Horizontal
#                            if listing[0] + listing[1] == 2:
#                                canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
#                            elif listing[1] + listing[3] == 2:
#                                canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='red')
#                            elif listing[3] + listing[2] == 2:
#                                canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
#                                
#                                
#                            elif listing[0] + listing[2] == 2:
#                                canvas.create_rectangle(x1, y1, x2, y2, outline='red')
#                                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
#                            # Separacion
#                            elif listing[0] + listing[3] == 2:
#                                canvas.create_rectangle(x1, y1, x2, y2, outline='red')
#                                canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(0), outline='blue')
#                            elif listing[1] + listing[2] == 2:
#                                canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(0), outline='red')
#                                canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='blue')
#
#                            if arr1[x] == arr2[x]:
#                                # Vertical
#                                if listing[0] + listing[4] == 2:
#                                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
#                                elif listing[1] + listing[5] == 2:
#                                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='red')
#                                elif listing[3] + listing[7] == 2:
#                                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='red')
#                                elif listing[2] + listing[6] == 2:
#                                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
#                            else:
#                                if x == 4:
#                                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
#                                if x == 5:
#                                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
#                                if x == 6:
#                                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
#                                if x == 7:
#                                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='red')
#
#                        elif line2 == 2:
#                            # Horizontal 
#                            if listing[4] + listing[5] == 2:
#                                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
#                            elif listing[5] + listing[7] == 2:
#                                canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='red')
#                            elif listing[7] + listing[6] == 2:
#                                canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
#                            elif listing[4] + listing[6] == 2:
#                                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
#                                canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
#                            # Separacion
#                            elif listing[4] + listing[7] == 2:
#                                canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
#                                canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='blue')
#                            elif listing[5] + listing[6] == 2:
#                                canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
#                                canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='blue')
#                        
#                            if arr1[x] == arr2[x]:
#                                # Vertical
#                                if listing[0] + listing[4] == 2:
#                                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
#                                elif listing[1] + listing[5] == 2:
#                                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='red')
#                                elif listing[3] + listing[7] == 2:
#                                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='red')
#                                elif listing[2] + listing[6] == 2:
#                                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
#                    
#                            else:
#                                if x == 4:
#                                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(0), y2+ver*(1), outline='red')
#                                if x == 5:
#                                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
#                                if x == 6:
#                                    canvas.create_rectangle(x1+hor*(3), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
#                                if x == 7:
#                                    canvas.create_rectangle(x1+hor*(2), y1+ver*(1), x2+hor*(2), y2+ver*(1), outline='red')
        elif count == 6:
            if line1 == 2:
                # Horizontal 
                if listing[0] + listing[1] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[1] + listing[3] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[3] + listing[2] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='blue')
                elif listing[0] + listing[2] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='green')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='blue')

                # Separacion
                elif listing[0] + listing[3] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='green')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[1] + listing[2] == 0:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(1), x2+hor*(1), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='blue')
                    
            elif line2 == 2:
                # Horizontal
                if listing[4] + listing[5] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[5] + listing[7] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='blue')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[7] + listing[6] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='blue')
                elif listing[4] + listing[6] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='blue')

                # Separacion
                elif listing[4] + listing[7] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='green')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[5] + listing[6] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='red')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='green')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='blue')

            elif line1 == 3 or line2 == 3:
                # Verticales en mismo lugar
                if listing[0] + listing[4] == 0:
                    canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[1] + listing[5] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                elif listing[3] + listing[7] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='blue')
                elif listing[2] + listing[6] == 0:
                    canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='red')
                    canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')

        elif count == 7:
            for x in range(0, len(listing)):
                if listing[x] == 0:
                    if x == 0:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='green')
                    elif x == 1:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='green')
                    elif x == 2:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='green')
                    elif x == 3:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(1), x2+hor*(3), y2+ver*(1), outline='green')
                    elif x == 4:
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='green')
                    elif x == 5:
                        canvas.create_rectangle(x1+hor*(2), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='green')
                    elif x == 6:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(1), y1+ver*(0), x2+hor*(2), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='green')
                    elif x == 7:
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(1), y2+ver*(1), outline='blue')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(0), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(3), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')
                        canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(0), outline='green')

        elif count == 8: 
            canvas.create_rectangle(x1+hor*(0), y1+ver*(0), x2+hor*(3), y2+ver*(1), outline='red')

    elif var == 4:
        count = sum(map(lambda x: x == 1, listing))

        #   Para todos ceros 
        if count == 0:
            label += "No hay grupos"
            label += "Funcion simplificada, f(P, Q, R, S) = 0"
        # Para todos unos
        elif count == 16:
            label += "Grupo de 16 = { [1], [2], [3], [4], [5], [6], [7], [8], " \
                    "\n[9], [10], [11], [12], [13], [14], [15], [16] }"
            label += "\nFuncion simplificada, f(P, Q, R, S) = 1"
        elif count == 15:
            label = g15.k4v15(listing, label)
        elif count == 14:
            label = g14.k4v14(listing, label)
        elif count == 13:
            label = g13.k4v13(listing, label)
        elif count == 12:
            label = g12.k4v12(listing, label)
        elif count == 11:
            #label = g11.k4v11(listing, label)
            label = " "
        elif count == 10:
            #label = g10.k4v10(listing, label)
            label = " "
        elif count == 9:
            #label = g9.k4v9(listing, label)
            label = " "
        elif count == 8:
            #label = g8.k4v8(listing, label)
            label = " "
        elif count == 7:
            label = g7.k4v7(listing, label)
        elif count == 6:
            #label = g6.k4v6(listing, label)
            label = " "
        elif count == 5:
            #label = g5.k4v5(listing, label)
            label = " "
        elif count == 4:
            label = g4.k4v4(listing, label)
        elif count == 3:
            label = g3.k4v3(listing, label)
        elif count == 2:
            label = g2.k4v2(listing, label)
        elif count == 1:
            label = g1.k4v1(listing, label)

        # Impresion en consola
        kmaps4(listing)
        print(label)


        canvas.place(x = 280, y = 92)

        canvas_label = tkinter.Canvas(ventana, height=300, width=400)
        canvas_label.place(x = 300, y = 500)

        # Dibujar el mapa
        karnaugh_img = canvas.create_image((0,0), image=PicK4, anchor=tkinter.N + tkinter.W)
        fila1 = "{}                {}                 {}              {}".format(listing[0], listing[1], listing[3], listing[2])
        fila2 = "\n\n{}                 {}                {}              {}".format(listing[4], listing[5], listing[7], listing[6])
        fila3 = "\n\n\n{}                 {}                {}              {}".format(listing[12], listing[13], listing[15], listing[14])
        fila4 = "\n\n{}                 {}                {}              {}".format(listing[8], listing[9], listing[11], listing[10])
        


        label_arr = canvas.create_text((250, 205), text=fila1+fila2+fila3+fila4, font="Calibri 18 bold")
        
        # Poner la funcion simplificada 
        label_fun = canvas_label.create_text((200, 50), text=label)
        
        
        # Crear grupos 
        x1 = 80
        x2 = 120 
        y1 = 60 
        y2 = 100
        hor = 72
        ver = 60



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
                        , wraplength=440, anchor = "w").place(x=20, y=20)
    
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