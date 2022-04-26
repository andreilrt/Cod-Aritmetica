import tkinter as tk
from tkinter import *
from Views.modulos.Boton import Boton
from Views.modulos.Texto import Texto
import Views.ViewFuntion.Common as Common
import Controladores.Controlador as Con

class Parte3:
    Principal = None
    Parte2 = None
    cod = None
    dec = None
    Codificacion = None
    Decodificacion = None
    controlador = None 
    textos = []

    def __init__(self, root, colorBotones, colorFondo):
        self.parte3 = Frame(root)
        self.color = colorBotones
        self.fondo = colorFondo

    def getFrames(self, parte2, Principal, controlador, cod, dec):
        self.Parte2 = parte2
        self.Principal = Principal
        self.controlador = controlador
        self.cod = cod
        self.dec = dec

    def generar(self):
        self.parte3.config(bg=self.fondo, width='1000', heigh='500')
        # Textos
        self.textos.append([Texto(self.parte3, 'El mensaje : ', self.fondo, 20), .3, .1])
        self.textos.append([Texto(self.parte3, f'{self.controlador.getMensaje()}', self.fondo, 20), .2, .2])
        self.textos.append([Texto(self.parte3, 'En Decimal : ', self.fondo, 20), .3, .3])
        self.textos.append([Texto(self.parte3, f'{self.controlador.getDecimal()}', self.fondo, 20), .2, .4])
        self.textos.append([Texto(self.parte3, 'En Binarios : ', self.fondo, 20), .3, .5])
        self.textos.append([Texto(self.parte3, f'{self.controlador.getBinario()}', self.fondo, 20), .05, .6])
        Common.generarTextos(self.textos)
        # Botones
        botonAtras = Boton(self.parte3, self.color, self.fondo, .1, .7, 'Atras', lambda evet : {self.isOculto(), self.Parte2.isVisible()})
        botonAtras.generarCirculo()
        Cone = Con.Controlador()
        Codificacion = Cone.getCodificacion()
        def Codi(event):
            self.isOculto()
            self.cod.isVisible()
            Common.cambiarText(self.cod.textos, 'S', self.controlador.getCodificacion())

        botonCod = Boton(self.parte3, self.color, self.fondo, .4, .7, 'Codifica',Codi)
        botonCod.generarCirculo()
        def Deco(event):
            self.isOculto()
            self.dec.isVisible()
            Common.cambiarText(self.dec.textos, 'a', self.controlador.getDecodificacion())

        Codificacion = Cone.getDecodificacion()
        botonDec = Boton(self.parte3, self.color, self.fondo, .7, .7, 'Decodifica', Deco)
        botonDec.generarCirculo()
    def isVisible(self):
        self.parte3.pack()

    def isOculto(self):
        self.parte3.pack_forget()