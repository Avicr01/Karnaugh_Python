from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("TEST")
root.geometry("500x500")

# las tablas no se ven tan bien

#my_table = ttk.Treeview(root)
#
#my_table['columns'] = ("0", "1")
#
#my_table.column("#0", width=120, minwidth=25)
#my_table.column("0", anchor=W, width=120)
#my_table.column("1", anchor=CENTER, width=80)
#
#my_table.heading("#0", text="P / Q", anchor=W)
#my_table.heading("0", text="0", anchor=W)
#my_table.heading("1", text="1", anchor=CENTER)
#
#my_table.insert(parent='', index='end', id=0, text="Parent")
#my_table.pack(pady=20)

arr = [1, 2, 3, 4]

canvas = tk.Canvas(root, height=360, width=400)
canvas.pack()

fila1 = "{}      {}".format(arr[1], arr[2])
fila2 = "{}      {}".format(arr[3], arr[0])

bg_img = tk.PhotoImage(file="interface/images/kar2.png")
bg_label = canvas.create_image((0,0), image=bg_img, anchor=tk.N + tk.W)
label_arr = canvas.create_text((200, 120), text=fila1+"\n"+fila2, font="Calibri 20 bold")

root.mainloop()

root.mainloop()