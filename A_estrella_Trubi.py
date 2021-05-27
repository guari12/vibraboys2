class A_estrella():

    def __init__(self,_qi,_qf,_dim,_qLims,_qRest=[]):
        Node.numNodes = 0 #Resetear los objetos Node (eliminar todos)

        self.dim = _dim

        self.qLims = _qLims
        self.qRest = _qRest

        self.distance_type = "MANHATTAN"
        self.vecinos_type = "SIMPLES" #"COMPLETOS"/"SIMPLES" (con diagonales o no)
        self.nodoInicial = Node(_qi,_g=0,_h=0,_father_id=0)
        self.nodoFinal = Node(_qf,_g=0,_h=0,_father_id=None) # no tiene ni G ni padre todavia

        #lista abierta, lista cerrada, posicion actual
        self.nodosAbiertos = []
        self.nodosCerrados = []
        

    def start(self):
        #nodos deben guardar ID, G, H, F, Padre
        #operaciones calcular G (euc o man) , H (euc o man)
        #actualizar listas abierta y cerrada, explorar vecinos, elegir menor camino

        self.nodoActual = self.nodoInicial
        self.id_nodoActual = self.nodoActual.id
        self.q_nodoActual = self.nodoActual.q

        self.nodosCerrados.append(self.nodoActual)

        it=0
        while not self.sonIguales(self.nodoActual.q,self.nodoFinal.q):
            vecinos = self.generarVecinos(self.nodoActual.q)

            #print(f"vecinos: {vecinos}")
            self.actualizarNodosAbiertos(vecinos)

            #Elegir el que tenga menor F
        
            minimoF = self.nodosAbiertos[0].f
            nodoMinimo = self.nodosAbiertos[0]

            for abierto in self.nodosAbiertos:
                if abierto.f < minimoF:
                    minimoF = abierto.f
                    nodoMinimo = abierto

            #actualizo mi nodo
            #print(f"Elijo: {nodoMinimo.q} -> Final: {self.nodoFinal.q}")
            self.nodoActual = nodoMinimo
            self.id_nodoActual = nodoMinimo.id
            self.q_nodoActual = nodoMinimo.q
            self.nodosAbiertos.remove(self.nodoActual)
            self.nodosCerrados.append(self.nodoActual)
        
            it+=1

        #print(f"A*>> Cantidad de Iteraciones: {it}")
        #print(f"A*>> Cantidad de Nodos: C:{len(self.nodosCerrados)} , A:{len(self.nodosAbiertos)} , T:{len(self.nodosAbiertos)+len(self.nodosCerrados)}")
        
        camino = [self.nodoActual.q]
        padreID = [self.nodoActual.father_id]

        while padreID[-1]!=0:
            nodoP = self.buscarEn(padreID[-1],self.nodosCerrados)
            camino.append(nodoP.q)
            padreID.append(nodoP.father_id)

        #camino.append(self.nodoFinal.q)
        camino.reverse()
        camino.insert(0,self.nodoInicial.q)

        return camino,camino[-2],self.nodoActual.g,self.nodoActual.h #

    def buscarEn(self,ide,lista):
        for nodo in lista:
            if nodo.id == ide:
                return nodo

    def actualizarNodosAbiertos(self,vecinos):
        for vec in vecinos: # Para cada pos de vecino generada
            for nodoA in self.nodosAbiertos: # compararlos con los nodos abiertos
                if self.sonIguales(vec,nodoA.q): # Si ya esta abierto actualizar
                    distancia = self.calculateG(vec,self.nodoActual)

                    if distancia < nodoA.g: #la distancia es mejor actualizar
                        nodoA.g = distancia # tengo que actualizar el nodo, porque encontre un mejor camino
                        nodoA.calculateF(distancia)
                        nodoA.father_id = self.nodoActual.id

                    pass # Ver si hay que actualizar ese nodo o no
                    break
            else: # Si termina y la pos no esta en los nodos abiertos, crear nuevo nodo
                newNodo = Node(vec,self.calculateG(vec,self.nodoActual),self.calculateH(vec),self.nodoActual.id)
                self.nodosAbiertos.append(newNodo)

    def calculateDistance(self,qA,qB,_type=None): # EUCLIDEA / MANHATTAN
        distance = 0
        if _type==None:
            #use defined distance
            if self.distance_type == "EUCLIDEA":
                for i in range(len(qA)):
                    distance += (qA[i] - qB[i])**2
                distance **= 0.5

            elif self.distance_type == "MANHATTAN":
                for i in range(len(qA)):
                    distance += abs(qA[i]-qB[i])

        elif _type == "EUCLIDEA":
            for i in range(len(qA)):
                distance += (qA[i] - qB[i])**2
            distance **= 0.5

        elif _type == "MANHATTAN":
            for i in range(len(qA)):
                distance += abs(qA[i]-qB[i])

        else:
            pass
            #show error or use a default method

        return distance

    def calculateH(self,q): #cost from actual node to target node
        H = 0
        
        H = self.calculateDistance(q,self.nodoFinal.q,"MANHATTAN")
        
        return H

    def calculateG(self,q,actual,_type="EUCLIDEA"):
        ge = actual.g
        ge += self.calculateDistance(q,actual.q,_type)
        return ge

    def sonIguales(self,A,B):
        iguales = True
        for i in range(len(A)):
            if A[i] == B[i]:
                iguales = True
            else:
                return False
        return iguales

    def generarVecinos(self,qq):
        if self.vecinos_type == "COMPLETOS":
            q_vecinos = self.crearVecinos(qq,self.dim)
        elif self.vecinos_type == "SIMPLES": 
            q_vecinos = self.crearVecinosSimples(qq,self.dim)
        
        q_vecinosValidos = []

        for qv in q_vecinos:
            if self.dentroLimites(qv):
                if not self.esObstaculo(qv):
                    if not self.estaCerrado(qv):
                        q_vecinosValidos.append(qv)
        
        return q_vecinosValidos
        
    def estaCerrado(self,q):
        cerrado = False
        for cerr in self.nodosCerrados:
            if self.sonIguales(q,cerr.q):
                return True
        return cerrado

    def crearVecinos(self,_q,_dim,_d=0):
        if _d < _dim:
            vec = []
            for i in range(_dim-_d):
                vec_izq = _q.copy()
                vec_der = _q.copy()
                if True:#if _q[i+_d] != self.nodoFinal.q[i+_d]:
                    vec_izq[i+_d] = _q[i+_d]-1
                    vec_der[i+_d] = _q[i+_d]+1

                    new_i = self.crearVecinos(vec_izq,_dim,_d+1+i)
                    if new_i != None:
                        vec.extend(new_i)

                    new_d = self.crearVecinos(vec_der,_dim,_d+1+i)
                    if new_d != None:
                        vec.extend(new_d)

                    vec.append(vec_izq)
                    vec.append(vec_der)

                else:
                    pass
            return vec
        return None

    def crearVecinosSimples(self,_q,_dim):
        
        vec = []
        for i in range(_dim):
            vec_izq = _q.copy()
            vec_der = _q.copy()
            if True:#if _q[i] != self.nodoFinal.q[i]:
                vec_izq[i] = _q[i]-1
                vec_der[i] = _q[i]+1

                vec.append(vec_izq)
                vec.append(vec_der)

            else:
                pass

        return vec

    def dentroLimites(self,_q):
        isInLimits = True
        for i in range(self.dim):
            if _q[i] >= self.qLims[i][0] and _q[i] < self.qLims[i][1]:
                pass#isInLimits = True
            else:
                return False
        return isInLimits

    def esObstaculo(self,q):
        esObstaculo = False
        for obs in self.qRest:
            if self.sonIguales(q,obs) and not(self.sonIguales(q,self.nodoFinal.q)):
                return True
            else:
                pass #esObstaculo = False
        return esObstaculo

class Node():

    numNodes = 0

    def __init__(self,_q,_g,_h,_father_id,_obj=None):
        self.id = Node.numNodes
        self.objeto = _obj
        self.q = _q
        self.g = _g
        self.h = _h
        self.f = self.g + self.h

        #self.active = False #True/False

        #self.distance_type = None # "EUCLIDEA" / "MANHATTAN"
        self.father_id = _father_id
        self.sons_ids = []

        Node.numNodes += 1

    def getId(self):
        return self.id
    
    def addSon(self,ID):
        self.sons_ids.append(ID)

    def deleteSon(self,ID):
        return self.sons_ids.pop(self.sons_ids.index(ID))

    def numSons(self):
        return len(self.sons_ids)

    def getFatherId(self):
        return self.father_id

    def deleteAll(self):
        Node.numNodes = 0

    def calculateF(self,_g):
        self.f = _g+self.h
