# Los algoritmos necesitan de estas librerías
from random import choice
from time import time

################################################
############ ALGORITMO MIXALB-1 ##################
################################################


def crear_lista_nro_predecesores(precedencia):
    """
    Genera una lista con todas las tareas y el número de predecesores que posee cada una de ellas

    Parámetros:
    - precedencia (Lista de Listas de Numeros):  lista de tareas de precedencias

    Retorna:
    - nro_predecesores (Lista de Listas de Numeros): lista en que sigue el siguiente formato [[Índice tarea, Nro. de predecesores]...]
    """

    # Compara todas las tareas y elige la que posea el menor tiempo de procesamiento (mira los tiempos de cada tarea para todos los productos)
    tareas_sin_checkear = list(range(len(precedencia)))
    predecesores = [[] for i in precedencia]

    # Definir una sub-funcion que va a ser de utilidad en otra parte de esta funcion
    def agregar_predecesores(tarea, tarea_madre, predecesores, precedencia):
        """
        Genera una lista de predecesores indirectos de una dada tarea

        Parámetros:
        - tarea (Nro): es el índice de la tarea sobre la cual se están checkeando los predecesores directos
        - tarea_madre (Nro): es el índice de la tarea sobre la cual se están checkeando los predecesores indirectos
        - precedesores (Lista de Lista de Números): lista de predecesores que posee la tarea madre
        - precedencia (Lista de Listas de Números): lista de tareas de precedencias

        Retorna:
        - predecesores (Lista de Lista de Números): lista actualizada de predecesores de la tarea madre

        """

        # Por cada predecesor de la tarea
        for predecesor in precedencia[tarea]:

            # Si el predecesor no está en la lista de predecesores de tareas
            if predecesor not in predecesores[tarea_madre]:

                # Lo agrego a la lista de predecesoresd de la tarea madre
                predecesores[tarea_madre].append(predecesor)

                # Reviso los predecesores del predecesor
                # Notar que es una función recursiva, es decir, se llama a sí misma, y como parámetro 'tarea' utiliza 'predecesor'
                agregar_predecesores(
                    predecesor, tarea_madre, predecesores, precedencia)

        # Cuando terminó de revisar todos los predecesores retorna la lista de predecesores
        return predecesores

    for tarea in tareas_sin_checkear:

        # Agrega los predecesores indirectos de la tarea
        predecesores = agregar_predecesores(
            tarea, tarea, predecesores, precedencia)

    # Mira la cantidad de predecesores indirectos que posee cada tarea y genera una lista
    # con formato: [(Índice de tarea, Nro. predecesores de tarea)...]
    nro_predecesores = list(enumerate([len(tareas)
                                       for tareas in predecesores]))

    # Retorna la lista de nro de sucesores.
    return nro_predecesores


def crear_lista_nro_sucesores(precedencia):
    """
    Genera una lista con todas las tareas y el número de sucesores que posee cada una de ellas

    Parámetros:
    - precedencia (Lista de Listas de Números):  lista de tareas de precedencias

    Retorna:
    - nro_sucesores (Lista de Listas de Números): lista en que sigue el siguiente formato [(Índice de tarea, Nro. sucesores de tarea)...]
    """

    # Inicializar variable sucesores con una lista de listas vacías
    # sucesores[i] = Índices de tareas que son sucesoras directas de la tarea i
    sucesores = [[] for i in precedencia]

    # Creo lista de sucesores (Invirtiendo lista de precedencia)
    # La variable j indicará el índice de la tarea i
    j = 0
    # Por cada tarea
    for i in precedencia:

        # Por cada predecesor de la tarea
        for predecesor in i:

            # Agrega a la lista de sucesores del predecesor el índice de la tarea i
            sucesores[predecesor].append(j)
        j += 1

    # Uso la lista de sucesores en la función que crea lista de número de predecesores.
    # Por la forma en que trabaja la función, esto dará como resultado una lista con número de sucesores
    nro_sucesores = crear_lista_nro_predecesores(sucesores)
    return nro_sucesores


