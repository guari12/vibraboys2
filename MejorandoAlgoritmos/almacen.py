from random import randint

class Almacen():
    limits_x = [0,28]
    limits_y = [0,30]
    limits = [limits_x,limits_y]

    estanterias_X = [1,2]
    estanterias_X_size = 2
    estanterias_Y = [1,2,3,4]
    estanterias_Y_size = 4
    pasillos = 2

    Dist_Estantes = [estanterias_X,estanterias_X_size,estanterias_Y,estanterias_Y_size]

    def __init__(self,plot=False):
        
        self.matriz_deposito = []
        self.estanterias_coord = []

        #almacen de productos
        # elemento = {    "id":0,
        #                 "almacen_id":None, #id de almacen
        #                 "pos":[x,y],
        #                 "x":x,
        #                 "y":y,
        #                 "almacen":True #True/False si es almacen o camino
        #                 #"free":True, #True/False si es camino y tiene objeto o no
        #                 #"prod":id_prod #or a None if it hasn't a product
        #                 }
        _id = 1
        _almacen_id = 1

        # Llenar la matriz del almacen (se comento el mapa)
        for y in range(Almacen.limits[1][1]): #limite en Y
            for x in range(Almacen.limits[0][1]): #limite en X
                xx = x%(Almacen.estanterias_X_size+Almacen.pasillos)
                yy = y%(Almacen.estanterias_Y_size+Almacen.pasillos)
                #print(f"X: {x} ({xx}), Y: {y} ({yy})",end="\t")
                if (xx in Almacen.estanterias_X) and (yy in Almacen.estanterias_Y):
                    elemento = {"id":_id,
                                "almacen_id":_almacen_id, #id de almacen
                                "pos":[x,y],
                                "x":x,
                                "y":y,
                                "almacen":True
                                }
                    if plot:
                        print("#",end=" ") #Almacen
                    _almacen_id += 1
                    self.estanterias_coord.append([x,y])

                else:
                    elemento = {"id":_id,
                                "almacen_id":None, #id de almacen
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
        self.restricciones = self.estanterias_coord

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
        id_end = randint(1,len(self.estanterias_coord))
        #ID_end = self.getPosicionEstante(id_end)
        return self.getPosicionEstante(id_end)

    def getPosicionEstante(self,id_estante):
        id_estante+=1
        for posicion in self.matriz_deposito:
            if posicion["almacen_id"] == id_estante:
                ID_end = posicion["id"]
                break
        else:
            print("el estante",id_estante,"esta fuera de rango")

        posicionFinal = self.matriz_deposito[ID_end-1]["pos"]
        #remueve el punto final de las restricciones porque si se puede llegar a el
        restricciones = list(filter(lambda x: x != posicionFinal,self.estanterias_coord))
        #self.estanterias_coord.copy().remove(self.matriz_deposito[ID_end-1]["pos"])
        return posicionFinal,restricciones