
# Funciones vectoriales


def reducir(N,vector,salida="int"):
    V = []
    
    #print("es entero")
    for i in range(len(vector)):
        if salida == "int":
            V.append(int(vector[i]/N))
        elif salida=="float":
            V.append(float(vector[i]/N))
    
    return V

def ampliar(N,vector,salida="int"):
    V = []
    
    #print("es entero")
    for i in range(len(vector)):
        if salida == "int":
            V.append(int(vector[i]*N))
        elif salida=="float":
            V.append(float(vector[i]*N))
    
    return V

def amplificar(N,_camine):
    Camino1 = []
    for c in _camine:
        agre = ampliar(N,c,"int")
        #print(agre)
        Camino1.append( agre )
    return Camino1

def reduccion(red,_camine):
    Camino1 = []
    for c in _camine:
        agre = reducir(red,c,"int")
        Camino1.append( agre )
    return Camino1
