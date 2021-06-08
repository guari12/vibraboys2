
class grafo_csp():

    def __init__(self,tareas=None,DominioTs=None,maquinas=None,csp=None):
        print("- Creando Grafo CSP")
        if csp==None:
            self.X=[]
            self.D=[]
            self.C={} # entro por id tareaA, luego id tareaB y ahi tengo la extension
            
            self.tareas=tareas
            self.maquinas=maquinas

            print("-- Creando Variables y Dominios")
            for i in range(len(tareas)):

                TSM={"Tarea":self.tareas[i]['id'],'Maquina':None,'PeriodoInicio':None,'PeriodoFin':None}

                dom=[]
                for T in DominioTs:

                    for M in self.maquinas:

                        if M['tipo']==self.tareas[i]['M']:
                            dom.append({'M':M['id'],'S':T})
                
                self.D.append({"Tarea":self.tareas[i]["id"],'Dominio':dom})
                
                self.X.append(TSM)
                if TSM['Tarea']<len(tareas): # la ultima tarea no se incluye, van de a pares de nodos las restricciones
                    self.C.update({TSM['Tarea']:{}})
            self.constraint() # crear las restricciones
        else:
            pass # usar el csp anterior para no empezar de cero
        
        print("---> Grafo creado!!")

    def constraint(self):
        print("--- Creando restricciones")
        C = {"id1":{"id2":[],
                    "id3":[]}}
        for i in self.C: # recorro variables TSMi
            X1 = self.X[i]
            keyA = i
            # diccionario vacio para agregar la sig tarea

            for j in range(i+1,len(self.X)): # para cada TSMi analizo TSMj
                #print(f"Restricciones: {i}-{j}")
                X2 = self.X[j]
                keyB = j
                self.C[keyA].update({keyB:[]})

                restricciones = [] # empiezan vacias las restricciones
                
                if X1["PeriodoInicio"]==None and X1["Maquina"]==None:
                    Dominio1 = self.D[i]["Dominio"]
                    for valor1 in Dominio1:
                        if X2["PeriodoInicio"]==None and X2["Maquina"]==None:
                            Dominio2 = self.D[j]["Dominio"]
                            for valor2 in Dominio2:
                                if valor1["M"]!=valor2["M"]: # usan distintas maquinas
                                    # es valido
                                    restricciones.append((valor1,valor2))
                                else: # ver tiempo
                                    if valor1["S"]+self.tareas[i]["D"]<valor2["S"]:
                                        # agregar, es valido
                                        restricciones.append((valor1,valor2))
                                    elif valor2["S"]+self.tareas[j]["D"]<valor1["S"]:
                                        # agregar, es valido
                                        restricciones.append((valor1,valor2))
                                    # sino, no agregar nada
                        else:
                            valor2= {   "M":X2["Maquina"],
                                        "S":X2["PeriodoInicio"]}
                            restricciones.append((valor1,valor2))
                else:
                    valor1= {   "M":X1["Maquina"],
                                "S":X1["PeriodoInicio"]}
                    if X2["PeriodoInicio"]==None and X2["Maquina"]==None:
                        Dominio2 = self.D[j]["Dominio"]
                        for valor2 in Dominio2:
                                if valor1["M"]!=valor2["M"]: # usan distintas maquinas
                                    # es valido
                                    restricciones.append((valor1,valor2))
                                else: # ver tiempo
                                    if valor1["S"]+self.tareas[i]["D"]<valor2["S"]:
                                        # agregar, es valido
                                        restricciones.append((valor1,valor2))
                                    elif valor2["S"]+self.tareas[j]["D"]<valor1["S"]:
                                        # agregar, es valido
                                        restricciones.append((valor1,valor2))
                                    # sino, no agregar nada
                    else:
                            valor2= {   "M":X2["Maquina"],
                                        "S":X2["PeriodoInicio"]}
                            restricciones.append((valor1,valor2))
                
                self.C[keyA][keyB] = restricciones


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

