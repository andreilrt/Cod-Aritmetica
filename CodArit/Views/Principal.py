import tkinter as tk
from tkinter import *
from Views.modulos.Boton import Boton
from Views.modulos.Texto import Texto
from Views.modulos.IngresoData import IngresoData
import Views.ViewFuntion.Common as Common
from Controladores.Controlador import Controlador

class Principal:
    creditos = None
    parte2 = None
    Mensaje = ''
    Error = ''
    mensaje = None
    controlador = Controlador()

    def __init__(self, root, colorBotones, colorFondo):
        self.principal = Frame(root)
        self.color = colorBotones
        self.fondo = colorFondo

    def getFrames(self, Creditos, parte2):
        self.creditos = Creditos
        self.parte2 = parte2

    def generar(self):
        self.principal.config(bg=self.fondo, width='700', heigh='500')
        # Textos
        textos = []
        textos.append(
            [Texto(self.principal, 'Codificación Aritmetica', self.fondo, 30), .20, .2])
        textos.append(
            [Texto(self.principal, 'Ingresar mensaje', self.fondo, 14), .4, .3])
        textos.append(
            [Texto(self.principal, 'Mensaje maximo de 10 caracteres y 5 simbolos :', self.fondo, 12), .28, .35])
        Common.generarTextos(textos)
        textoError = Texto(self.principal, self.Error, self.fondo, 14)
        textoError.Generar()
        # input
        self.mensaje = IngresoData(self.principal, .1, .45, .8)
        self.mensaje.ingreso()
        # Botones

        def Comenzar(event):
            self.Mensaje = self.mensaje.getData()
            self.controlador.setMensaje(self.Mensaje)
            textoError.isOculto()
            if Common.ObtenerConcurrencia(self.Mensaje) == 1:
                textoError.setText('Tamaño Invalido')
                textoError.isVisible(.35, .75)
                self.mensaje.Limpiar()
            elif Common.ObtenerConcurrencia(self.Mensaje) == 2:
                textoError.setText('Numero de Simbolos Invalido')
                textoError.isVisible(.35, .75)
                self.mensaje.Limpiar()
            elif Common.ObtenerConcurrencia(self.Mensaje) == 3:
                textoError.setText('Caracteres Especiales')
                textoError.isVisible(.35, .75)
                self.mensaje.Limpiar()
            else:
                self.controlador.setProbabilidades(Common.ObtenerConcurrencia(self.Mensaje))
                prob = self.controlador.getProbabilidades()
                self.parte2.barra.destruir()
                self.parte2.barra.generar(prob[0], prob[1], prob[2], prob[3], prob[4])
                self.parte2.isVisible()
                self.isOculto()

        botonCalcular = Boton(self.principal, self.color, self.fondo, .37, .6,
                              'Comenzar', Comenzar)
        botonCalcular.generarOvalado()
        botonCreditos = Boton(self.principal, self.color, self.fondo, .05, .85,
                              'Creditos', lambda event: {self.isOculto(), self.creditos.isVisible()})
        botonCreditos.generarCuadrado()
        botonSalir = Boton(self.principal, self.color,
                           self.fondo, .65, .85, 'Salir', lambda event: exit())
        botonSalir.generarCuadrado()

    def isVisible(self):
        self.principal.pack()

    def isOculto(self):
        self.principal.pack_forget()
