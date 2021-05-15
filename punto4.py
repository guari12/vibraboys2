
#Implementar un algoritmo genético para resolver el problema de optimizar la ubicación de los
#productos en el almacén, de manera de optimizar el picking de los mismos. Considere que

import random
import colorama
import numpy as np
from colorama import Fore,Style
import matplotlib.pyplot as plt
import time
from simulated_anneling import anneling,layout, ley_enfriamiento

cant_ordenes=100    #Cantidad de ordenes que se desean leer

#Lee las ordenes de un archivo
archivo=open('orders.txt')
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

# Se crea el layout asignando un numero a cada estanteria y con '*' a los pasillos
[lista_A,osbtaculos]=layout()



