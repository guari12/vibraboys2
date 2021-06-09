from ac3 import ac3

def backtrack(csp,assigment,cant_tareas):

    if iscomplete(assigment,csp):
        return assigment

    var=select_unassignedvariable(csp)
    assigment['variables'].append(var)
    valuelist=order_domain_values(var,csp)

    for value in valuelist:
        
        if isconsistent(value,csp,assigment):
            assigment['values'].append(value)
            bool_inference=inference(csp,assigment)

            if bool_inference:

                result=backtrack(csp,assigment,cant_tareas)

                if result!=None:
                
                    return result

            assigment['values'].pop(-1)
            auxX=assigment['inferences']['X'].pop(-1)
            auxD=assigment['inferences']['Dominio'].pop(-1)
            csp.X=auxX
            csp.D=auxD
    assigment['variables'].pop(-1)
    return None


def iscomplete(assigment,csp):

    if len(assigment['variables'])==len(csp.C.keys()):

        return True

    return False

#Heuristicas globales
def select_unassignedvariable(csp):

    #En primer lugar elegimos la heuristica MRV
    aux=10e4
    variableMRV=[]
    aux2=0
    for dom in csp.D:

        if dom['Tarea'] in csp.C.keys():
            if len(dom['Dominio'])>1:
                if len(dom['Dominio'])<aux:

                    aux=len(dom['Dominio'])
                    aux2=dom['Tarea']

    variableMRV.append(aux2)

    for dom in csp.D:
        if dom['Tarea'] in csp.C.keys():
            if len(dom['Dominio'])>1:
                if dom['Tarea']!=aux2:
                    if len(dom['Dominio'])==aux:
                        variableMRV.append(dom['Tarea'])
        
    #Si hay mas de dos variables MRV se desempata de acuerdo a la Variable más restrictiva
    if len(variableMRV)>0:

        cant_rest=[]
        for var in variableMRV:
            if var in csp.C.keys():
                cant_rest.append(len(csp.C[var]))

        if len(cant_rest)>0:
            ind=cant_rest.index(max(cant_rest))
            return variableMRV[ind]

    return variableMRV[0]


def order_domain_values(var,csp):

    aux=csp.D[var]['Dominio']

    aux1=0
    aux3=[]
    u=[]

    for x in aux:

        aux2=0

        for k in csp.C[var].keys():
                
            aux2+=len(csp.C[var][k][str(x)] )

        if aux2>aux1:
            aux1=aux2
            u.append(x)
        else:
            aux3.append(x)

    u.reverse()
    u.extend(aux3)

    return u

def isconsistent(value,csp,assigment):
    
    if value in csp.D[assigment['variables'][-1]]['Dominio']:

        return True

    return False

def inference(csp,assigment):
    
    aux1=[]
    aux2=[]
    aux1.extend(csp.X)
    aux2.extend(csp.D)
    assigment['inferences']['X'].append(aux1.copy())
    assigment['inferences']['Dominio'].append(aux2.copy())
    csp.X[assigment['variables'][-1]]['PeriodoInicio']=assigment['values'][-1]['S']
    csp.X[assigment['variables'][-1]]['Maquina']=assigment['values'][-1]['M']
    csp.X[assigment['variables'][-1]]['PeriodoFin']=assigment['values'][-1]['S']+csp.X[assigment['variables'][-1]]['D']
    csp.D[assigment['variables'][-1]]['Dominio']=[assigment['values'][-1]]
    return ac3(csp)
    
