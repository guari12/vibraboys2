import numpy as np
import matplotlib.pyplot as plt
from random import randint


# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)

def generar_datos_regresion(cantidad_ejemplos):
    AMPLITUD_ALEATORIEDAD = 0.9

    # Entradas: 2 columnas (x1 y x2)
    x = np.zeros((cantidad_ejemplos, 2))
    # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
    t = np.zeros((cantidad_ejemplos,1))  # 1 columna: la clase correspondiente (t -> "target")

    randomgen = np.random.default_rng()

    # Se generan datos aleatorios siguiendo como valor medio una linea, si se implementa la funcion 
    # liespace. Si se implementa la funcion uniform se obtienen valores completamente aleaotrios
    x1 = np.linspace(0, 5, cantidad_ejemplos) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=cantidad_ejemplos)
    x2 = np.linspace(0, 5, cantidad_ejemplos) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=cantidad_ejemplos)
    #x1 = np.random.uniform(0,5,cantidad_ejemplos)
    #x2 = np.random.uniform(0,5,cantidad_ejemplos)

    # Generamos un rango con los subindices de cada punto generado.
    indices = range(0, cantidad_ejemplos)

    #Creamos la matriz de ejemplos de regresion
    x1.sort()                       #Ordenamos en orden creciente las abcisas
    x[indices] = np.c_[x1, x2]

    # Generamos los vlaores deseados t (target) como una recta que pasa por dos puntos promedio
    # de los valoresgenerados
    sum_y=0
    sum_x=0
    prom = np.zeros((2,2))
    for i in range(cantidad_ejemplos):
            sum_x = sum_x + x[i][0]
            sum_y = sum_y + x[i][1]
            if i==int(cantidad_ejemplos/2):
                prom[0] = np.c_[sum_x/(cantidad_ejemplos/2),sum_y/(cantidad_ejemplos/2)]
                sum_x=0
                sum_y=0
    prom[1] = np.c_[sum_x/(cantidad_ejemplos/2),sum_y/(cantidad_ejemplos/2)]
    m = (prom[1][1] - prom[0][1])/(prom[1][0] - prom[0][0])
    b = prom[0][1] - m*prom[0][0]
    for i in range(cantidad_ejemplos):
        t[i] = m*x1[i] + b

    return x, t


def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):
    randomgen = np.random.default_rng()

    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    # Genera valores aleatorios con distribucion normal estandar (media 0 y desviacion estandar 1)
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))

    w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}


def ejecutar_adelante(x, pesos):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]

    # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
    h = np.maximum(0, z)

    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}


def clasificar(x, pesos):
    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos)
    
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)

    y = resultados_feed_forward["y"]

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return y#[:, 0]

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x_train, t_train, x_test, t_test, x_validation, t_validation, pesos, learning_rate, epochs, detencion_temprana):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x_train, 0)
    
    # Cantidad de epochs a las cuales hay que revisar con el conjunto de validacion
    # para hacer una detencion temprana del entrenamiento si ya no hay mejoras
    N = detencion_temprana
    
    prevAccuracy = None # precision minima de prediccion
    
    for i in range(epochs):
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x_train, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]

        # LOSS --> Calculo de MSE
        # a. Error cuadrático
        L = np.power((t_train - y), 2)

        # b. Promedio de los m errores cuadráticos obtenidos de cada ejemplo. Es un escalar
        loss = (1 / m) * np.sum(L)
        
        # Mostramos solo cada N epochs
        if i % N == 0:
            # Training =======================================

            print()
            print("Training Loss epoch", i, ":", loss)
            

        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dy = y-t_train         
        dL_dy = dL_dy*(2/m)

        dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

        dL_dh = dL_dy.dot(w2.T)
        
        dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
        dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)

        dL_dw1 = x_train.T.dot(dL_dz)                         # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1

        # Aplicamos el ajuste a los pesos
        w1 += -learning_rate * dL_dw1
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        # Actualizamos la estructura de pesos
        # Extraemos los pesos a variables locales
        pesos["w1"] = w1
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2
    
    # Termino el ciclo de entrenamiento
    print()
    print(f" * Termino el entrenamiento en {i} epochs")
    
    
    

def iniciar(numero_clases, numero_ejemplos, graficar_datos):
    # Generamos datos
    x_train, t_train = generar_datos_regresion(round(numero_ejemplos*0.8))
    x_validation, t_validation = generar_datos_regresion(round(numero_ejemplos*0.2))
    x_test, t_test = generar_datos_regresion(round(numero_ejemplos*0.2))

    # Graficamos los datos si es necesario
    if graficar_datos:
        # Parametro: "c": color (un color distinto para cada clase en t)
        plt.scatter(x_train[:, 0], x_train[:, 1])
        plt.scatter(x_train[:, 0], t_train)
        plt.yticks(range(0,5))
        plt.title("Entrenamiento")
        plt.show()
        
        plt.scatter(x_validation[:, 0], x_validation[:, 1])
        plt.scatter(x_validation[:, 0], t_validation)
        plt.yticks(range(0,5))
        plt.title("Validacion")
        plt.show()
        
        plt.scatter(x_test[:, 0], x_test[:, 1])
        plt.scatter(x_test[:, 0], t_test)
        plt.yticks(range(0,5))
        plt.title("Test")
        plt.show()

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    DETENCION_TEMPRANA = 500
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    # Entrena
    LEARNING_RATE=0.5
    EPOCHS=10000
    train(x_train, t_train, x_test, t_test, x_validation, t_validation, pesos, LEARNING_RATE, EPOCHS, DETENCION_TEMPRANA)


iniciar(numero_clases=1, numero_ejemplos=400, graficar_datos=True)