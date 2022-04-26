import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

class BarraProb:
    def __init__(self, frame, colorFondo, horizontal, vertical):
        self.barra = Canvas(frame)
        self.fondo = colorFondo
        self.x = horizontal
        self.y = vertical

    def generar(self, prob1, prob2, prob3, prob4, prob5):
        p1 = (int(prob1)/100)*560
        p2 = (int(prob2)/100)*560
        p3 = (int(prob3)/100)*560
        p4 = (int(prob4)/100)*560
        p5 = (int(prob5)/100)*560
        self.barra.config(bg=self.fondo, highlightthickness=0, width=560, height=42)
        sum = 0
        self.barra.create_rectangle(0, 0, p1, 40, fill='#0C0DED', outline='#0C0DED')
        self.barra.create_text(sum + 10, 20, text=f'{prob1}')
        sum = p1 + sum
        self.barra.create_rectangle(sum, 0,sum + p2, 40, fill='#0C4CF7', outline='#0C4CF7')
        self.barra.create_text(sum + 10, 20, text=f'{prob2}')
        sum = p2 + sum
        self.barra.create_rectangle(sum, 0,sum + p3, 40, fill='#0178E0', outline='#0178E0')
        self.barra.create_text(sum + 10, 20, text=f'{prob3}')
        sum = p3 + sum
        self.barra.create_rectangle(sum, 0,sum + p4, 40, fill='#0CC8F7', outline='#0CC8F7')
        self.barra.create_text(sum + 10, 20, text=f'{prob4}')
        sum = p4 + sum
        self.barra.create_rectangle(sum, 0,sum + p5, 40, fill='#0CEDDF', outline='#0CEDDF')
        self.barra.create_text(sum + 10, 20, text=f'{prob5}')
        self.barra.place(relx=self.x, rely=self.y)

    def destruir(self):
        self.barra.place_forget()