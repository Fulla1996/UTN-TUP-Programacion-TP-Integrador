########################## ATENCION ################################
###EJECUTAR ESTE CÓDIGO PRODUCIRÁ UN BUCLE PRACTICAMENTE INFINITO###
####################################################################
import timeit
import random
import string

#Para generar strings aleatorios
def rand_str(k = 10):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=k))
    return random_string

def busquedaLineal(arr, valor):
    for i, elemento in enumerate(arr):
        if elemento == valor:
            return i, elemento
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio, lista[medio]
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

#Ejecuta la función enviada como parámetro, se incluye dato_obj en caso de que sea búsqueda, si no se incluye debe de ejecutar el ordenamiento.
def ejec_con_timer(funcion, array, dato_obj = None):
    if dato_obj is None:
        start_time = timeit.default_timer()
        funcion(array)
        end_time = timeit.default_timer()
        return array, (end_time - start_time)
    else:
        start_time = timeit.default_timer()
        ret = funcion(array, dato_obj)
        end_time = timeit.default_timer()
        return ret, (end_time - start_time)

#Se inicializan variables
tiempoLineal = 0
tiempoBinario = 100
tiempoOrden = 0

#Se generan datos iniciales
lista_datos = [random.randint(1, 1000) for _ in range(10000)]
#lista_datos = [rand_str() for _ in range(1000000)]

while (tiempoLineal < (tiempoBinario + tiempoOrden)):
    lista_datos += [random.randint(1, 1000) for _ in range(1)]
    #lista_datos += [rand_str()]
    
    dato_objetivo = lista_datos[len(lista_datos) - 1]

    resultadoL, tiempoLineal = ejec_con_timer(busquedaLineal, lista_datos, dato_objetivo)
    lista_datos_ord, tiempoOrden = ejec_con_timer(list.sort, lista_datos.copy())
    resultadoB, tiempoBinario = ejec_con_timer(busqueda_binaria, lista_datos_ord, dato_objetivo)
    
    #Break en caso de error en búsqueda
    if resultadoL == -1 or resultadoB == -1:
        print("Objeto no encontrado")
        break
    
    print(len(lista_datos),tiempoLineal, tiempoBinario + tiempoOrden)