def filtrar_tareas_factibles(tareas_no_asignadas, precedencia, tiempos, tiempo_disponible_et):
    """
    Genera una lista de tareas que pueden ingresar a una ET cumpliendo restricciones de precedencia y tiempo de ciclo.

    Parámetros:
    - tareas no asignadas (Lista de números):  lista de índices de tareas que se quiere ingresar a una ET
    - tiempo disponible el (Número entero):  tiempo disponible para procesar tareas en la ET
    - precedencia (Lista de listas de números):  lista de precedencia, dada la tarea i, precedencia[i] es la lista de tareas que esta requiere para poder realizarse

    Retorna:
    - tareas factibles (Lista de números): Lista de índices de las tareas factibles filtradas por esta función
    """
    # Genera rango de índices de productos. En este caso como hay 2 se generará el rango (0,1)
    productos = range(len(tiempos[0]))

    # Inicializa lista de tareas factibles
    tareas_factibles = []

    # Realiza un loop en todas las tareas no asignadas
    for tarea in tareas_no_asignadas:

        # Setea variable que mira si se cumplió la precedencia en falso
        no_cumple_por_precedencia = False
        no_cumple_por_tiempo = False

        # Chequea si la tarea es factible por precedencias
        # Realiza un loop por cada predecesor de la misma
        for predecesor in precedencia[tarea]:

            # Si hay un predecesor de la tarea que no fue asignada aun a una ET entonces no será factible por precedencia
            if predecesor in tareas_no_asignadas:
                no_cumple_por_precedencia = True
                break

        # Si no fue factible por precedencia se continuará a la siguiente tarea en la lista de no asignadas y no se la agrega a la lista de tareas factibles
        if no_cumple_por_precedencia:
            continue

        # Chequea si es factible por tiempo disponible por cada uno de los productos
        # Si no es factible por tiempo disponible en al menos uno de los productos se continuará a la siguiente tarea
        for p in productos:
            if tiempos[tarea][p] > tiempo_disponible_et[p]:
                no_cumple_por_tiempo = True
                break

        # Si no fue factible por tiempo disponible se continuará a la siguiente tarea en la lista de no asignadas y no se la agrega a la lista de tareas factibles
        if no_cumple_por_tiempo:
            continue

        # Este código se ejecuta si fue factible tanto por precedencia como por tiempo disponible
        # Agrega a la lista de tareas factibles la tarea y continúa con la siguiente tarea en la lista de no asignadas
        tareas_factibles.append(tarea)
        continue

    # Cuando reviso toda la lista de tareas no asignadas retorna la lista de tareas factibles obtenida
    return tareas_factibles


