from random import randint
import math
from arbol import reduccion,ampliar,amplificar,reducir,A_estrella

#Resolver robot 6gdl con algoritmo A*
gdl = 6
q_lim = [[-140,140],[-150,150],[0,180],[-400,400],[-180,180],[-360,360]] #lim min y max

#gdl = 4
#q_lim = [[-14,14],[-15,15],[-13,13],[-18,18]] #lim min y max
#q_lim = [[-140,140],[-150,150],[0,180],[-400,400]]#,[-5,5]] #lim min y max

#Genero aleatoriamente posiciones inicial y final
qi = [] # aleatorio
qf = [] # aleatorio
for i in range(gdl):
    qi.append(randint(q_lim[i][0],q_lim[i][1]))
    qf.append(randint(q_lim[i][0],q_lim[i][1]))

qi = [-140,150,0,400,-180,360]
qf = [140,-150,180,-400,180,-360]

#Proponer obstaculos y restricciones aleatorias en el camino
cant_obstaculos = 0
obstaculos = []
tol_obstaculo = 1 #no me puedo acercar a 1 grados de los obstaculos

# Tomar un paso mas grande =====================================================================
# print(f"Inicio: {qi}")
# print(f"Final: {qf}")
camino = []

escal = 100

qir = reducir(escal,qi,"int")
qfr = reducir(escal,qf,"int")

print(f"Inicio: {qir}")
print(f"Final: {qfr}")

print(reduccion(escal,q_lim))
algoritmo = A_estrella(qir,qfr,gdl,reduccion(escal,q_lim))
algoritmo.vecinos_type = "COMPLETOS" #"COMPLETOS"(en diagonales)/"SIMPLES"(mov. rectos)
solucion,q,g,h = algoritmo.start()

solucion = amplificar(escal,solucion)
camino.extend(solucion)

print(camino[-1])

escal = 20
qir = reducir(escal,camino[-1],"int")
qfr = reducir(escal,qf,"int")

algoritmo = A_estrella(qir,qfr,gdl,reduccion(escal,q_lim))
algoritmo.vecinos_type = "COMPLETOS" #"COMPLETOS"(en diagonales)/"SIMPLES"(mov. rectos)
solucion,q,g,h = algoritmo.start()
solucion = amplificar(escal,solucion)
camino.extend(solucion)


algoritmo = A_estrella(camino[-1],qf,gdl,q_lim)
algoritmo.vecinos_type = "COMPLETOS" #"COMPLETOS"(en diagonales)/"SIMPLES"(mov. rectos)
solucion,q,g,h = algoritmo.start()
camino.extend(solucion)


print(camino)

matlab=False


if matlab:
    #print(f"\n\nInicio: {qi}\n {qI}")
    #print("\nCamino:")
    #print(camino[1])
    #print(f" ... {len(camino)-2} ...")
    #for q in camino:
    #    print(q)
    #print(camino[-2])

    #print(f"\nFinal: {qf}\n {qF}")

    print("\n\nMATLAB ===================")
    print("qt = [")
    #print(f"       {qi}".replace(","," ").replace("[","").replace("]",""),";")
    ite = 0
    for q in camino:
        ite+=1
        if ite%2 == 0:
            continue
        q[0] *= math.pi/180
        q[1] *= math.pi/180
        q[2] /= 1000
        q[3] *= math.pi/180
        print(f"       {q}".replace(","," ").replace("[","").replace("]","")," ;")
    #print(f"       {qf}".replace(","," ").replace("[","").replace("]",""),";")
    print("                                ];")

print("Trayectoria final")


print("FIN")