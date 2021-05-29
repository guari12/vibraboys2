import math
from A_estrella import A_star,nodos,nodo_inicial
import os
import json

class Cache():
    def __init__(self,almacen):
        self.almacen = almacen
        self.X = self.almacen.limits_x
        self.Y = self.almacen.limits_y

        self.path, _ = os.path.split(os.path.abspath(__file__))
        
        # =================================== Se crea una vez la cache ====================
        create = False
        if create:
            self.tabla = {}
            for j in range(self.Y[0],self.Y[1]):
                for i in range(self.X[0],self.X[1]):
                    # from i,j
                    dct = {}
                    From = [i,j]
                    for J in range(self.Y[0],self.Y[1]):
                        for I in range(self.X[0],self.X[1]):
                            # to I,J
                            To = [I,J]
                            D = -1
                            dct.update({f"{str(To)}":D})
                    self.tabla.update({f"{str(From)}":dct})
            #np.save(self.path+'/cache.npy', self.tabla)
            tf = open(self.path+"/cache.json", "w")
            json.dump(self.tabla,tf)
            tf.close()
            print("Se creo el cache")
        # =================================================================================
        #self.tabla = np.load(self.path+'/cache.npy', allow_pickle='TRUE')
        tf = open(self.path+"/cache.json", "r")
        self.tabla = json.load(tf)
        tf.close()
        print("Se abrio la cache")
        
    def distanciaEntre(self,A,B,ds,obstaculos):
        # Buscarla ?
        From = str(A)
        To = str(B)
        d = self.tabla[From][To]
        if d<0:
            print("Hay que calcular distancia")
            A_object=A_star(A,B,ds,1,obstaculos)
            d = A_object.buscar_camino()
            self.tabla[From][To] = d
            self.tabla[To][From] = d
            print("Actualizar cache")
            tf = open(self.path+"/cache.json", "w")
            json.dump(self.tabla,tf)
            tf.close()
            return d
            
        else:
            print("La distancia es:",d)
            return d
        