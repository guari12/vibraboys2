# empiezo a la brevedad
# Este es mi brach de trabajo
from random import randint

class Almacen():
    col = 6
    row = 3

    estanterias_X_size = 2
    estanterias_Y_size = 3
    pasillos = 1

    def __init__(self,col=None,row=None,estantesX=None,estantesY=None,pasillos=None,plot=False):
        if col == None:
            self.col = Almacen.col
        else:
            self.col = col
        if row == None:
            self.row = Almacen.row
        else:
            self.row = row

        if estantesX == None:
            self.estanterias_X_size = Almacen.estanterias_X_size
        else:
            self.estanterias_X_size = estantesX
        self.estanterias_X = list(range(1,self.estanterias_X_size+1))
        if estantesY==None:
            self.estanterias_Y_size = Almacen.estanterias_Y_size
        else:
            self.estanterias_Y_size = estantesY
        self.estanterias_Y = list(range(1,self.estanterias_Y_size+1))
        if pasillos == None:
            self.pasillos = Almacen.pasillos
        else:
            self.pasillos = pasillos

        self.limits_x = [0,self.col*(self.estanterias_X_size+self.pasillos)+1]
        self.limits_y = [0,self.row*(self.estanterias_Y_size+self.pasillos)+1]
        self.limits = [self.limits_x,self.limits_y]

        self.Dist_Estantes = [  self.estanterias_X,
                                self.estanterias_X_size,
                                self.estanterias_Y,
                                self.estanterias_Y_size     ]
        
        self.matriz_deposito = []
        self.estanterias = [] #Guardo los objetos estanterias
        self.obstaculos = [] #guardo posiciones X,Y

        _id = 1
        _almacen_id = 1

        # Llenar la matriz del almacen (se comento el mapa)
        for y in range(self.limits[1][1]): #limite en Y
            for x in range(self.limits[0][1]): #limite en X
                xx = x%(self.estanterias_X_size+self.pasillos)
                yy = y%(self.estanterias_Y_size+self.pasillos)
                #print(f"X: {x} ({xx}), Y: {y} ({yy})",end="\t")
                if (xx in self.estanterias_X) and (yy in self.estanterias_Y):
                    elemento = {"id":_id,
                                "pos":[x,y],
                                "x":x,
                                "y":y,
                                "almacen":True,
                                "almacen_id":_almacen_id, #id de almacen
                                "producto":_almacen_id
                                }
                    if plot:
                        #print(_almacen_id,end=" ")
                        print("#",end=" ") #Almacen
                    _almacen_id += 1
                    self.estanterias.append(elemento)
                    self.obstaculos.append([x,y])

                else:
                    elemento = {"id":_id,
                                "pos":[x,y],
                                "x":x,
                                "y":y,
                                "almacen":False
                                }
                    if plot:
                        print(".",end=" ") #Camino
                self.matriz_deposito.append(elemento)
                _id += 1
            if plot:
                print()
        # Aca ya tengo mi almacen creado como matriz
        self.restricciones = self.estanterias

    def inicioAleatorio(self):
        # Genero el nodo inicial que tambien es el final ================================================
        # Elegir al azar algun nodo de inicio (no puede ser almacen)
        ID_start = randint(1,len(self.matriz_deposito))

        while self.matriz_deposito[ID_start-1]["almacen"] == True:
            ID_start = randint(1,len(self.matriz_deposito)) #cambiar la eleccion
        
        return self.getPosicion(ID_start)

    def getPosicion(self,ID_):
        return self.matriz_deposito[ID_-1]["pos"]

    def finalAleatorio(self):
        id_end = randint(1,len(self.estanterias))
        #ID_end = self.getPosicionEstante(id_end)
        return self.getPosicionEstante(id_end)

    def getPosicionEstante(self,id_estante):
        if id_estante+1<len(self.estanterias):
            posicionFinal = self.estanterias[id_estante+1]["pos"]
            return posicionFinal
        else:
            print("el estante",id_estante,"esta fuera de rango")
            return False
        
    def getPosicionProducto(self,producto):
        for estanteria in self.estanterias:
            if estanteria["producto"]==producto:
                posicion = self.estanterias["pos"]
                return posicion
        else:
            print(f"No se encontro el producto {producto}")
            return None

    def cargarProductos(self,layout):
        for prod in layout:
            self.estanterias["producto"]=prod

Almacen(plot = True)