
#Implementar un algoritmo genético para resolver el problema de optimizar la ubicación de los
#productos en el almacén, de manera de optimizar el picking de los mismos. Considere que

from cache import Cache
from LayoutAlmacen import Almacen
from simulated_anneling import anneling, ley_enfriamiento
from genetic import genetic
from leerOrdenes import getOrdenes

import random
import numpy as np

import matplotlib.pyplot as plt
import time
import os

cant_ordenes=10    #Cantidad de ordenes que se desean leer

#Lee las ordenes de un archivo
path, _ = os.path.split(os.path.abspath(__file__))
list_order=getOrdenes("orders.txt")

#Parametros del modelo
len_enfria=200  #Longitud de la ley de enfriamiento
coef_exp=1.5    #Coef de caida exponelcia de la temperatura
tem_max=5000    #Temperatur maxima
# cant_ordenes=2  #Cantidad de ordenes
# len_ordenes=5  #Longitud de ordenes

almacen = Almacen(plot=True)
cache = Cache(almacen)

T=ley_enfriamiento(tem_max,len_enfria,coef_exp)
#Creacion de la poblacion incial

cant_poblacion = 10 #Numeros de individuos de una poblacion
alg_genetic=genetic(almacen,cache,cant_poblacion,list_order,T)
print(alg_genetic.process())
