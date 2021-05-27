
#Implementar un algoritmo genético para resolver el problema de optimizar la ubicación de los
#productos en el almacén, de manera de optimizar el picking de los mismos. Considere que

from LayoutAlmacen import Almacen
from simulated_anneling import anneling, ley_enfriamiento
from genetic import genetic

import random
import numpy as np
<<<<<<< HEAD
from colorama import Fore,Style
import matplotlib.pyplot as plt
import time
import os
=======
from simulated_anneling import anneling,layout, ley_enfriamiento
from LayoutAlmacen import Almacen
from leerOrdenes import getOrdenes

>>>>>>> mejoras-genetic

cant_ordenes=10    #Cantidad de ordenes que se desean leer

#Lee las ordenes de un archivo
<<<<<<< HEAD
path, _ = os.path.split(os.path.abspath(__file__))
with open(path+'/orders.txt') as archivo:
    ordertxt=archivo.read()
    list_order=[]
    for i in range(1,cant_ordenes):

        index1=ordertxt.find('Order'+' '+f'{i}')
        index2=ordertxt.find('Order'+' '+f'{i+1}')
        aux=ordertxt[(index1+len('Order'+' '+f'{i}')):index2]
        list_aux2=aux.split('\nP')
        list_aux2.pop(0)
        list_aux2[-1]=list_aux2[-1].replace('\n\n','')
        list_aux2=list(map(int,list_aux2))
        list_order.append(list_aux2)
=======
list_order=getOrdenes("orders.txt")
>>>>>>> mejoras-genetic

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
<<<<<<< HEAD
"""
lista_A=[]      #Lista que contiene el mapeo del layout
osbtaculos=[]   #Lista que contiene las direccion de las estanterias dentro de lista_A, que van a ser consideradas como obstaculos por nuestro algoritmo A*

# Se crea el layout asignando un numero a cada estanteria y con '*' a los pasillos
[lista_A,osbtaculos]=layout()
"""
almacen = Almacen(plot=True)
=======


# Se crea el layout
almacen=Almacen()
>>>>>>> mejoras-genetic

T=ley_enfriamiento(tem_max,len_enfria,coef_exp)
#Creacion de la poblacion incial


cant_poblacion = 10 #Numeros de individuos de una poblacion
<<<<<<< HEAD
alg_genetic=genetic(almacen,cant_poblacion,list_order,almacen.obstaculos,T)
print(alg_genetic.process())
=======
alg_genetic=genetic(almacen,cant_poblacion,list_order,T)
print(alg_genetic.process())



>>>>>>> mejoras-genetic
