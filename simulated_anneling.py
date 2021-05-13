import numpy as np
import random
import math
from A_estrella import A_star,nodos,nodo_inicial

class anneling(): 

    def __init__(self,_order,_T,_obstaculos,_spatialdimension,inicio,list_fin,fin=False):

        self.order=_order
        self.tolerancia = 10**(-4) # cuando la temperatura esta muy cerca de cero termina
        self.T=_T
        self.t=len(_T)
        self.d=len(self.order)
        self.d2=self.d
        self.ds=_spatialdimension
        self.obstaculos=_obstaculos
        self.actual_state=_order
        self.next_stateaux=[]
        self.start=inicio
        self.end=fin
        self.list_end=list_fin
        
        if self.end==False:
            self.d2=self.d2-1

        self.list_energy=[]
        self.E1=self.energy(self.actual_state.copy())


    def next_state(self):
        #it=0
        #while(True):

        aux=self.actual_state.copy()
        index=random.sample(range(self.d),2)
        aux[index[0]],aux[index[1]] = self.actual_state[index[1]],self.actual_state[index[0]]
        
        return aux
            #if (aux in self.next_statelist):
            #    pass

            #else:
            #    return aux

            #if (it==1000):
             #   return aux
            
            #it+=1
    
    def energy(self,state,camino_total=False):
        
        list_way=[]
        way=0

        if (self.end):
            state.append(self.list_end)
            
          
        state.insert(0,self.start)

        for i in range(self.d2+1):

            A_object=A_star(state[i+1],state[i],self.ds,1,self.obstaculos)

            if camino_total==True:
                
                list_way.extend(A_object.buscar_camino(camino_total=True))
            
            else:
                way+=A_object.buscar_camino()

        if camino_total==True:
            return list_way
        else:
            return way


    def probability(self,delta_energy,Temp):

        return math.exp(delta_energy/Temp)

    def search(self):
        it=0
        for i in range(self.t):
            it+=1
            #print("Variacion Temperatura",self.T[i])
            if abs(self.T[i])==0 or it==100:
                return self.energy(self.actual_state.copy(),camino_total=True),self.actual_state,self.list_energy

            self.next_stateaux=self.next_state()
            E2=self.energy(self.next_stateaux.copy())
            deltaenergy=self.E1-E2

            if deltaenergy>0:
                it=0
                self.actual_state=self.next_stateaux
                self.E1=E2

            else:

                prob=self.probability(deltaenergy,self.T[i])
                choise=random.choices([0,1],[1-prob,prob])
                if (choise[0]==1): 
                    self.actual_state=self.next_stateaux
                    self.E1=E2

            self.list_energy.append(self.E1)



    



    