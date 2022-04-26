from Modelos.CodificacionArit import Codificacion
from Controladores.Controlador import Controlador

def generarTextos(textos):
    i = 0
    for text in textos:
        text[0].Generar()
        text[0].isVisible(text[1], text[2])
        i = i + 1

def generarInputs(inputs):
    i=0
    for inp in inputs:
        inp.ingreso()
        i = i + 1

def ocurencia(mensaje):
    if len(mensaje) > 10:
        return 1
    else:
        mensaje = mensaje.lower()
        letters = {}
        for x in range(len(mensaje)):
		        letters[mensaje[x]] = letters.get(mensaje[x],0) + 1
        return letters

def ObtenerConcurrencia(mensaje):
    CA = Codificacion()
    con = Controlador()
    letters = ocurencia(mensaje)
    if len(mensaje) > 10:
        return 1
    else:
        mensaje = mensaje.lower()
        letters = {}
        for x in range(len(mensaje)):
		        letters[mensaje[x]] = letters.get(mensaje[x],0) + 1
        if len(letters) > 5:
            return 2
        else:
            for letra in mensaje:
                c = ord(letra)
                if (c>=97 and c<=122) or (c>=48 and c<=57) or c==241 or c==32:
                    con.setProbabilidades(CA.probabilidades(letters.values(), mensaje))
                    con.setDecimal(CA.Codificar(mensaje, con.getProbabilidades(), letters.keys()))
                    CA.Binario(CA.Codificar(mensaje, con.getProbabilidades(), letters.keys()))
                    con.setBinario(CA.Binario(CA.Codificar(mensaje, con.getProbabilidades(), letters.keys())))
                    return con.getProbabilidades()
                else:
                    return 3

def cambiarText(lista, l, cod):
    i = 1
    for x in cod:
        if i > 0:
            lista[i][0].setText(f' {l}{i} = {cod[i-1]}')
        i = i + 1
