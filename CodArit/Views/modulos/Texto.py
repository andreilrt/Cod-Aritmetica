import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

class Texto:
    def __init__(self, frame, texto, colorFondo, pt):
        self.texto = Text(frame)
        self.text = texto
        self.fondo = colorFondo
        self.puntos = pt

    def Generar(self):
        self.texto.insert(1.0, self.text)
        self.texto.config(font=('Calibri', self.puntos, 'bold'),
                            bg=self.fondo,
                            bd=0,
                            state=DISABLED,
                            width=600,
                            heigh=2
                            )

    def isVisible(self, x, y):
        self.texto.place(relx=x, rely=y)

    def isOculto(self):
        self.texto.place_forget()

    def setText(self, text):
        self.texto.config(state=NORMAL)
        self.texto.delete(1.0 ,tk.END)
        self.texto.insert(1.0, text)
        self.texto.config(state=DISABLED)