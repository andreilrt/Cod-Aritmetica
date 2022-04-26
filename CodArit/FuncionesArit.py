class validaciones:
    def validacion_probabilidades(self,probabilidades):
        prob = 0
        for x in range(len(probabilidades)):
            prob = prob + probabilidades[x]
        if prob == 1:
            return True
        else:
            return False

    def validacion_numerica_int(self,opcion):
        try:
            opcion = int(opcion)
        except:
            return False
        else:
            return True
    
    def validacion_numerica_float(self,numero):
        try:
            numero = float(numero)
        except:
            return False
        else:
            return True

    def validar_numero_caracteres(self,mensaje):
        if len(mensaje) > 10:
            print("El mensaje excede de 10 caracteres.")
            return False
        else:
            return True
    
    def validar_alfabeto(self,letters):
        if len(letters) > 5:
            print("El alfabeto tiene más de 5 caracteres.")
            return False
        else:
            return True

class funciones:
    
    def probabilidades(self,letters):
        valores = list(letters.values())
        suma = 0
        for x in range(len(valores)):
            suma = suma + valores[x]
        for x in range(len(valores)):
            valores[x] = valores[x]/suma
        return valores

    def ingresar_probabilidades(self,letters,a):
        alfabeto = list(letters.keys())
        probabilidades = alfabeto
        while (a<len(letters)):
            prob = input(f"Digite la probabilidad para {alfabeto[a]}: ")
            if self.v.validacion_numerica_float(prob)==False:
                self.ingresar_probabilidades(letters,a)
            else:
                probabilidades[a] = float(prob)
                a = a+1
        a = 0
        if self.v.validacion_probabilidades(probabilidades)==False:
            print("La suma de probabilidades no es 1.")
            respuesta = input("Te recomiendo permitir que el programa realice automaticamente las probabilidades.\nDigita S para permitir esto o cualquier otra tecla para ingresar nuevamente las probabilidades: ")
            if respuesta.upper()=="S":
                probabilidades = self.probabilidades(letters)
                return probabilidades
            else:
                self.ingresar_probabilidades(letters,a)
        else:
            return probabilidades

    def letter_count(self,text):
        text = text.lower()
        letters = {}
        for x in range(len(text)):
            letters[text[x]] = letters.get(text[x], 0) + 1
        return letters

    def recibir_mensaje(self):
        mensaje = input("Digite el mensaje: ")
        return mensaje

    def menu(self,letters):
        opcion = input("Digite 1 si quiere que el programa calcule las probabilidades.\nDigite 2 si quiere ingresar las probabilidades.\n")
        if self.v.validacion_numerica_int(opcion)==False:
            self.menu(letters)
        else:
            opcion = int(opcion)
            if opcion == 1:
                probabilidades = self.probabilidades(letters)
                return probabilidades
            else:
                if opcion == 2:
                    a = 0
                    probabilidades = self.ingresar_probabilidades(letters,a)
                    return probabilidades

    def limites_recta(self,prob):
        puntos = [0.0]
        limites = []
        for x in range(len(prob)):
            puntos.append(puntos[x]+prob[x])
            limites.append((puntos[x],puntos[x+1]))
        return limites

    def Convert(self,string): 
        list1=[] 
        list1[:0]=string 
        return list1 

    def obt_valor_codificar(self,mensaje,letters,limites):
        mensaje = self.Convert(mensaje)
        alfabeto = list(letters.keys())
        a = 0
        b = 1
        for x in range(len(mensaje)):
            (ai,bi) = limites[alfabeto.index(mensaje[x])]
            (a,b) = (a+(b-a)*ai,a+(b-a)*bi)
        valor_a_codificar = a
        return valor_a_codificar
        
    v = validaciones()

class principal:
    
    
    def proceso(self):
        mensaje = self.f.recibir_mensaje()
        letters = self.f.letter_count(mensaje)
        probabilidades = [.2,.2,.2,.2,.2]
        limites = self.f.limites_recta(probabilidades)
        print(limites)
        valor_a_codificar = self.f.obt_valor_codificar(mensaje,letters,limites)
        print(valor_a_codificar) 

    f = funciones()
    v = validaciones()       

p = principal()
p.proceso()