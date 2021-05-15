#Dada una orden de pedido, que incluye una lista de productos del almacén anterior que deben
#ser despachados en su totalidad, determinar el orden óptimo para la operación de picking
#mediante Temple Simulado. ¿Qué otros algoritmos pueden utilizarse para esta tarea
import random
import colorama
import numpy as np
from colorama import Fore,Style
import matplotlib.pyplot as plt
import time
from simulated_anneling import anneling, layout, ley_enfriamiento


colorama.init() #Libreria que me permite camibar el color de salida del print()

lista_A=[]      #Lista que contiene el mapeo del layout
osbtaculos=[]   #Lista que contiene las direccion de las estanterias dentro de lista_A, que van a ser consideradas como obstaculos por nuestro algoritmo A*

#Parametros del modelo
len_enfria=200  #Longitud de la ley de enfriamiento
coef_exp=1.5    #Coef de caida exponelcia de la temperatura
tem_max=5000    #Temperatur maxima
cant_ordenes=1  #Cantidad de ordenes
len_ordenes=5  #Longitud de ordenes

E2=np.zeros((len_enfria))
list_E2=[]



# Se crea el layout asignando un numero a cada estanteria y con '*' a los pasillos
[lista_A,osbtaculos]=layout()


#Genera ordenes aleatorias
list_order=[]
order_aux=random.sample(range(100),len_ordenes)
#[2, 3, 5, 7, 14, 15, 17, 40, 41, 44, 58, 65, 67, 75, 78, 84, 88, 110, 112, 118]


for i in range(cant_ordenes):
    
    list_order.append(order_aux)


#Ley de enfriamiento
T=ley_enfriamiento(tem_max,len_enfria,coef_exp)

time_ini=time.time()

#Se realiza el temple orden por orden
for order in list_order:

    #Se busca las coordenadas de estos puntos en el layout
    list_order2=[]
    for q2 in order:

        it=0

        for q in lista_A:

            if q2 in q:

                a=q.index(q2)
                list_order2.append([it,a])

            it +=1

    temple=anneling(list_order2,T,osbtaculos,2,[0,0],[0,0],fin=True)
    [way,resultado,E]=temple.search()

    order2=[]
    for i in resultado:
        order2.append(lista_A[i[0]][i[1]])
    
    print(f"El mejor camino para realizar las ordenes {order} es: {order2} \n\n")
    
    tim=time.time()-time_ini
    print(tim)
    list_E2.append(E[-1])
    E2+=np.array(E)
    plt.plot(np.linspace(0,(len(E)-1),len(E)),np.array(E))


for i in way:

    lista_A[i[0]][i[1]]="O"

for i in list_order2:

    lista_A[i[0]][i[1]]="P"

stirng=""
for q in lista_A:

    for i in q:

        stirng+="{:^5}".format(i)

    stirng+="\n\n"

print(f"El mejor camino para realizar las ordenes {order} es: {order2} \n\n")
print(stirng.replace("O",Fore.RED+ Style.BRIGHT+"O"+Style.RESET_ALL).replace("P",Fore.GREEN+ Style.BRIGHT+"P"+Style.RESET_ALL))
E2=E2/cant_ordenes
plt.plot(np.linspace(0,(len(E2)-1),len(E2)),E2)
print(f"Promedio:{E2[-1]}")
print(f"Lista de energia finales:{list_E2}")

plt.show()
