from random import randint
import random

class grafo_csp():
    def __init__(self,tareas,DominioTs,maquinas,cant_tareas):
        self.X=[]
        self.D=[]
        self.C=[]
        
        self.tareas=tareas
        self.maquinas=maquinas

        # (m1,1),(m1,2).......,(m3,1),(m3,2)......

        for i in range(cant_tareas):

            TSM={"Tarea":self.tareas[i]['id'],'Maquina':None,'PeriodoInicio':None,'PeriodoFin':-1}

            dom=[]
            for T in DominioTs:

                for M in self.maquinas:

                    if M['tipo']==self.tareas[i]['M']:
                        dom.append({'M':M['id'],'S':T})
            
            self.D.append({"Tarea":self.tareas[i]["id"],'Dominio':dom})
            
            self.X.append(TSM)
        print("")

    def constraint(self):

        #di={'1':{'2':{'3':[]}}}
        restriccion={"Alcance":[],"Relacion":[]}
        alcance=[]
        #Recorrido de la lista de tareas
        for TS in self.tareas:
            cant_tareas=0
            cant_maquinas=0

            #Conteo de maquinas del tipo requerido por la tarea TS
            for TM in self.maquinas:
                if TS["M"]==TM["tipo"]:
                    cant_maquinas+=1
            
            #Recorrido de la lista de tareas en busca de tareas que requieran la misma maquina
            for TS0 in self.tareas:
                if TS["M"]==TS0["M"]: #En principio cuenta la misma maquina que se selecciono en primer instancia
                    cant_tareas+=1
                    alcance.append(TS0) #El vector de alcance contiene las tareas que implementan la misma maquina
                    restriccion["Alcance"].append(TS0["id"])
                    self.tareas.remove(TS0)

            #A la siguiente funcion le paso la tarea actual y devuelve los ids de las maquinas
            #que hayan disponibles para resolverla
            ids_maq=self.get_idmaq(TS["M"],cant_maquinas)

            #A la siguinte funcion se le pasa la lista de tareas que requieren la misma maquina y retorna
            #una lista con las combinaciones de tiempos en que dichas tareas podrian ejecutarse
            restriccion["Relacion"]=self.set_dominio(alcance,ids_maq,cant_maquinas)
            self.C.append(restriccion)
        return self.C
        
        
    def get_constraints(self):
        return self.C

#funcion que setea el dominio temporal entre tareas
    def set_dominio(self,tareas,ids_maquinas,cant_maquinas):
        #Vector que contendra cada una de las posibles restricciones entre dos variables
        rest={"id_tarea":'',"id_maq":'',"t_inicio":'',"t_fin":''}
        restrictions=[]
        n=len(tareas)
        for x in range(n):
            dominio=self.D
            for k in dominio:
                if (k%tareas[0]["D"])==0:
                    aux=k-tareas[0]["D"]
                    rest["id_tarea"]=tareas[0]["id"]
                    rest["id_maq"]=ids_maquinas[0]
                    rest["t_inicio"]=aux
                    rest["t_fin"]=aux + tareas[0]["D"]
                    restrictions.append(rest)

                    #En este caso tarea 1 contendra un unico valor, y tarea 2 ira tomando cada uno de los 
                    #valores posibles en el dominio restante
                    if len(tareas)==2 and len(tareas)>cant_maquinas:
                        #Se eliminan los valores del dominio ocupados por la tarea 1
                        dominio_aux=self.D
                        for j in range(rest["t_inicio"],rest["t_fin"]):
                            dominio_aux.pop(j)

                        #Se recorre el nuevo dominio en busca de tiempos suficientes para ejecutar la tarea 2
                        for i in dominio_aux:
                            if (i%tareas[1]["D"])==0:
                                aux=i-tareas[1]["D"]
                                rest["id_tarea"]=tareas[1]["id"]
                                rest["id_maq"]=ids_maquinas[1]
                                rest["t_inicio"]=aux
                                rest["t_fin"]=aux + tareas[1]["D"]
                                restrictions.append(rest)

                    #Caso hipotetico de dos tareas que disponen de dos maquinas del mismo tipo
                    elif len(tareas)==2 and len(tareas)==cant_maquinas:
                        for p in dominio:
                            if (p%tareas[1]["D"])==0:
                                aux=p-tareas[1]["D"]
                                rest["id_tarea"]=tareas[1]["id"]
                                rest["id_maq"]=ids_maquinas[1]
                                rest["t_inicio"]=aux
                                rest["t_fin"]=aux + tareas[1]["D"]
                                restrictions.append(rest)
            tareas.reverse()
            ids_maquinas.reverse()
        return restrictions
    

    def get_idmaq(self,maquina,cant_maq):
        ids=[]
        for j in range(cant_maq):
            i=0
            while maquina!=self.maquinas[i]:
                i+=1
            ids.append(self.maquinas[i]["id"])
            self.maquinas.pop(i)
        return ids

    def __str__(self):
        return "Variables:\n%s\nDominio temporal:\n%s\nRestricciones:\n%s\n" % (self.X, self.D,self.C)

