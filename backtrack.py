
def backtrack(csp,assigment,cant_tareas):

    if iscomplete(assigment,cant_tareas):
        return assigment

    var=select_unassignedvariable(csp)
    assigment['variable'].append(var)
    valuelist=order_domain_values(var,csp)

    for value in valuelist:

        if isconsistent(value,csp,assigment):
            bool_inference,var_inference=inference(csp,var,value)
            if bool_inference:
                assigment['values'].append(value)
                assigment['inferences'].append(var_inference)
                bool_result,result=backtrack(csp,assigment)
                if bool_result:
                    return result
                assigment['values'].pop(-1)
                csp.D=assigment['inferences'].pop(-1)

    return False


def iscomplete(assigment,cant_tareas):

    if len(assigment['variables'])==cant_tareas:

        return True

    return False

#Heuristicas globales
def select_unassignedvariable(csp):

    #En primer lugar elegimos la heuristica MRV
    aux=10e4

    for dom in csp.D:

        if len(dom['Dominio'])<aux:

            aux=len(dom['Dominio'])
            variableMRV=dom['id']

        if dom == aux:

            variableMRV.extend(dom['id'])

    #Si hay mas de dos variables MRV se desempata de acuerdo a la Variable más restrictiva
    if len(variableMRV):

        cant_rest=[]
        for var in variableMRV:

            cant_rest.append(len(csp.C[str(var)]))

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

        for k in csp.C[str(var)].key():
                
            aux2+=len(csp.C[str(var)][k][str(x)] )

        if aux2>aux1:
            aux1=aux2
            u.append(x)
        else:
            aux3.append(x)

    u.reverse()
    u.extend(aux3)

    return u

def isconsistent(value,csp,assigment):
    
    if value in csp.D[assigment['variable'][-1]]["Dominio"]:

        return True

    return False

def inference(csp,var,value):


    pass
