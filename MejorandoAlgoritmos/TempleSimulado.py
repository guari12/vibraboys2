from random import randint
from math import exp
from multi_A_estrella import resolverCamino
import time

class TempleSimulado():

    def __init__(self,almacen,inicio_,intermedios_,fin_=None,temp=1000,alfa=0.9995,tolerancia=0.00000001):
        self.alfa = alfa
        self.tolerancia = tolerancia
        self.almacen = almacen
        self.inicio = inicio_ # Es la posicion de la que parto
        if fin_ == None: # Y esta la posicion a la que quiero llegar
            self.fin = self.inicio
        else:
            self.fin = fin_
        
        self.estanterias_pos = []
        self.estanterias_id = intermedios_
        for int in intermedios_:
            pos,restricc = almacen.getPosicionEstante(int)
            self.estanterias_pos.append(pos) # Armo un vector con todos los lugares por donde tengo que pasar

        # empezar con una configuracion de inicio
        self.Temp = [temp] # registro de temperaturas
        self.estados = [] # registro de estados por los que paso
        self.energias = [] # la energia que le corresponde a cada estado
        
        self.estado_actual = self.generarEstadoAleatorio(self.estanterias_pos) #generar estado de forma aleatoria
        self.energia_actual = self.calculateE(self.estado_actual)

        #necesito ir guardando el estado actual o nuevo, el anterior y el mejor de todos
        self.estados.append(self.estado_actual)
        self.energias.append(self.energia_actual)

        self.prob1 = []
        self.prob2 = []

    def start(self):
        it = 0
        while not abs(self.Temp[-1]) <= abs(self.tolerancia): # mientras la temperatura este en un cierto rango
            print(self.Temp[-1],"°C")
            self.estado_siguiente = self.generarVecino(self.estado_actual)
            while self.estado_siguiente in self.estados:
                self.estado_siguiente = self.generarVecino(self.estado_actual)
            self.energia_siguiente = self.calculateE(self.estado_siguiente)

            deltaE = (self.energia_siguiente - self.energia_actual)*(-1) # si la energia sig es menor (menos distancia), es un mejor estado, la energia tiene que ser positiva
            # se da vuelta para que cuando el delta sea negativo el estado sea peor es por la probabilidad
            # Busco minimizar la energia, o energia minima

            if deltaE >= 0:
                self.decreaseTemp()
                self.estado_actual = self.estado_siguiente
                self.energia_actual = self.energia_siguiente

            elif self.calculateProbability(deltaE,self.Temp[-1]):
                #print("Elijo un estado peor")
                self.estado_actual = self.estado_siguiente
                self.energia_actual = self.energia_siguiente

            self.estados.append(self.estado_actual)
            self.energias.append(self.energia_actual)

            it+=1
            self.decreaseTemp() # Decrece la temperatura

        minE = min(self.energias)
        index = self.energias.index(minE)
        mejorEstado = self.estados[index]

        ides = []
        for mej in mejorEstado:
            ind = self.estanterias_pos.index(mej)
            ides.append(self.estanterias_id[ind])

        #al finalizar el bucle while
        return ides,mejorEstado,minE,self.energias,self.Temp,self.prob1,self.prob2

    def decreaseTemp(self,iter=None):
        newTemp = self.Temp[-1]*self.alfa
        self.Temp.append(newTemp) #la temperatura va decreciendo de uno en uno

    def calculateE(self,state):
        energia = self.calculateDistance(self.inicio,state[0])
        for i in range(len(state)-1):
            energia += self.calculateDistance(state[i],state[i+1])
        energia += self.calculateDistance(state[-1],self.fin)
        
        return energia
    """
    def calculateE2(self,state):
        vect,E = resolverCamino(self.almacen,self.inicio,state)
        return E
    """
    def calculateDistance(self,A,B):
        dist = 0
        for i in range(len(A)):
            dist += abs(A[i]-B[i])**2
        dist **= 0.5
        return dist

    def estaEstudiado(self,state):
        for estado in self.estados:
            if self.sonIguales(state,estado):
                return True
        else:
            return False

    def sonIguales(self,A,B):
        for i in range(len(A)):
            if A[i] == B[i]:
                pass
            else:
                return False
        else:
            return True
    
    def generarVecino(self,est):
        # Generar un indice aleatorio para hacer un swap
        new = est.copy()
        index_a = randint(0,len(est)-1)
        index_b = randint(0,len(est)-1)
        while index_b == index_a:
            index_b = randint(0,len(est)-1)
        new[index_a], new[index_b] = new[index_b], new[index_a]
        return new
        
    def calculateProbability(self,E,temp):
        if E>0:
            print("Error el delta energia no puede ser positivo")
        else:
            prob = exp(E/temp) # Calcula un valor de probabilidad
            num = randint(0,100)/100

            elijo = (num < prob)
            if elijo == True:
                self.prob1.append(prob)
                self.prob2.append(num)


            return elijo # supongo que son decimales, devuelvo True or False

    def generarEstadoAleatorio(self,paso):
        paso2 = []
        copiaSeg = paso.copy()
        while len(copiaSeg)>0:
            paso2.append(copiaSeg.pop(randint(0,len(copiaSeg)-1)))
        return paso2