def asignar_t_a_et(tareas_factibles, metodo, tiempos, nro_predecesores=None, nro_sucesores=None):
    """
    Dada una lista de tareas factibles y un método, selecciona una tarea para que ingrese a una ET

    Parámetros:
    - tareas factibles (Lista de números): es la lista de tareas factibles a ingresar en una ET
    - metodo (String): posibilita la selección de un método para elegir la tarea que ingresara a la estación del trabajo
     - Metodos disponibles: "tarea mas larga" - "tarea más corta" - "kilbridge y webster" - "bedworth - "aleatorio"
    - tiempos (Lista de números): es la lista ordenada de los tiempos de las tareas por ET.

    (Opcionales)
    - nro_predecesores (Lista de lista de numeros): es la lista con número de predecesores de cada tarea.
    - nro_sucesores (Lista de lista de numeros): es la lista con número de sucesores de cada tarea.

    Retorna:
    - tarea_elegida (Número): El índice de la tarea seleccionada ingresar a una ET por la función
    """

    # Genera rango de índices de productos. En este caso como hay 2 se generará el rango (0,1)
    productos = range(len(tiempos[0]))

    # Inicializa variable de tarea elegida
    tarea_elegida = None

    # Si el metodo elegido es "tarea mas larga"
    if metodo == "tarea mas larga":
        # Compara todas las tareas y elige la que posea el mayor tiempo de procesamiento (mira los tiempos de cada tarea para todos los productos)
        tiempo_maximo = 0
        for tarea in tareas_factibles:
            for p in productos:
                if tiempo_maximo < tiempos[tarea][p]:
                    tiempo_maximo = tiempos[tarea][p]
                    tarea_elegida = tarea

    # Si el método elegido es "tarea mas corta"
    if metodo == "tarea mas corta":

        # Compara todas las tareas y elige la que posea el menor tiempo de procesamiento (mira los tiempos de cada tarea para todos los productos)
        tiempo_minimo = max(max(tiempo) for tiempo in tiempos)
        for tarea in tareas_factibles:
            for p in productos:
                if tiempo_minimo >= tiempos[tarea][p]:
                    tiempo_minimo = tiempos[tarea][p]
                    tarea_elegida = tarea

    # Si el metodo es Kilbridge y Webster
    if metodo == "kilbridge y webster":

        # Si no se proveyó el número de predecesores tirar error
        if nro_predecesores == None:
            raise TypeError(
                "Si elegiste el metodo Kilbridge y Webster, poner como argumento la lista de numero de predecesores de las tareas")

        # Elijo tarea con más predecesores dentro de las factibles que tengo
        tareas_posibles = []

        # Creó la lista con número de predecesores factible
        nro_predecesores_factibles = [
            nro_predecesores[tarea] for tarea in tareas_factibles]

        # La ordeno por número de predecesores de forma descendente
        nro_predecesores_factibles.sort(key=lambda x: x[1], reverse=True)

        # Elijo la tarea con más predecesores
        tarea_elegida = nro_predecesores_factibles[0][0]

    # Si el metodo es Bedworth
    if metodo == "bedworth":

        # Si no se provee el número de sucesores tirar error
        if nro_sucesores == None:
            raise TypeError(
                "Si elegiste el metodo Bedworth, poner como argumento la lista de número de sucesores de las tareas")

        # Elijo tarea con más sucesores dentro de las factibles que tengo
        tareas_posibles = []

        # Creo la lista con número de sucesores factible
        nro_sucesores_factibles = [
            nro_sucesores[tarea] for tarea in tareas_factibles]

        # La ordeno por número de sucesores de forma descendente
        nro_sucesores_factibles.sort(key=lambda x: x[1], reverse=True)

        # Elijo la tarea con más sucesores
        tarea_elegida = nro_sucesores_factibles[0][0]

    # Si el método elegido es "aleatorio"
    if metodo == "aleatorio":
        # Elige aleatoriamente una tarea
        tarea_elegida = choice(tareas_factibles)

    # Retorna la tarea seleccionada
    return tarea_elegida


