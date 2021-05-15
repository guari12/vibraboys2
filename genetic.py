import random
from simulated_anneling import anneling,layout, ley_enfriamiento



class genetic():

    def __init__(self,_cant_poblacion):
        self.cant_poblacion = _cant_poblacion #Numeros de individuos de una poblacion
        self.poblacion=[]                     #Poblacion inicial 
        #Creacion de la poblacion incial 
        self.set_poblacion()

    def genoma(self,colm,row):   
        individuo=[]
        for i in range(row):
            individuo.append([random.sample(range(100),colm)])
    
    def set_poblacion(self):
        for i in range(self.cant_poblacion):
            self.poblacion.append(self.genoma(12,9))

    def fitness(self):
        pass