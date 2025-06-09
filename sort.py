from collections import defaultdict
import timeit
import random
import string

def rand_str(k = 10):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=k))
    return random_string

def ejec_con_timer(funcion, array):
    start_time = timeit.default_timer()
    funcion(array)
    end_time = timeit.default_timer() 
    return (end_time - start_time)
    

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >=0 and key < arr[j] :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar el índice del elemento mínimo
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambiar el elemento mínimo con el elemento actual
        arr[i], arr[min_index] = arr[min_index], arr[i]

def quick_sort_rand(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort_rand(less) + [pivot] + quick_sort_rand(greater)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
def bubble_sort(arr):
    arr_aux = arr[:]
    for i in range(0,len(arr_aux)-1):
        for j in range(i + 1,len(arr_aux)):
            if arr_aux[i] > arr_aux[j]:
                arr_aux[i], arr_aux[j] = arr_aux[j], arr_aux[i]
    return arr_aux

#Se inicializa una lista con números aleatorios
lista_datos_str = [rand_str() for _ in range(200)]
lista_datos = [random.randint(1, 1000) for _ in range(200)]

#Se inicializa vector para resultados de strings
resultadosStrPreOrden = defaultdict(list)
resultadosStrPostOrden = defaultdict(list)
#Se inicializa vector para resultados de ints
resultadosIntPreOrden = defaultdict(list)
resultadosIntPostOrden = defaultdict(list)

#Se define una lista de funciones a utilizar
funciones_a_usar = [
    bubble_sort,
    #quick_sort,
    quick_sort_rand,
    insertion_sort,
    selection_sort,
    list.sort
]

#Se ejecutan las funciones listadas a través de una función que incluye la funcionalidad del TimeIt con mensajes de consola
for i in range(10):
    for funcion in funciones_a_usar:
        resultadosStrPreOrden[funcion.__name__].append(ejec_con_timer(funcion, lista_datos_str.copy()))
        resultadosIntPreOrden[funcion.__name__].append(ejec_con_timer(funcion, lista_datos.copy()))

#Se ordena el listado
lista_datos = quick_sort_rand(lista_datos)
lista_datos_str = quick_sort_rand(lista_datos_str)
#Se incorporan más datos
cant = 200
print(f"Se incorporan {cant} nuevos datos")
lista_datos+= [random.randint(1, 1000) for _ in range(cant)]
lista_datos_str += [rand_str() for _ in range(cant)]

#Se vuelven a ejecutar las funciones listadas
for i in range(10):
    for funcion in funciones_a_usar:
        resultadosStrPostOrden[funcion.__name__].append(ejec_con_timer(funcion, lista_datos_str.copy()))
        resultadosIntPostOrden[funcion.__name__].append(ejec_con_timer(funcion, lista_datos.copy()))

for funcion in funciones_a_usar:
    print(f"Los tiempos antes de ordenar de {funcion.__name__} sobre Int son: {resultadosIntPreOrden[funcion.__name__]}")
    print(f"Los tiempos antes de ordenar de {funcion.__name__} sobre Strings son: {resultadosStrPreOrden[funcion.__name__]}")

for funcion in funciones_a_usar:
    print(f"Los tiempos despues de ordenar de {funcion.__name__} sobre Int son: {resultadosIntPostOrden[funcion.__name__]}")
    print(f"Los tiempos despues de ordenar de {funcion.__name__} sobre Strings son: {resultadosStrPostOrden[funcion.__name__]}")