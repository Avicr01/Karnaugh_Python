from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from src.k2v import kmaps2 
from src.k3v import kmaps3 
from src.k4v import kmaps4 
import os
import json

interface = Tk()


def binary_string_to_bytearray(binary_string):
    """
    Transforms a binary string "01001100..." into a bytearray
    to be written into a binary file.
    """
    # Add 0 until the binary string has a length divisible by 8
    counter = 0
    while not len(binary_string) % 8 == 0:
        binary_string += "0"
        counter += 1

    # Divide the binary string into chunks of 8. For each chunk, cast it into
    # an integer and then convert the list of integers into a bytearray.
    return bytearray(int(binary_string[x:x+8], 2) for x in range(0, len(binary_string), 8))




#----Variables Strings Respectivos  ---------------



#----Variables Ints Respectivos  ---------------

#----Instancias de imagenes ---------------

PicTable3 = ImageTk.PhotoImage(file="interface/images/3v.png")

#------------Funcion que abre una nueva ventana -------------

def calcular(arr, ventana, Hventana, var):
    label = ""
    listing = []
    for i in range(len(arr)):
        listing.append(arr[i].get())
    print("\n")

    # Funcion de Mapas de Karnaugh
    if var == 2:
        label = kmaps2(listing, label)
    elif var == 3:
        label = kmaps3(listing, label)
    elif var == 4:
        label = kmaps4(listing, label)

    print(label)
    LabelSimple=Label(ventana,text=label)
    LabelSimple.place(x=10,y=Hventana-100)

def openK3Window():
    def show():
        label = ""
        listing = []
        for i in range(len(arr)):
            listing.append(arr[i].get())
        print("\n")

        # Funcion de Mapas de Karnaugh
        label = kmaps3(listing, label)
        print(label)
        LabelSimple=Label(K3Window,text=label)
        LabelSimple.place(x=10,y=370)


    K3Window = Toplevel(interface) 

    Hventana = 480
    K3Window.geometry("470x480")
    K3Window.resizable(0, 0)
    K3Window.title("Mapas de Karnaugh con 3 Variables")
    K3Window.iconbitmap("interface/map.ico")

    LabelInstruc = Label(K3Window, text="Marque en los checkbox de la tabla de verdad las variables que sean unos. " + \
                                        "Deje en blanco las variables que sean cero. " + \
                                        "Después, presione calcular y revise la consola."\
                        , wraplength=440, anchor = "w").place(x=20, y=20)
    
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

    buttonCalc = Button(K3Window,text="Calcular", command=lambda: calcular(arr, K3Window, Hventana, 3)).place(x=300, y=190)


def openK2Window():
    K3Window = Toplevel(interface)



def openK4Window():
    K3Window = Toplevel(interface)



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