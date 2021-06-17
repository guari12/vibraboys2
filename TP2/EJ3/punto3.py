


def membership(a1,a2,a3,X): #Me indica el grado de pertenencia de una variable a un conjunto borroso. Funcion triangular.

    if X>a2:
        return 1-(1)/(a3-a2)*X

    if X<a2:
        return 1+(1)/(a2-a1)*X
