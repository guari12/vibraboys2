
#Variable linguistica theta(angulo): dict={conjuntos borrosos,universo del discurso(Por comprension)}. Suponemos que el rango de los angulos que puede tomar es -45 a 45

theta={'NG':(-60,-20),'NP':(-40,0),'Z':(-20,20),'PP':(0,40),'PG':(20,60)}
dtheta={'NG':(-15,-5),'NP':(-10,0),'Z':(-5,5),'PP':(0,10),'PG':(5,15)}
conjuntos_borrosos=['NG','NP','Z','PP','PG']
F={'NG':(-15,-5),'NP':(-10,0),'Z':(-5,5),'PP':(0,10),'PG':(5,15)}

#FAM: (theta,dtheta,F) Contrareloj Positivo.
FAM=[('NG','NG','PP'),('NG','NP','PP'),('NG','Z','PG'),('NG','PP','PG'),('NG','PG','PG'),
('NP','NG','PP'),('NP','NP','Z'),('NP','Z','PP'),('NP','PP','PG'),('NP','PG','PG'),
('Z','NG','Z'),('Z','NP','Z'),('Z','Z','Z'),('Z','PP','NP'),('Z','PG','NG'),
('PP','NG','NG'),('PP','NP','NP'),('PP','Z','NP'),('PP','PP','Z'),('PP','PG','Z'),
('PG','NG','NG'),('PG','NP','NG'),('PG','Z','NP'),('PG','PP','NG'),('PG','PG','NG')
]

dict_FAM={}
for j in conjuntos_borrosos:
    for i in FAM:
        FAM_C=[]
        if i[3]==j:
            FAM_C.append(i[:2])
    dict_FAM[j]=FAM_C

xtheta_borrosa={}
dxtheta_borrosa={}

def borrosificador(xtheta,xdtheta):

    for i in conjuntos_borrosos:
        xtheta_borrosa[i]=membership(theta[i][0],theta[i][1])
        dxtheta_borrosa[i]=membership(dtheta[i][0],dtheta[i][1])

dict_FAM2={}

def motordeinferencias(xtheta,xdtheta):

    borrosificador(xtheta,xdtheta)

    for j in conjuntos_borrosos:
        list_aux=[]
        for i in dict_FAM[j]:
            aux1=xtheta_borrosa[i[0]]
            aux2=xtheta_borrosa[i[1]]
            list_aux.append(min(aux1,aux2))
        dict_FAM2[j]=list_aux


def membership(a1,a3,X): #Me indica el grado de pertenencia de una variable a un conjunto borroso. Funcion triangular.
    a2=(a3+a1)/2
    if X>a2:
        return 1-(1)/(a3-a2)*X

    if X<a2:
        return 1+(1)/(a2-a1)*X
