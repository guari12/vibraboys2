#Implemente un algoritmo de satisfacción de restricciones para resolver un problema de
#scheduling. El problema de scheduling consiste en asignar recursos a tareas. Modele las
#variables, dominio de las mismas, restricciones, etc. Asuma que

# Datos:     .Tares:  -id: identificacion de la tarea
#                     -M: maquinas que pueden utilizar
#                     -T: tiempo que se demora (en minutos)
#            .Maquinas:   -id
#                         -tipo

# Variables:     .TS: tiempo de inicio de una tarea
#                .TM: tipo de maquina utilizable

# Suposiciones: -Cada tarea se realiza con una sola maquina
#               -Cada maquina puede hacer una sola tarea 
#               -Pueden haber 2 o mas maquinas iguales 

from random import randint

cant_maquinas=15
cant_tareas=20
max_duracionTarea=20 #min

#Variables
tiposmaquinas=['torno','amoladora','mezcladora','trituradora','alesadora','fresadora','CNC','oxicorte','impresora 3D','soldadora']
maquinas = []
for i in range(cant_maquinas):
    while True:
        maqAleatoria = tiposmaquinas[randint(0,len(tiposmaquinas)-1)]
        contador = 1
        for maquin in maquinas:
            if maquin["tipo"] == maqAleatoria:
                contador+=1
        if contador<=2:
            break
    maquinas.append({'id':i,'tipo':maqAleatoria})
tareas=[{'id':i,"T":f"Tarea_{i}",'M':maquinas[randint(0,len(maquinas)-1)]["tipo"],'D':randint(1,max_duracionTarea)} for i in range(cant_tareas)]

tiempo_max=0
for i in range(cant_tareas):
    tiempo_max+=tareas[i]['D']

# Ya tengo maquinas, tareas y tiempo_max


print("FIN")

# Variables: ====================================================
# TSi: periodo en que se inicia la tarea (num entero de periodos ej horas)
# TMi: lista de maquinas del tipo que se requieran (puede haber mas de una maquina de ese tipo)

# Restricciones: ====================================================
# una restriccion Cr involucra 4 variables (TSi,TMi,TSj,TMj)

# NOTA:
# Hay que definir al incio: variables, dominio y restricciones (ya se dijo antes)
# luego es usar un A* para ir buscando en el arbol,
# solo que cada rama no tiene todas las posibles combinaciones
# sino aquellas que cumplan las restricciones.
