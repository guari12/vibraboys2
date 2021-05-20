from A_estrella import A_estrella
from almacen import Almacen
from graficar import mapa

def resolverCamino(almacen,inicio,estanterias,final=None):

    caminoTotal = []
    distTotal = 0

    # Defino todos mis puntos de interes
    start_pos = inicio
    if final==None:
        end_pos = inicio
    else:
        end_pos = final
    
    est_posiciones = []
    est_restricciones = []
    for est in estanterias:
        est_p,est_r = almacen.getPosicionEstante(est)
        est_posiciones.append(est_p)
        est_restricciones.append(est_r)

    # Primer trayectoria
    algoritmo = A_estrella(start_pos,est_posiciones[0],2,almacen.limits,est_restricciones[0])
    algoritmo.vecinos_type = "SIMPLES" #"COMPLETOS"(en diagonales)/"SIMPLES"(mov. rectos)
    solucion,qfinal,g,h = algoritmo.start()
    distTotal+=g
    caminoTotal.append(solucion)

    for i in range(1,len(est_posiciones)):
        # Segunda trayectoria
        algoritmo = A_estrella(qfinal,est_posiciones[i],2,almacen.limits,est_restricciones[i])
        algoritmo.vecinos_type = "SIMPLES" #"COMPLETOS"(en diagonales)/"SIMPLES"(mov. rectos)
        solucion,qfinal,g,h = algoritmo.start()
        distTotal+=g
        caminoTotal.append(solucion)

    # Ultima trayectoria
    algoritmo = A_estrella(qfinal,end_pos,2,almacen.limits,almacen.restricciones)
    algoritmo.vecinos_type = "SIMPLES" #"COMPLETOS"(en diagonales)/"SIMPLES"(mov. rectos)
    solucion,qfinal,g,h = algoritmo.start()
    distTotal+=g
    caminoTotal.append(solucion)

    # Camino final y distancia, esto es lo que tengo que devolver
    # graficos.printCaminos(caminoTotal,marcarPuntos=1,animar=0.01,hilo=True)
    # print(f"Distancia Total: {distTotal}")
    return caminoTotal,distTotal