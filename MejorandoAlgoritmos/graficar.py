import pygame
import random
import time
import _thread # para hacer multihilos
#from almacen import Almacen

pasada = 0
estanteria = 1
inicio = 2
final = 3
recorrido = 4
estante = 5

class mapa():
    # Colores
    BLUE = (20, 34, 238)
    GREEN = (20, 240, 50)
    RED = (230, 0, 20)
    BLACK = (0, 0, 0)
    WHITE = (250,250,250)
    YELLOW = (240,240,20)
    GRAY = (30,30,30)
    VIOLET = (250,0,250)
          # camino,estant,inicio,fin,recorr,estant.
    Color = [WHITE,GRAY,GREEN,RED,BLUE,YELLOW,VIOLET]
    sizeSquare = 20

    def __init__(self,limits,distrib_estantes):
        # Distribucion del almacen
        self.estanterias_X_pos = distrib_estantes[0]
        self.estanterias_X_size = distrib_estantes[1]
        self.estanterias_Y_pos = distrib_estantes[2]
        self.estanterias_Y_size = distrib_estantes[3]

        # Crear mapa
        self.cantCol = limits[0][1]
        self.cantRow = limits[1][1]
        
        pygame.init()
        self.size = (mapa.sizeSquare*self.cantCol, mapa.sizeSquare*self.cantRow)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Almacen on PYGAME")
        self.clock = pygame.time.Clock()
        self.gameOver = False
        self.matrix = []
        for i in range(self.cantCol):
            subM = []
            for j in range(self.cantRow):
                xx = i%(self.estanterias_X_size+2)
                yy = j%(self.estanterias_Y_size+2)
                if (xx in self.estanterias_X_pos) and (yy in self.estanterias_Y_pos):
                    subM.append(estanteria)
                else:
                    subM.append(pasada)
            self.matrix.append(subM)

    def start(self):
        _thread.start_new_thread( self.mostrarMapa,() )

    # Muestra el mapa completo y lo va actualizando =======================================================
    def mostrarMapa(self):
        while not self.gameOver:
            self.screen.fill(mapa.BLACK)
            i=0
            for X in range(1, self.size[0], self.sizeSquare):
                j=0
                for Y in range(1, self.size[1], self.sizeSquare):
                    # pygame.draw.rect(self.screen, mapa.WHITE, [i, j, self.sizeSquare-2, self.sizeSquare-2], 0)
                    xx = (i)%(self.estanterias_X_size+2)
                    yy = (j)%(self.estanterias_Y_size+2)
                    elemento = self.matrix[i][j]
                    pygame.draw.rect(self.screen, mapa.Color[elemento], [X, Y, self.sizeSquare-2, self.sizeSquare-2], 0)
                    
                    j+=1
                i+=1
            pygame.display.flip()
            #self.clock.tick(5)
        pygame.quit()
    
    def resetMapa(self):
        for i in range(self.cantCol):
            subM = []
            for j in range(self.cantRow):
                xx = i%(self.estanterias_X_size+2)
                yy = j%(self.estanterias_Y_size+2)
                if (xx in self.estanterias_X_pos) and (yy in self.estanterias_Y_pos):
                    self.matrix[i][j]=estanteria
                else:
                    self.matrix[i][j]=pasada
    """
    def mostrarObstaculos(self,X,Y):
        colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
        pygame.draw.rect(self.screen, mapa.BLUE, [X*self.sizeSquare, Y*self.sizeSquare, self.sizeSquare-2, self.sizeSquare-2], 0)
        pygame.display.flip()
        #self.clock.tick(5)
    """

    def printCaminos(self,caminos,marcarPuntos=0,animar=0,hilo=True,reset=False):
        if hilo:
            _thread.start_new_thread( self.animarCaminos,(caminos,marcarPuntos,animar,False,reset) )
        else:
            self.animarCaminos(caminos,marcarPuntos=marcarPuntos,animar=animar,hilo=False,reset=reset)

    def animarCaminos(self,caminos,marcarPuntos=0,animar=0,hilo=False,reset=False):
        inicio = caminos[0][0]
        final = caminos[-1][-1]
        #intermedios = []
        ultimos = []
        for c in caminos[0:-1]:
            #intermedios.append(c[0])
            ultimos.append(c[-1])
        
        if marcarPuntos>0:
            self.mostrarInicio(inicio)
            self.mostrarFinal(final)
            for i in range(len(ultimos)):
                self.mostrarEstante(ultimos[i])
            time.sleep(marcarPuntos)
        
        for c in caminos:
            if reset:
                self.resetMapa()
            self.printCamino(c,animar,hilo)

    def printCamino(self,camino_,animar=0,hilo=True):
        if hilo:
            _thread.start_new_thread( self.animar,(camino_,animar) )
        else:
            self.animar(camino_,animar)

    def animar(self,camino_,animar=0):
        camino = camino_.copy()
        q_0 = camino.pop(0)
        q_f = camino.pop(-1)
        self.mostrarInicio(q_0)
        time.sleep(animar)

        for q in camino:
            self.mostrarCamino(q,6)
            time.sleep(animar)
            self.mostrarCamino(q)
        
        self.mostrarFinal(q_f)
        time.sleep(animar)

    # Sirven para animar cada celda del mapa del almacen ==================================================
    def mostrarCamino(self,pos,state=recorrido):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est

    def borrarCamino(self,pos,state=pasada):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est
    
    def mostrarEstante(self,pos,state=estante):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est

    def borrarEstante(self,pos,state=estanteria):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est

    def mostrarInicio(self,pos,state=inicio):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est

    def borrarInicio(self,pos,state=pasada):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est
    
    def mostrarFinal(self,pos,state=final):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est

    def borrarFinal(self,pos,state=pasada):
        X = pos[0]
        Y = pos[1]
        est = self.matrix[X][Y]
        self.matrix[X][Y] = state
        return est

    # Para cerrar el ploteo y terminar ====================================================================
    def close(self):
        self.gameOver = True
        time.sleep(1)
        pygame.quit()


# graphics = mapa()
# graphics.start()
# graphics.mostrarCamino(2,5)

# for j in range(Almacen.limits_y[1]):
#     for i in range(Almacen.limits_x[1]):
#         ant = graphics.mostrarCamino(i,j)
#         time.sleep(0.01)
#         ant = graphics.borrarCamino(i,j,ant)
# ant = graphics.mostrarCamino(i,j,3)
# input("Presiona enter para salir...")
# graphics.close()