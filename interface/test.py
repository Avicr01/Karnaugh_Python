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


import random 
import numpy as np

numero_colores = 10


def _paint():
    return "#" + ''.join([random.choice('0123456789AB') for j in range(6)])

 
# print(np.array_equal([1, 2], [1, 2]))


canvas = tk.Canvas(root, height=360, width=400)
canvas.pack()

canvas.create_rectangle(20, 40, 70, 90, outline=_paint())
canvas.create_rectangle(50, 20, 90, 30, outline=_paint())
canvas.create_rectangle(200, 140, 170, 190, outline=_paint())
canvas.create_rectangle(10, 10, 100, 120, outline=_paint())

tmp = np.ones((2, 1), dtype=np.int64)
arr = [[1], [1]]
print(arr)
print(tmp)
print("is equal ", np.array_equal(tmp, arr))

root.mainloop()