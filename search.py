########################## ATENCION ################################
###EJECUTAR ESTE CÓDIGO PRODUCIRÁ UN BUCLE PRACTICAMENTE INFINITO###
####################################################################

from collections import defaultdict
import timeit
import random
import string
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

def quick_sort_rand(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort_rand(less) + [pivot] + quick_sort_rand(greater)
    
def ejec_con_timer(funcion, array, dato_obj = None):
    if dato_obj is None:
        start_time = timeit.default_timer()
        funcion(array)
        end_time = timeit.default_timer()
        #print(f"Tiempo de ejecución de {funcion.__name__}, {(end_time - start_time)}, segundos")
        return array, (end_time - start_time)
    else:
        start_time = timeit.default_timer()
        ret = funcion(array, dato_obj)
        end_time = timeit.default_timer()
        #print(f"Tiempo de ejecución de {funcion.__name__}, {(end_time - start_time)}, segundos")
        return ret, (end_time - start_time)
    
tiempoLineal = 0
tiempoBinario = 100
tiempoOrden = 0
i = 0


lista_datos = [random.randint(1, 1000) for _ in range(10000)]
#lista_datos = [rand_str() for _ in range(1000000)]

while (tiempoLineal < (tiempoBinario + tiempoOrden)):
    lista_datos += [random.randint(1, 1000) for _ in range(1)]
    #lista_datos += [rand_str()]
    
    dato_objetivo = lista_datos[len(lista_datos) - 1]

    resultadoL, tiempoLineal = ejec_con_timer(busquedaLineal, lista_datos, dato_objetivo)
    lista_datos_ord, tiempoOrden = ejec_con_timer(list.sort, lista_datos.copy())
    resultadoB, tiempoBinario = ejec_con_timer(busqueda_binaria, lista_datos_ord, dato_objetivo)
    if resultadoL == -1 or resultadoB == -1:
        print("Objeto no encontrado")
        break
    print(len(lista_datos),tiempoLineal, tiempoBinario + tiempoOrden)




