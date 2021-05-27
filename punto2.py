
import random
import colorama
from colorama import Fore,Style
from A_estrella import A_star,nodos,nodo_inicial

colorama.init() #Libreria que me permite camibar el color de salida del print()

lista_A=[]      #Lista que contiene el mapeo del layout
osbtaculos=[]   #Lista que contiene las direccion de las estanterias dentro de lista_A, que van a ser consideradas como obstaculos por nuestro algoritmo A*

it=0
aa=1

# Se crea el layout asignando un numero a cada estanteria y con '*' a los pasillos
for i in range(16):
    
    for i in range(13):

        lista_aux=[]

        if i%4==0:
            lista_aux.extend( ["*" for j in range(19)])
        else:

            for j in range(19):
                if aa%3==1:
                    lista_aux.append("*")
                
                else:
                    it +=1
                    lista_aux.append(it)
                    osbtaculos.append([i,j])
                aa +=1
        lista_A.append(lista_aux)
        aa=1

#Se elige una estanteria inicial y final al azar
punto_inicial=random.randrange(0,120,1)
punto_final=random.randrange(0,120,1)

#Se busca las coordenadas de estos puntos en el layout
it=0
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
#Se acondicionan los datos para ser mostrados
for i in posicion_int:
    lista_A[i[0]][i[1]]="O"

stirng=""
for q in lista_A:
    for i in q:
        stirng+="{:^5}".format(i)

    stirng+="\n\n"
print(f"El mejor camino entre [{punto_inicial}, {punto_final}] es:\n\n")
print(stirng.replace("O",Fore.RED+ Style.BRIGHT+"O"+Style.RESET_ALL))
