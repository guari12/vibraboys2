
from random import randint
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

from A_estrella import A_estrella
from almacen import Almacen
from graficar import mapa
from leerOrdenes import getOrdenes
from multi_A_estrella import resolverCamino
from TempleSimulado import TempleSimulado

import time

print("INICIO")
almacen = Almacen()

#limits = [[0,36],[0,36]]
#estanterias_X_pos = [1,2]
#estanterias_X_size = 2
#estanterias_Y_pos = [1,2,3,4]
#estanterias_Y_size = 4

graficos = mapa(Almacen.limits,Almacen.Dist_Estantes)
graficos.start()
time.sleep(1)

# Cargo las ordenes de pedidos ==================================================================
empiezoEn = almacen.getPosicion(581)
ordenes = getOrdenes()
orden1 = ordenes[0] # lista de id de almacenes

# Orden original =============================================================================
start_time = time.time() # tiempo al iniciar el algoritmo A*

solucion,distTotal = resolverCamino(almacen,empiezoEn,orden1,final=None)
print(solucion)
#graficos.printCaminos(solucion,marcarPuntos=2,animar=0.5,hilo=False)
print(f"Distancia Total camino original: {distTotal}")

elapsed_time = time.time() - start_time # tiempo al terminar de unir todos los puntos 
print("Elapsed time: %.10f seconds." % elapsed_time)

# Mejorar con temple =============================================================================
start_time = time.time() # tiempo al iniciar el temple

temple = TempleSimulado(almacen,empiezoEn,orden1,temp=1000,alfa=0.9995,tolerancia=0.001)
mejorEstado,coordenadas,mejorE,evolucionE,evolucionT,prob1,prob2 = temple.start()

elapsed_time = time.time() - start_time # tiempo al terminar de unir todos los puntos 
print("Elapsed time: %.10f seconds." % elapsed_time)

print(mejorEstado)
print(mejorE)
plt.subplot(2,2,1)
plt.plot(evolucionE)

plt.subplot(2,2,2)
plt.plot(evolucionT)

plt.subplot(2,2,3)
X,Y = [empiezoEn[0]],[-empiezoEn[1]]
for x,y in coordenadas:
    X.append(x)
    Y.append(-y)
X.append(empiezoEn[0])
Y.append(-empiezoEn[1])
plt.plot(X,Y,marker='o', linestyle='--', color='r')

plt.subplot(2,2,4)
plt.plot(prob1,".")
#plt.plot(prob2,".")

plt.show()


# Orden "mejorada" =============================================================================
graficos.resetMapa()
input("Presiona enter para salir...")
start_time = time.time() # tiempo al iniciar el algoritmo A*

solucion,distTotal = resolverCamino(almacen,empiezoEn,mejorEstado,final=None)
print(f"Distancia Total camino mejorado: {distTotal}")

elapsed_time = time.time() - start_time # tiempo al terminar de unir todos los puntos 
print("Elapsed time: %.10f seconds." % elapsed_time)

graficos.printCaminos(solucion,marcarPuntos=1,animar=0.01,hilo=False)

#time.sleep(5)
input("Presiona enter para salir...")

graficos.close()
print("FIN")