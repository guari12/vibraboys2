import random
from simulated_anneling import anneling,layout, ley_enfriamiento



class genetic():

    def __init__(self,_cant_poblacion,_list_ordenes,_obstaculos,_layout,_T):
        self.cant_poblacion = _cant_poblacion #Numeros de individuos de una poblacion
        self.poblacion=[]                     #Poblacion inicial 
        self.colm=12
        self.row=9
        #Creacion de la poblacion incial 
        self.set_poblacion()
        self.list_ordenes=_list_ordenes
        self.obstaculos=_obstaculos
        self.layout=_layout
        self.n=len(self.poblacion)
        self.T=_T   #Agenda de enfriamiento

    def genoma(self):

        individuo=[]
        aux=random.sample(range(1,109),108)
        for i in range(self.row):

            individuo.append(aux[i*self.colm:(i+1)*self.colm])

        return individuo
    
    def set_poblacion(self):
        for i in range(self.cant_poblacion):
            self.poblacion.append(self.genoma())

    #La funcion de fitness hace uso del temple simulado para obtener una medida de idoneidad
    def fitness(self,individuo):
        #Se busca las coordenadas de estos puntos en el layout
        
        fit=0
        for order in self.list_ordenes :
            list_order2=[]
            for q2 in order:

                it=0

                for q in individuo :


                    if q2 in q:

                        a=q.index(q2)
                        aux=self.obstaculos[it*(len(q)-1)+a]
                        list_order2.append(aux)

                    it +=1

            temple=anneling(list_order2,self.T,self.obstaculos,2,[0,0],[0,0],fin=True)
            [way,resultado,E]=temple.search()
            fit+=fit+E[-1]
            
        return  fit/len(self.list_order)

    def cross_over(self,cant_cross=1):
        
        pares=[[random.sample(self.poblacion_best,2)] for i in range(round(self.n)/2)]
        self.poblacion=[]

        for i in range(round(self.n)/2):
            
            index_colm=[[0,0]]
            index_row=[[0,0]]
            index_colm.append([random.sample(self.colm,cant_cross)])
            index_row.append([random.sample(self.row,cant_cross)])
            individuo_aux1=pares[i][1]
            individuo_aux2=pares[i][2]
            aux1=[]
            aux2=[]

            for j in range(cant_cross):

                if j%2==0:

                    aux1.append(individuo_aux2[index_row[j]:index_row[j+1]][index_colm[j]:index_colm[j+1]])
                    aux2.append(individuo_aux1[index_row[j]:index_row[j+1]][index_colm[j]:index_colm[j+1]])

                else:

                    aux1.append(individuo_aux1[index_row[j]:index_row[j+1]][index_colm[j]:index_colm[j+1]])
                    aux2.append(individuo_aux2[index_row[j]:index_row[j+1]][index_colm[j]:index_colm[j+1]])  

            self.poblacion.append(aux1,aux2)    


    def process(self):
        
        #Se selecciona los k mejores individuos
        it=0
        while it<1000:

            k=round(self.n*0.4)
            list_fit=[]
            self.poblacion_best=[]

            for invididuos in self.poblacion:

                list_fit.append(self.fitness(invididuos))

            dictor=dict.fromkeys(list_fit,range(self.cant_poblacion))      

            list_fit.sort()
            
            for i in list_fit:
                self.poblacion_best.append(dictor[i])

            self.cross_over()

            it+=1

        return self.poblacion_best[-1]
        
        
