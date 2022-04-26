import tkinter as tk
from tkinter import *
from Views.modulos.Boton import Boton
from Views.modulos.Texto import Texto
import Views.ViewFuntion.Common as Common
from Controladores.Controlador import Controlador


class FCodificar:
    parte3 = None
    con = Controlador()
    textos = []

    def __init__(self, root, colorFondo, colorBotones):
        self.cod = Frame(root)
        self.fondo = colorFondo
        self.color = colorBotones

    def getFrames(self, parte3):
        self.parte3 = parte3

    def generar(self):
        self.cod.config(bg=self.fondo, width='700', heigh='1000')
        # Textos
        Codificacion = self.con.getCodificacion()
        self.textos.append(
            [Texto(self.cod, 'Codificacion Paso a Paso', self.fondo, 20), .4, .05])
        self.textos.append(
            [Texto(self.cod, f'S0 = {Codificacion[0]}', self.fondo, 14), .3, .15])
        self.textos.append(
            [Texto(self.cod, f'S1 = {Codificacion[1]}', self.fondo, 14), .3, .2])
        self.textos.append(
            [Texto(self.cod, f'S2 = {Codificacion[2]}', self.fondo, 14), .3, .25])
        self.textos.append(
            [Texto(self.cod, f'S3 = {Codificacion[3]}', self.fondo, 14), .3, .3])
        self.textos.append(
            [Texto(self.cod, f'S4 = {Codificacion[4]}', self.fondo, 14), .3, .35])
        self.textos.append(
            [Texto(self.cod, f'S5 = {Codificacion[5]}', self.fondo, 14), .3, .4])
        self.textos.append(
            [Texto(self.cod, f'S6 = {Codificacion[6]}', self.fondo, 14), .3, .45])
        self.textos.append(
            [Texto(self.cod, f'S7 = {Codificacion[7]}', self.fondo, 14), .3, .5])
        self.textos.append(
            [Texto(self.cod, f'S8 = {Codificacion[8]}', self.fondo, 14), .3, .55])
        self.textos.append(
            [Texto(self.cod, f'S9 = {Codificacion[9]}', self.fondo, 14), .3, .6])
        Common.generarTextos(self.textos)
        # Botones
        botonRegresar = Boton(self.cod, self.color, self.fondo, .7, .8, 'Regresar', lambda event: {
                              self.isOculto(), self.parte3.isVisible()})
        botonRegresar.generarOvalado()

    def isVisible(self):
        self.cod.pack()

    def isOculto(self):
        self.cod.pack_forget()