def MIXALB1(metodo, tc_objetivo, tiempos, precedencia, nro_predecesores=None,  nro_sucesores=None):
    """
    Función que conceptualiza el método de resolución de balanceo de líneas MIXALB-1 (Múltiples productos mixtos).
    Buscará encontrar el número mínimo de ETs sin superar el TC objetivo.

    Parámetros:
    - metodo (String): posibilita la selección de un método para elegir la tarea que ingresara a la estación del trabajo
        - Métodos disponibles: "tarea mas larga" - "tarea más corta" - "aleatorio"
    - tc_objetivo (Número): es el TC objetivo que utilizará el algoritmo y no superará.
    - tiempos (Lista de números): es la lista ordenada de los tiempos de las tareas.
    - precedencia (Lista de listas de números):  lista de precedencia, dada la tarea i, precedencia[i] es la lista de tareas que esta requiere para poder realizarse

    Retorna:
        - et (Número): Número de ETs que se obtuvieron al realizar el algoritmo
        - tarea_estacion (Lista de lista de números): Lista en la que cada elemento corresponde a una ET y contiene otra lista que posee los índices de las tareas asignadas a esa estación
        - te (Lista de Números): Tiempos de las estaciones obtenidos
        - tc (Número): Tiempo de ciclo real de la distribución de tareas obtenida por el algoritmo
        - ef (Lista de Números): Eficiencia de la línea por producto teniendo en cuenta que solo posee un producto en todas las estaciones
    """

    # Genera rango de índices de tareas.
    # La lista comienza en 0, por lo que la primera tarea tendrá índice 0
    tareas = range(len(tiempos))

    # Genera rango de índices de productos. En este caso como hay 2 se generará el rango (0,1)
    productos = range(len(tiempos[0]))

    # Inicializa variable de Estación de trabajo
    et = 0

    # Inicializa variable de Tarea asignada a ET.
    # tarea_estacion[estacion]: lista de índices de estaciones asignadas a esa et. Ej: [0,3,2,9,27]
    tarea_estacion = [[]]

    # Crea lista de tareas no asignadas
    tareas_no_asignadas = list(tareas)

    # Tiempo de estación respecto a cada producto
    # tiempo_ets[k][j] = tiempo utilizado en la estación k respecto al producto j
    tiempo_ets = [[[] for p in productos]]

    # Tiempo disponible en estación respecto a cada producto
    # tiempo_ets[j] = tiempo disponible en la estación respecto al producto j
    tiempo_disponible_et = [[] for p in productos]

    # Mientras haya tareas sin asignar continua el loop
    while len(tareas_no_asignadas):

        # Calcula variables de tiempos de las estaciones
        for p in productos:
            tiempo_ets[et][p] = sum([tiempos[i][p]
                                     for i in tarea_estacion[et]])
            tiempo_disponible_et[p] = tc_objetivo - tiempo_ets[et][p]

        # Se filtran todas las tareas factibles a ingresar en la ET, por precedencia y por tiempo disponible en la ET
        tareas_factibles = filtrar_tareas_factibles(
            tareas_no_asignadas, precedencia, tiempos, tiempo_disponible_et)

        # Si no hay tareas factibles se agrega otra ET
        if tareas_factibles == []:
            et += 1
            tarea_estacion.append([])
            tiempo_ets.append([[] for p in productos])
            continue

        # Se selecciona la tarea
        tarea_elegida = asignar_t_a_et(
            tareas_factibles, metodo, tiempos, nro_predecesores, nro_sucesores)

        # Se agrega la tarea elegida a la ET
        tarea_estacion[et].append(tarea_elegida)

        # Se remove la tarea elegida de la lista de no asignadas.
        tareas_no_asignadas.remove(tarea_elegida)

        # Continua con el loop
        continue

    # Una vez terminado el loop (todas las tareas asignadas a ETs)
    # Calcula el tiempo de ciclo real (el cual puede ser un menor al objetivo)
    te = [[sum([tiempos[i][p] for i in tarea_estacion[estacion]])
           for estacion in range(et+1)] for p in productos]

    # Calcula el tiempo de ciclo por cada ET
    tc = [max(p) for p in te]

    # Calcula la eficiencia de la línea por producto teniendo en cuenta que solo posee un producto en todas las estaciones
    ef = [(sum([tiempo[p]
                for tiempo in tiempos])/(tc[p]*(et+1)))*100 for p in productos]

    # Retorna las variables
    return et+1, tarea_estacion, te, tc, ef

################################################
############ ALGORITMO MIXALB-2 ##################
################################################


