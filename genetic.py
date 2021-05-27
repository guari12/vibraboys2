import random
from numpy.lib.shape_base import kron
from simulated_anneling import anneling,layout, ley_enfriamiento
from LayoutAlmacen import Almacen


class genetic():

    def __init__(self,almacen,_cant_poblacion,_list_ordenes,_T,_cant_prod=108):
        self.almacen = almacen
        self.cant_poblacion = _cant_poblacion #Numeros de individuos de una poblacion
        self.cant_pro=_cant_prod
        self.poblacion=[]                     #Poblacion inicial 
        #Creacion de la poblacion incial 
        self.set_poblacion()
        self.cant_iter=10
        self.list_ordenes=_list_ordenes
        self.k=round(self.cant_poblacion*0.5)
        self.T=_T   #Agenda de enfriamiento

    def genoma(self):
        return random.sample(range(1,self.cant_pro+1),self.cant_pro)
    
    def set_poblacion(self):
        for i in range(self.cant_poblacion):
            self.poblacion.append(self.genoma())

    #La funcion de fitness hace uso del temple simulado para obtener una medida de idoneidad
    def fitness(self,individuo):

        fit=0
        self.almacen.cargarProductos(individuo)
        for order in self.list_ordenes :

            ordenesPosiciones = list(map(lambda x:self.almacen.getPosicionProducto(x),order))

            temple=anneling(ordenesPosiciones ,self.T,self.almacen.obstaculos,2,[0,0],[0,0],fin=True)
            [way,resultado,E]=temple.search()
            fit+=E[-1]
            
        return  fit/len(self.list_ordenes)

    def cross_over(self,cant_cross=1):
        
        pares=[random.sample(self.poblacion_best,2) for i in range(round(self.cant_poblacion/2))]
        self.poblacion=[]

        for i in range(round(self.cant_poblacion/2)):
            
            individuo_aux1=pares[i][0]
            individuo_aux2=pares[i][1]

            index=random.sample(range(len(individuo_aux1)),2*cant_cross)
            index.sort()

            aux1=individuo_aux2[index[0]:index[1]]
            aux2=individuo_aux1[index[0]:index[1]]

            for j in [aux1.copy(),aux2.copy()]:
                
                aa=0
                if j==aux1:
                    aux3=[]
                    aux3=individuo_aux1[index[1]:]
                    aux3.extend(individuo_aux1[0:index[0]])
                    individuo=individuo_aux1
                    aux4=aux2

                if j==aux2:
                    aux3=[]
                    aux3=individuo_aux2[index[1]:]
                    aux3.extend(individuo_aux2[0:index[1]])
                    individuo=individuo_aux2
                    aux4=aux1

                for i in aux3:
                    
                    if i in j:

                        pass

                    elif (len(j)+index[0])>=len(individuo):

                        j.insert(aa,i)
                        aa+=1
                        
                    else:

                        j.append(i)

                    if aux3.index(i)==len(aux3)-1:

                        if len(j)==len(individuo):
                            pass

                        if len(j)<len(individuo):
                            for i in range((len(individuo)-len(j))):
                                index2=0
                                aux5=aux4[index2]
                                while aux5 in j:
                                    index2+=1
                                    aux5=aux4[index2]

                                if (len(j)+index[0])>=len(individuo):

                                    j.insert(aa,aux5)
                                    aa+=1
                                    
                                else:

                                    j.append(aux5)

                self.poblacion.append(j) 

        if len(self.poblacion)<self.cant_poblacion:

            self.poblacion.append(self.poblacion_best[0])

    def get_best(self):

        list_fit=[]                 #Lista de fitness
        self.poblacion_best=[]      #Lista con los mejores

        it=0
        dictor={}

        for invididuo in self.poblacion:

            list_fit.append(self.fitness(invididuo))
            dictor[list_fit[-1]]=it
            it+=1        

        list_fit.sort()
            
        for i in range(self.k):

            index=dictor[list_fit[i]]
            self.poblacion_best.append(self.poblacion[index])
             


    def process(self):
        
        #Se selecciona los k mejores individuos
        it=0
        while it<self.cant_iter:

            self.get_best()
            self.cross_over()
            print(it,'\n')
            it+=1

        return self.poblacion_best[0]
        
        
