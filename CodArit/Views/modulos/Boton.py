import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk


class Boton:
    def __init__(self, frame, colorBotones, colorFondo, horizontal, vertical, texto, funct):
        self.boton = Canvas(frame)
        self.color = colorBotones
        self.fondo = colorFondo
        self.x = horizontal
        self.y = vertical
        self.text = texto
        self.funcion = funct

    def generarOvalado(self):
        self.boton.config(bg=self.fondo, highlightthickness=0,
                          width=162, height=62)
        self.boton.create_oval(
            0, 0, 160, 60, fill=self.color, outline=self.color)
        self.boton.create_text(80, 30, fill=self.fondo,
                               font="Calibri 16 bold", text=self.text)
        self.utilidad()

    def generarCuadrado(self):
        self.boton.config(bg=self.color, highlightthickness=0,
                          width=160, height=40)
        self.boton.create_rectangle(
            0, 0, 160, 40, fill=self.color, outline=self.color)
        self.boton.create_text(80, 20, fill=self.fondo,
                               font="Calibri 20 bold", text=self.text)
        self.utilidad()

    def generarCirculo(self):
        self.boton.config(bg=self.fondo, highlightthickness=0,
                          width=100, height=100)
        self.boton.create_oval(
            0, 0, 100, 100, fill=self.color, outline=self.color)
        self.boton.create_text(50, 50, fill=self.fondo,
                               font="Calibri 16 bold", text=self.text)
        self.utilidad()

    def utilidad(self):
        self.boton.place(relx=self.x, rely=self.y)
        self.boton.bind("<Button-1>", self.funcion)
