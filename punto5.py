#Implemente un algoritmo de satisfacción de restricciones para resolver un problema de
#scheduling. El problema de scheduling consiste en asignar recursos a tareas. Modele las
#variables, dominio de las mismas, restricciones, etc. Asuma que

#Datos:     .Tares:  -id: identificacion de la tarea
#                    -M: maquinas que pueden utilizar
#                    -T: tiempo que se demora (en minutos)
#           .Maquinas:   -id
#                        -tipo

#Variables:     .TS: tiempo de inicio de una tarea
#               .TM: tipo de maquina utilizable

#Suposiciones: -Cada tarea se realiza con una sola maquina
#              -Cada maquina puede hacer una sola tarea 
#              -Pueden haber 2 o mas maquinas iguales 
#

import random

cant_maquinas=10
cant_tareas=20
max_duracionTarea=20 #min

#Variables
tiposmaquinas=['torno','amoladora','mezcladora','trituradora','alesadora','fresadora','CNC','oxicorte','impresora 3D','soldadora']
maquinas=[{'id':i,'tipo':tiposmaquinas[random.sample(range(len(tiposmaquinas)))]} for i in range(cant_maquinas)]
Tareas=[{'id':i,'M':maquinas[i],'T':random.sample(range(max_duracionTarea))} for i in range(cant_tareas)]

tiempo_max=0
for i in range(cant_tareas):
    
    tiempo_max+=Tareas[i]['T']





# Satisfaccion de restricciones

# Problema: ====================================================

# al inicio hay que definir una lista de tareas
# cada TAREA tiene:
# - Identificacion
# - Duracion
# - Requerimientos de Maquina (Tipo)

# ademas hay que cargar las maquinas que tenemos
# cada MAQUINA tiene:
# - Identificador
# - Tipo

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
