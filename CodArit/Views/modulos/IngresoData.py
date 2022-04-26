import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

class IngresoData:
    def __init__(self, frame, x, y, w):
        self.input = Text(frame)
        self.x = x
        self.y = y
        self.w = w

    def ingreso(self):
        self.input.config(font=('Calibri', 14, 'bold'), 
                            bg='#CEE8F2',
                            bd=0,
                            height=1,
                            padx=5,
                            pady=15
                            )
        self.input.place(relx=self.x, rely=self.y, relwidth=self.w)

    def getData(self):
        return self.input.get('1.0', 'end-1c')

    def Limpiar(self):
        self.input.delete(1.0 ,tk.END)