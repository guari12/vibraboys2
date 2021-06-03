class csp():
    pass
    def __init__(self):
        self.X = []
        self.D = []
        self.C = []

def ac3(csp): #receive binary CSP (X,D,C)
    queue = csp.C # cola de arcos, inicialmente los arcos en el csp
            # []
    while len(queue)>0:
        Xi,Xj = queue.pop(0)["alcance"] # saco el primer elemento
        if revise(csp,Xi,Xj):
            if len(csp.Di)==0:
                return False
            for Xk in csp.vecinos(Xi): #
                    pass #
    return True

def revise(csp,Xi,Xj):
    revised = False
    for x in csp.D[i]: # (m1,1)....,(m3,1)...
        #hay_y = 
        # hay un "y" en "Dj" que cumpla que (x,y) satisface restricciones entre (Xi,Xj)
        # sino, eliminar ese x del dominio Di y poner revised como true
        pass #
    return revised
def exist(x,y):
    pass