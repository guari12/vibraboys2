#Dada una orden de pedido, que incluye una lista de productos del almacén anterior que deben
#ser despachados en su totalidad, determinar el orden óptimo para la operación de picking
#mediante Temple Simulado. ¿Qué otros algoritmos pueden utilizarse para esta tarea
import random
import colorama
import numpy as np
from colorama import Fore,Style
import matplotlib.pyplot as plt
import time
from simulated_anneling import anneling


colorama.init() #Libreria que me permite camibar el color de salida del print()

lista_A=[]      #Lista que contiene el mapeo del layout
osbtaculos=[]   #Lista que contiene las direccion de las estanterias dentro de lista_A, que van a ser consideradas como obstaculos por nuestro algoritmo A*

it=0
aa=1

# Se crea el layout asignando un numero a cada estanteria y con '*' a los pasillos
for i in range(16):

    lista_aux=[]

    if i%5==0:
        lista_aux.extend( ["*" for j in range(16)])
    else:

        for j in range(16):
            if aa%3==1:
                lista_aux.append("*")
            
            else:
                it +=1
                lista_aux.append(it)
                osbtaculos.append([i,j])
            aa +=1
    lista_A.append(lista_aux)
    aa=1

# #Lee las ordenes de un archivo
# archivo=open('orders.txt')
# ordertxt=archivo.read()
# list_order=[]
# for i in range(1,100):
#     index1=ordertxt.find('Order'+' '+f'{i}')
#     index2=ordertxt.find('Order'+' '+f'{i+1}')
#     aux=ordertxt[(index1+len('Order'+' '+f'{i}')):index2]
#     list_aux2=aux.split('\nP')
#     list_aux2.pop(0)
#     list_aux2[-1]=list_aux2[-1].replace('\n\n','')
#     list_aux2=list(map(int,list_aux2))
#     list_order.append(list_aux2)
    
list_order=[]
#random.sample(range(120),20)
order_aux= [3, 5, 15, 19, 22, 30, 32, 33, 34, 39, 44, 47, 58, 61, 77, 98, 100, 115, 116, 117]
order_aux.sort()
for i in range(10):
    
    list_order.append(order_aux)


#Ley de enfriamiento
T=[10000]
it=1
for i in range(700):
    # if i %100==0 and it<4 :
    #     it+=1
    #     T.append(10)
    # else:
    T.append(T[-1]/1.05)
T[-1]=0

time_ini=time.time()
#Se realiza el temple orden por orden
for order in list_order:

    #Se busca las coordenadas de estos puntos en el layout
    list_order2=[]
    list_order1=[]
    for q2 in order:
        it=0

        for q in lista_A:
            if q2 in q:
                a=q.index(q2)

                # if q2>50:
                list_order2.append([it,a])
                # else:
                #     list_order1.append([it,a])

            it +=1

    temple=anneling(list_order2,T,osbtaculos,2,[0,0],[0,0],fin=True)
    [way,resultado,E]=temple.search()

    # temple2=anneling(list_order2,T,osbtaculos,2,way[-1],[0,0],fin=True)
    # [way2,resultado2,E]=temple2.search()

    # way.extend(way2)
    # resultado.extend(resultado2)

    order2=[]
    for i in resultado:
        order2.append(lista_A[i[0]][i[1]])
    
    print(f"El mejor camino para realizar las ordenes {order} es: {order2} \n\n")
    
    tim=time.time()-time_ini
    print(tim)
    plt.plot(np.linspace(0,(len(E)-1),len(E)),np.array(E))


for i in way:
    lista_A[i[0]][i[1]]="O"

list_order2.extend(list_order1)
for i in list_order2:

    lista_A[i[0]][i[1]]="P"

stirng=""
for q in lista_A:
    for i in q:
        stirng+="{:^5}".format(i)

    stirng+="\n\n"

print(f"El mejor camino para realizar las ordenes {order} es: {order2} \n\n")
print(stirng.replace("O",Fore.RED+ Style.BRIGHT+"O"+Style.RESET_ALL).replace("P",Fore.GREEN+ Style.BRIGHT+"P"+Style.RESET_ALL))

plt.plot(np.linspace(0,(len(T)-1),len(T)),np.array(T))

plt.show()
