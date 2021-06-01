
#Implementar un algoritmo genético para resolver el problema de optimizar la ubicación de los
#productos en el almacén, de manera de optimizar el picking de los mismos. Considere que

from cache import Cache
from simulated_anneling import ley_enfriamiento
from LayoutAlmacen import Almacen
from genetic import genetic
from leerOrdenes import getOrdenes

import numpy as np
import matplotlib.pyplot as plt
import os
import random


#Lee las ordenes de un archivo
path, _ = os.path.split(os.path.abspath(__file__))
list_order=getOrdenes("orders.txt")
# cant_ordenes=1  #Cantidad de ordenes
# len_ordenes=5  #Longitud de ordenes
# # Genera ordenes aleatorias
# aux=random.sample(range(20),len_ordenes) 
# list_order=[random.sample(range(100),len_ordenes)  for i in range(cant_ordenes) ]

#Parametros del modelo
len_enfria=400  #Longitud de la ley de enfriamiento
coef_exp=1.1    #Coef de caida exponelcia de la temperatura
tem_max=5000    #Temperatur maxima
T=ley_enfriamiento(tem_max,len_enfria,coef_exp)

almacen2 = Almacen(plot=True)
cache = Cache(almacen2)
cant_poblacion = 20 #Numeros de individuos de una poblacion

#Se realiza el algoritmo genetico
alg_genetic=genetic(almacen2,cache,cant_poblacion,list_order,T)
best_individuo,list_fit=alg_genetic.process()

#--------------------------------------------------------------------------------------
#                   Se imprime el mejor individuo y se grafica los fitness
#--------------------------------------------------------------------------------------

print(best_individuo)
print(list_fit)

plt.figure(1)
plt.xlabel("Fitness")
plt.ylabel("it")
plt.plot(np.linspace(0,(len(list_fit)-1),len(list_fit)),list_fit)

#--------------------------------------------------------------------------------------
# Se carga el mejor individuo al almacen y se realiza un analisis con todas las ordenes
#--------------------------------------------------------------------------------------