def MIXALB2(metodo, et_objetivo, tiempos, precedencia, nro_predecesores=None, nro_sucesores=None, aumento_tc=1):
    """
    Función que conceptualiza el metodo de resolución de balanceo de líneas MIXALB-2 (Múltiples productos mixtos).
    Dado un número de ET, distribuye las tareas en las ETs de manera que se minimice el tiempo de ciclo.

    Entrada:
    - metodo (String): posibilita la selección de un metodo para elegir la tarea que ingresara a la estacion del trabajo
        - Metodos disponibles: "tarea mas larga" - "tarea mas corta"
    - et_objetivo (Número): número de ETs que utilizará el algoritmo
    - tiempos (Lista de números): es la lista ordenada de los tiempos de las tareas.
    - precedencia (Lista de listas de números):  lista de precedencia, dada la tarea i, precedencia[i] es la lista de tareas que esta requiere para poder realizarse
    - aumento_tc (Numero): Esta variable es opcional, sirve para fijar un porcentaje (por default 1 que refiere a 1%) que es la cantidad que aumentará el TC por cada iteración

    Salida:
    - mejor_solucion (Lista): Una lista con:
        - tarea_estacion (Lista de lista de números): Lista en la que cada elemento corresponde a una ET y contiene otra lista que posee los indices de las tareas asignadas a esa estación
        - te (Lista de Números): Tiempos de las estaciones obtenidos
        - tc (Número): Tiempo de ciclo real de la distribución de tareas obtenida por el algoritmo
        - ef (Lista de Números): Eficiencia de la línea por producto teniendo en cuenta que solo posee un producto en todas las estaciones
    - iteraciones (Número): número de iteraciones realizadas por el metodo
    """

    # Genera rango de índices de tareas.
    # La lista comienza en 0, por lo que la primera tarea tendrá indice 0.
    tareas = range(len(tiempos))

    # Genera rango de índices de productos. En este caso como hay 2 se generará el rango (0,1)
    productos = range(len(tiempos[0]))

    # Para calcular el mejor TC obtenible se necesita calcular dos constantes el máximo tiempo de las tareas y el mínimo tc posible
    # Calcula el tiempo máximo de tareas (sin importar producto)
    tiempo_maximo = max([max(t) for t in tiempos])

    # Calcula mínimo tc posible
    max_suma_tiempos = max([sum([tiempo[p]
                                 for tiempo in tiempos]) for p in productos])

    # Inicializa la variable tc objetivo. El mejor TC obtenible es el máximo entre: tiempo máximo de las tareas y la suma de todos los tiempos sobre la cantidad de ET.
    tc_objetivo = max(max_suma_tiempos / et_objetivo, tiempo_maximo)

    # Inicializa variable de iteraciones
    i = 0

    # Inicializa la mejor solución.
    mejor_solucion = []

    # Inicializa un loop que hay que cortar manualmente
    while True:

        # Ejecutar algoritmo MIXALB-1 y obtiene los resultados
        (et, tarea_estacion, te, tc, ef) = MIXALB1(
            metodo, tc_objetivo, tiempos, precedencia, nro_predecesores, nro_sucesores)

        # Si el número de ET es el buscado
        if (et == et_objetivo):
            mejor_solucion = (tarea_estacion, te, tc, ef)

            # Rompo el loop
            break

        # Si no lo es
        else:
            # Aumentar un 1% el tc anterior
            tc_objetivo = tc_objetivo * (1 + aumento_tc/100)

        # Aumentar el número de iteraciones
        i += 1

    # Retorno la solución y numero de iteraciones
    return mejor_solucion, i

####################################################
##################### MIX-COMSOAL-2 ################
####################################################


def MIXCOMSOAL2(et_objetivo, tiempos, precedencia, iteraciones, iteraciones_sin_aumentar_tc_objetivo=None, aumento_tc=1):
    """
    Algoritmo de balanceo de líneas de tipo SALB-2 basado en aleatoriedad y fuerza bruta.
    Dado un número de ET, distribuye las tareas en las ETs de manera que se minimice el tiempo de ciclo.

    Entrada:
    - et_objetivo (Número): número de ETs fijado que utilizará el algoritmo
    - tiempos (Lista de números): es la lista ordenada de los tiempos de las tareas.
    - precedencia (Lista de listas de números):  lista de precedencia, dada la tarea i, precedencia[i] es la lista de tareas que esta requiere para poder realizarse
    - iteraciones (Número): Esta variable es opcional, define el límite de iteraciones que realiza este algoritmo, se recomienda un número grande, por defecto está fijada en 100.000 iteraciones
    - iteraciones_sin_aumentar_tc_objetivo (Numero): Esta variable es opcional, define el límite de iteraciones que el algoritmo realiza manteniendo el TC, por defecto está fijada en 1.000 iteraciones.
    - aumento_tc (Numero): Esta variable es opcional, sirve para fijar un porcentaje (por default 1 que refiere a 1%) que es la cantidad que aumentará el TC por cada "iteraciones_sin_aumentar_tc_objetivo" iteraciones

    Salida:
    - (Lista) con:
        - (Lista de lista de números) Lista en la que cada elemento corresponde a una ET, cada elemento es otra lista que contiene los indices de las tareas asignadas a esa estación
        - (Número) Tiempo de ciclo real de la distribución de tareas obtenida por el algoritmo
    - (Número) número de iteraciones realizadas por el método
    """

    # Genera rango de índices de tareas.
    # La lista comienza en 0, por lo que la primera tarea tendrá índice 0.
    tareas = range(len(tiempos))

    # Genera rango de índices de productos. En este caso como hay 2 se generará el rango (0,1)
    productos = range(len(tiempos[0]))

    # Para calcular el mejor TC obtenible se necesita calcular dos constantes el máximo tiempo de las tareas y el mínimo tc posible
    # Calcula el tiempo máximo de tareas (sin importar producto)
    tiempo_maximo = max([max(t) for t in tiempos])

    # Calcula mínimo tc posible
    max_suma_tiempos = max([sum([tiempo[p]
                                 for tiempo in tiempos]) for p in productos])

    # Inicializa la variable tc_objetivo. El mejor TC obtenible es el máximo entre: tiempo máximo de las tareas y la suma de todos los tiempos sobre la cantidad de ET.
    tc_objetivo = max(max_suma_tiempos / et_objetivo, tiempo_maximo)

    # Inicializa variables de iteraciones
    i = 0

    # Inicializa variable de iteraciones sin aumentar TC
    iteraciones_sin_aumentar_tc = 0

    # Inicializa variable de mejor solucion
    mejor_solucion = []

    # Mientras no se superen las iteraciones ingresadas
    while i <= iteraciones:

        # Ejecutar algoritmo SALB-1 con metodo "aleatorio"
        (et, tarea_estacion, te, tc, ef) = MIXALB1(
            "aleatorio", tc_objetivo, tiempos, precedencia)

        # Encuentro mejor solucion
        if et_objetivo == et:
            # Actualizo mejor solucion
            mejor_solucion = (tarea_estacion, te, tc, ef)

            # Rompo el loop
            break

        # Si se alcanza el número de iteraciones sin aumentar tc objetivo
        if iteraciones_sin_aumentar_tc >= iteraciones_sin_aumentar_tc_objetivo:
            # Aumentar un 1% el TC anterior
            tc_objetivo = tc_objetivo * (1 + aumento_tc/100)

            # Reiniciar el número de iteraciones sin aumentar tc
            iteraciones_sin_aumentar_tc = 0

        # Aumentar ambos números de iteraciones en 1
        i += 1
        iteraciones_sin_aumentar_tc += 1

    # Retorno mejor solucion
    return mejor_solucion, i

