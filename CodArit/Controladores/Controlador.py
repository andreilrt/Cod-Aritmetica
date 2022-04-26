Mensaje = ''
Decimal = 0.0
Binario = ''
Codificacion = [[],[],[],[],[],[],[],[],[],[]]
Decodificacion = [[],[],[],[],[],[],[],[],[],[]]
probabilidades = ['20', '20', '20', '20', '20']
concurrencia = []

class Controlador:
    def setMensaje(self, mensaje):
        global Mensaje
        Mensaje = mensaje

    def getMensaje(self):
        return Mensaje

    def setConcurrencia(self, con):
        global concurrencia
        concurrencia = con

    def setDecimal(self, dec):
        global Decimal
        Decimal = dec

    def getDecimal(self):
        return Decimal

    def setBinario(self, bina):
        global Binario
        if bina != None :
            Binario = bina

    def getBinario(self):
        return Binario

    def setCodificacion(self, cod):
        global Codificacion
        Codificacion = cod

    def getCodificacion(self):
        return Codificacion

    def setDecodificacion(self, dec):
        global Decodificacion
        Decodificacion = dec

    def getDecodificacion(self):
        return Decodificacion

    def setProbabilidades(self, prob):
        global probabilidades
        probabilidades = prob

    def getProbabilidades(self):
        return probabilidades