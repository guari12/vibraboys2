
#Implementar un algoritmo genético para resolver el problema de optimizar la ubicación de los
#productos en el almacén, de manera de optimizar el picking de los mismos. Considere que

from genetic import genetic
import random
import numpy as np
from simulated_anneling import anneling,layout, ley_enfriamiento
from LayoutAlmacen import Almacen
from leerOrdenes import getOrdenes


cant_ordenes=10    #Cantidad de ordenes que se desean leer

#Lee las ordenes de un archivo
list_order=getOrdenes("orders.txt")

#Parametros del modelo
len_enfria=200  #Longitud de la ley de enfriamiento
coef_exp=1.5    #Coef de caida exponelcia de la temperatura
tem_max=5000    #Temperatur maxima
# cant_ordenes=2  #Cantidad de ordenes
# len_ordenes=5  #Longitud de ordenes

# list_order=[]

# for i in range(cant_ordenes):
#     order_aux=random.sample(range(10),len_ordenes)
#     list_order.append(order_aux)


# Se crea el layout
almacen=Almacen()

T=ley_enfriamiento(tem_max,len_enfria,coef_exp)
#Creacion de la poblacion incial


cant_poblacion = 10 #Numeros de individuos de una poblacion
alg_genetic=genetic(almacen,cant_poblacion,list_order,T)
print(alg_genetic.process())