################################################
################## DATOS #######################
################################################

# A continuación se cargarán los datos específicos del problema de balanceo


# Lista con los tiempos de cada tarea por cada producto
# TIEMPOS[i][j] = Es el tiempo que tarda el producto j en realizar la tarea i
# Notar que el primer índice de una lista en lenguaje Python es el número 0. Por lo que la primer tarea y producto será considerada la tarea/producto 0
TIEMPOS = [(61.4, 61.4, 61.4, 70.6, 70.6), (80.1, 80.1, 80.1, 91.8, 91.8), (14.6, 14.6, 14.6, 19.8, 19.8), (29.3, 29.3, 29.3, 37.3, 37.3), (47, 47, 47, 55.8, 55.8), (36.6, 36.6, 36.6, 48.4, 48.4), (5.8, 5.8, 5.8, 5.8, 5.8), (118.9, 118.9, 118.9, 118.9, 118.9), (43.1, 43.1, 43.1,
                                                                                                                                                                                                                                                                      50.1, 50.1), (41.5, 41.5, 41.5, 41.5, 41.5), (27.8, 27.8, 27.8, 34.2, 34.2), (5.4, 5.4, 5.4, 5.4, 5.4), (27.9, 27.9, 27.9, 42, 42), (40.7, 40.7, 40.7, 45, 45), (50.4, 50.4, 50.4, 79.8, 79.8), (36.3, 36.3, 36.3, 0, 0), (29.9, 0, 0, 29.9, 29.9), (0, 59.6, 59.6, 59.6, 59.6), ]

# Lista de precedencia conjunta
# PRECEDENCIA[i] = Es la lista de predecesores de la tarea i.
# NOTA: Dado que en capítulos anteriores se refiere a la primera tarea como tarea 1 y Python toma como primer elemento el elemento 0, en esta lista se tuvo que reducir en 1 cada uno de los índices de las tareas
PRECEDENCIA = [[], [1], [2], [3], [2], [4, 5], [6], [7], [8], [11], [
    9], [11], [12], [16, 17, 18], [14], [10, 13], [9], [9], ]

# Si no los reduje podría usar esto para que los reduzca
PRECEDENCIA = [[j-1 for j in i] for i in PRECEDENCIA]

