

def ac3(csp): #receive binary CSP (X,D,C)
    queue = csp.C # cola de arcos, inicialmente los arcos en el csp
            # []
    while len(queue)>0:
        Xi,Xj = queue.pop(0)["alcance"] # saco el primer elemento
        if revise(csp,Xi,Xj):
            if len(csp.Di)==0:
                return False
            for Xk in csp.vecinos(Xi): #
                # buscar en restricciones todos los que tengan Xi, y sacar el otro
                    pass #
    return True

def revise(csp,Xi,Xj):
    i = Xi["id"]
    j = Xj["id"]
    revised = False
    for x in csp.D[i]: # (m1,1)....,(m3,1)... para Xi

        # Existe algun y talque (x,y) satisfacen restricciones entre (Xi,Xj) ===========
        hay_y = False
        for y in csp.D[j]: # (m3,1)....,(m4,1)... para Xj
            # si x,y satisfacen las restricciones de Xi, Xj
            restricciones = csp.getRestricciones(Xi,Xj)
            for solucion in restricciones["extension"]:
                if [x,y] == solucion: # si mi par x,y es alguno de los x,y posibles
                    hay_y = True # entonces hay un y que cumple
                    break
            if hay_y: # si ya encontre un "y", no busco otros
                break
        # ==============================================================================
        
        if hay_y==False: # if no value y in Dj...
            pass #delete x from Di
            revised = True
            
    return revised
