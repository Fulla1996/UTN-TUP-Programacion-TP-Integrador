import timeit
import random

def ejec_con_timer(funcion, array):
    start_time = timeit.default_timer()
    funcion(array)
    end_time = timeit.default_timer()
    print(f"Tiempo de ejecución de {funcion.__name__}, {(end_time - start_time)}, segundos")


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
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
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

def busquedaLineal(arr, valor):
    for i in arr:
        if i == valor:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

#Se inicializa una lista con números aleatorios
lista_datos = [random.randint(1, 1000) for _ in range(20000)]
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
for funcion in funciones_a_usar:
    ejec_con_timer(funcion, lista_datos.copy())

#Se ordena el listado
lista_datos = quick_sort(lista_datos)
#Se incorporan más datos
cant = 100
print(f"Se incorporan {cant} nuevos datos")
lista_datos+= [random.randint(1, 1000) for _ in range(cant)]

#Se vuelven a ejecutar las funciones listadas
for funcion in funciones_a_usar:
    ejec_con_timer(funcion, lista_datos.copy())

