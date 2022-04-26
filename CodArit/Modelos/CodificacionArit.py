from Controladores.Controlador import Controlador
class Codificacion:
    prob = []
    controlador = Controlador()
    def probabilidades(self, con, mensaje):
        valor = list(con)
        for x in range(len(valor)):
            valor[x] = str(int((valor[x]/len(mensaje)*100)))
        while len(valor) < 5:
            valor.append('0')
        self.prob = valor
        return self.prob

    def limites(self, prob):
        limite = []
        sum = 0
        for x in range(len(prob)):
            limite.append([sum/100, (sum+int(prob[x]))/100])
            sum = sum + int(prob[x])
        return limite

    def Codificar(self, mensaje, prob, key):
        limites = self.limites(prob)
        list1=[]
        list1[:0]=mensaje
        Ma = dict(zip(key, limites))
        Mc = [[0 , 1]]
        i = 0
        for x in list1:
            ai = Ma[x]
            Mc.append([(Mc[i][0] + (Mc[i][1] - Mc[i][0])*ai[0]),
                 (Mc[i][0] + (Mc[i][1] - Mc[i][0])*ai[1])])
            i = i + 1
        while len(Mc) < 10:
            Mc.append('')
        self.controlador.setDecimal(Mc[i][0])
        self.Binario(Mc[i][0])
        self.Decodificacion(Mc[i][0], Ma, list1)
        self.controlador.setCodificacion(Mc)
        return Mc

    def Binario(self, dec):
        dec = self.controlador.getDecimal()
        dec2 = dec
        val = 0
        ent = 0
        bina = '0.'
        i = 1
        while val < dec:
            dec2 = dec2*2
            ent = int(dec2)
            bina = bina + str(ent)
            dec2 = dec2 - ent
            val = round(((pow(2, -i))*ent) + val, len(str(dec))-2)
            i=i+1
        self.controlador.setBinario(bina)

    def Decodificacion(self, dec, Ma, lis):
        a = dec
        mensaje = ''
        limites = list(Ma.values())
        la = [[0, 0]]
        keys = list(Ma.keys())
        D = []
        for x in lis:
            limit = limites[1][0]
            if a >= limites[0][0] and a < limites[0][1]:
               mensaje = mensaje + keys[0] 
               la = [limites[0][0], limites[0][1]]
            elif a >= limites[1][0] and a < limites[1][1]:
                mensaje = mensaje + keys[1]
                la = [limites[1][0], limites[1][1]]
            elif a >= limites[2][0] and a < limites[2][1]:
                mensaje = mensaje + keys[2]
                la = [limites[2][0], limites[2][1]]
            elif a >= limites[3][0] and a < limites[3][1]:
                mensaje = mensaje + keys[3]
                la = [limites[3][0], limites[3][1]]
            elif a >= limites[4][0] and a < limites[4][1]:
                mensaje = mensaje + keys[4]
                la = [limites[4][0], limites[4][1]]
            
            a = (a-la[0])/(la[1]-la[0])
            D.append(a)
        while len(D) < 10:
            D.append('')
        self.controlador.setDecodificacion(D)
        
