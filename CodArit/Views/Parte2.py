import tkinter as tk
from tkinter import *
from Views.modulos.Boton import Boton
from Views.modulos.Texto import Texto
from Views.modulos.IngresoData import IngresoData
import Views.ViewFuntion.Common as Common
from Views.modulos.BarraProb import BarraProb
from Controladores.Controlador import Controlador
from Modelos.CodificacionArit import Codificacion

class Parte2:
    principal = None
    parte3 = None
    controlador = Controlador()
    barra = None

    def __init__(self, root, colorBotones, colorFondo):
        self.parte2 = Frame(root)
        self.color = colorBotones
        self.fondo = colorFondo

    def getFrames(self, principal, parte3):
        self.principal = principal
        self.parte3 = parte3

    def generar(self):
        self.parte2.config(bg=self.fondo, width='700', heigh='500')
        # Textos
        textos = []
        textos.append(
            [Texto(self.parte2, 'Barra de probabilidades', self.fondo, 20), .3, .1])
        textos.append([Texto(
            self.parte2, '(Las probabilidades son de sugerencia)', self.fondo, 14), .3, .4])
        textos.append(
            [Texto(self.parte2, 'o Ingresar las suyas: ', self.fondo, 14), .4, .5])
        Common.generarTextos(textos)
        # Barra de probabilidades
        self.barra = BarraProb(self.parte2, self.fondo, .1, .2)
        # Inputs
        inputs = []
        inputs.append(IngresoData(self.parte2, .15, .6, .1))
        inputs.append(IngresoData(self.parte2, .3, .6, .1))
        inputs.append(IngresoData(self.parte2, .45, .6, .1))
        inputs.append(IngresoData(self.parte2, .6, .6, .1))
        inputs.append(IngresoData(self.parte2, .75, .6, .1))
        Common.generarInputs(inputs)
        # Botones
        def recaulcular(inputs):
            i = 0
            for x in inputs:
                if x.getData() != '' or x.getData() != None:
                    pass
                else:
                    i = i + 1
            if i == 0:
                sum = int(inputs[0].getData())+int(inputs[1].getData())+int(inputs[2].getData())+int(inputs[3].getData())+int(inputs[4].getData())
                if sum == 100:
                    self.barra.destruir()
                    self.barra.generar(inputs[0].getData(), inputs[1].getData(),
                    inputs[2].getData(), inputs[3].getData(), inputs[4].getData())
                    prob = [inputs[0].getData(), inputs[1].getData(),
                    inputs[2].getData(), inputs[3].getData(), inputs[4].getData()]
                    keys = Common.ocurencia(self.principal.Mensaje)
                    keys = keys.keys()
                    CA = Codificacion()
                    self.controlador.setCodificacion(CA.Codificar(self.principal.Mensaje, prob, keys))
                else:
                    inputs[0].Limpiar()
                    inputs[1].Limpiar()
                    inputs[2].Limpiar()
                    inputs[3].Limpiar()
                    inputs[4].Limpiar()
            else:
                pass

        botonRecalcular = Boton(self.parte2, self.color, self.fondo, .4, .75,
                                'Recalcular', lambda event: {recaulcular(inputs)})
        botonRecalcular.generarCuadrado()
        botonAtras = Boton(self.parte2, self.color, self.fondo, .05, .8, 'Atras', lambda event: {
                           self.isOculto(), self.principal.isVisible(), self.barra.destruir()})
        botonAtras.generarOvalado()
        botonSiguiente = Boton(self.parte2, self.color, self.fondo, .7, .8,
                               'Siguiente', lambda event :{self.isOculto(),
            self.parte3.isVisible(),
            self.parte3.textos[1][0].setText(f'{self.controlador.getMensaje()}'),
            self.parte3.textos[3][0].setText(f'{self.controlador.getDecimal()}'),
            self.parte3.textos[5][0].setText(f'{self.controlador.getBinario()}')})
        botonSiguiente.generarOvalado()

    def isVisible(self):
        self.parte2.pack()

    def isOculto(self):
        self.parte2.pack_forget()
