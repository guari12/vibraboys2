import random
import os
from simulated_anneling import anneling, layout, ley_enfriamiento
from A_estrella import A_star,nodos,nodo_inicial

lista_A=[]      #Lista que contiene el mapeo del layout
osbtaculos=[]   #Lista que contiene las direccion de las estanterias dentro de lista_A, que van a ser consideradas como obstaculos por nuestro algoritmo A*

[lista_A,osbtaculos]=layout()
diccionario = {}

#La siguiente funcion agrega la lista de nodos necesarios para ir de una estanteria a otra en una 
#variable del tipo diccionario cuya clave de acceso a cada camino sera 'ESTANTERIA1/ESTANTERIA2'
def dictionary_way(punto_inicial,punto_final,iteracion):

    #Se busca las coordenadas de estos puntos en el layout
    it=0
    aux1=[0,0]
    aux2=[0,0]
    for q in lista_A:
        if punto_inicial in q:
            a=q.index(punto_inicial)
            aux1=[it,a]
        if punto_final in q:
            a=q.index(punto_final)
            aux2=[it,a]
        it +=1

    #Se realiza la busqueda con el algoritmo A*
    posicion=A_star(aux1,aux2,2,1,osbtaculos)
    posicion_int=posicion.buscar_camino(camino_total=True)
    
    diccionario[str(punto_inicial)+'/'+str(punto_final)] = posicion_int
    return diccionario

#La siguiente función genera un archivo .txt  que almacena todos los caminos mas cortos entre dos 
#estanterias implementando el algoritmo a estrella.
def crear_cache():
    flag=1
    iter=0
    while(flag==1):
        #Se elige una estanteria inicial y final al azar
        punto_inicial=random.randrange(0,100,1)
        punto_final=random.randrange(0,100,1)

        #Si la clave ya fue almacenada en el diccionario incementa el iterador
        if str(punto_inicial)+'/'+str(punto_final) in diccionario:
            iter=iter+1
        else:
            dic=dictionary_way(punto_inicial,punto_final)
            iter=0

        #Si se repite 3 veces seguidas el mismo nombre, damos por hecho que se resolvieron todas las 
        #posibles combinaciones de estanterias, y se sale del bucle
        if(iter==3):
            flag=0
            
    #se crea el archivo cache y se almacena el diccionario
    archivo = open('Ast_cache.txt', 'a')
    archivo.write(str(dic))
    archivo.close()

def cache():
    if os.path.exists('Ast_cache.txt'):
        x=int(input("Ya existe una memoria cache. Desea generar otra?\n1-Si\n2-No\n"))
        if(x==1):
            os.remove('Ast_cache.txt')
            crear_cache()
    else:
        crear_cache()

#La siguiente función se implementa para leer el archivo '.txt' y retornar la lista de nodos
# que se recorren para ir de una estanteria a otra
# clave de acceso al camino: 'ESTANTERIA1/ESTANTERIA2'
def read_cache(clave):
    with open('Ast_cache.txt', 'r') as dict_file:
        dict_text = dict_file.read()
        diccionario=eval(dict_text)
        return diccionario[str(clave)]

cache()
print("Orden 38/30\n",read_cache('38/30'))