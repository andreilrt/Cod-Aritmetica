import tkinter as tk
from tkinter import *
from Views.Principal import Principal
from Views.Creditos import Creditos
from Views.Parte2 import Parte2
from Views.parte3 import Parte3
from Controladores.Controlador import Controlador
from Modelos.CodificacionArit import Codificacion
from Views.FCodificacion import FCodificar
from Views.FDecodificar import FDecodificar
#########################################################################################################
# Configuracion de la raiz
raiz = Tk()
raiz.title('Codificación Aritmetica')
raiz.iconbitmap('./usta.ico')
raiz.geometry('700x500')
raiz.resizable(0, 0)
raiz.config(bg='#FFFFFF')
# Variables Globales
colorBotones = "#2CDB00"
colorFondo = '#FFFFFF'
########################################################################################################
# Creacion de los Frame
# Frame Principal
principal = Principal(raiz, colorBotones, colorFondo)
principal.generar()
# Frame Creditos
creditos = Creditos(raiz, colorFondo, colorBotones)
creditos.generar()
# Frame part 2
parte2 = Parte2(raiz, colorBotones, colorFondo)
parte2.generar()
# Frame parte 3
parte3 = Parte3(raiz, colorBotones, colorFondo)
# Frame part4
cod = FCodificar(raiz, colorFondo, colorBotones)
cod.generar()
# Frame part5
dec = FDecodificar(raiz, colorFondo, colorBotones)
dec.generar()
# Modelos y Controlador
modelo = Codificacion()
controlador = Controlador()
# Navegacion
principal.getFrames(creditos, parte2)
creditos.getPrincipal(principal)
parte2.getFrames(principal, parte3)
parte3.getFrames(parte2, principal, controlador, cod, dec)
cod.getFrames(parte3)
dec.getFrames(parte3)

# Lol
parte3.generar()
principal.isVisible()
raiz.mainloop()