# Operarios necesarios x tarea
OPERARIOS_TAREA = [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

# Se ha cambiado el índice de las tareas ya que se eliminaron todas las tareas de apoyo en esta resolución. Para presentar la solución se convertiran a los numeros tareas.
# Equivalencia nueva numeración. EQUIVALENCIA_INDICE[IndiceDeTarea] = Indice de tarea original.
EQUIVALENCIA_INDICE = [11, 12, 13, 14, 15, 16, 17,
                       18, 19, 20, 21, 22, 23, 24, 25, 26, 30, 31, ]

# Número de estaciones de trabajo (ETs) objetivo
ET_OBJETIVO = 5

################################################
############ DATOS CALCULADOS ##################
################################################

# Los siguientes datos seran calculados automaticamente una vez y usados en los algoritmos

# Creo una lista con el numero de predecesores de cada tarea
# La lista esta ordenado de mayor numero a menor numero
NRO_PREDECESORES = crear_lista_nro_predecesores(PRECEDENCIA)

# Creo una lista con el numero de sucesores de cada tarea
# La lista esta ordenada de mayor numero a menor numero
NRO_SUCESORES = crear_lista_nro_sucesores(PRECEDENCIA)

####################################################
##################### REPORTES #####################
####################################################


def reportar_solucion(titulo, algoritmo, *arguments):
    """
    Funcion que sirve para correr los algoritmos, calcular el tiempo de ejecucion y reportar la solucion de manera mas ordenada

    Entrada:
    - titulo (String): El título del algoritmo a correr
    - algoritmo (Funcion): Es la funcion que referencia al algoritmo a correr
    - *arguments: Son los argumentos que tomara la funcion del algoritmo, se colocan como argumentos adicionales y deben estar en el orden en el que el algoritmo los requiera

    """

    tiempo_procesamiento = time()
    mejor_solucion, i = algoritmo(*arguments)
    tiempo_procesamiento = time() - tiempo_procesamiento

    operarios_et = [max([OPERARIOS_TAREA[tarea] for tarea in et])
                    for et in mejor_solucion[0]]

    print("Algoritmo finalizado - ", titulo)
    print("Resultados obtenidos en ", i, " iteraciones")
    print("Resultados obtenidos en ", tiempo_procesamiento*1000, "milisegundos")
    print("TE: ", mejor_solucion[1])
    print("TC: ", mejor_solucion[2])
    print("EF: ", mejor_solucion[3])
    print("Asignación de tareas a ET: ", [
          [EQUIVALENCIA_INDICE[indice] for indice in et] for et in mejor_solucion[0]])
    print("Operarios x ET: ", operarios_et)
    print("\n\n")


# Ejecuto algoritmo MIXALB-2 con método: "tarea mas larga"
reportar_solucion("MIXALB2 - Tarea más larga", MIXALB2, "tarea mas larga", ET_OBJETIVO,
                  TIEMPOS, PRECEDENCIA, NRO_PREDECESORES, NRO_SUCESORES)

# Ejecuto algoritmo MIXALB-2 con método: "tarea mas corta"
reportar_solucion("MIXALB2 - Tarea más corta", MIXALB2, "tarea mas corta", ET_OBJETIVO,
                  TIEMPOS, PRECEDENCIA, NRO_PREDECESORES, NRO_SUCESORES)

# Ejecuto algoritmo MIXALB-2 con método: "kilbridge y webster"
reportar_solucion("MIXALB2 - Kilbridge y Webster", MIXALB2, "kilbridge y webster", ET_OBJETIVO,
                  TIEMPOS, PRECEDENCIA, NRO_PREDECESORES, NRO_SUCESORES)

# Ejecuto algoritmo MIXALB-2 con método: "bedworth"
reportar_solucion("MIXALB2 - Bedworth", MIXALB2, "bedworth", ET_OBJETIVO,
                  TIEMPOS, PRECEDENCIA, NRO_PREDECESORES, NRO_SUCESORES)

# Ejecuto algoritmo MIX-COMSOAL-2
reportar_solucion("MIX-COMSOAL2", MIXCOMSOAL2, ET_OBJETIVO,
                  TIEMPOS, PRECEDENCIA, 1000000, 1000)
