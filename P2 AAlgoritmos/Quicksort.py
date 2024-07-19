def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]
        menores = [x for x in arr if x < pivote]
        iguales = [x for x in arr if x == pivote]
        mayores = [x for x in arr if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

lista = [34, 7, 23, 32, 5, 62, 32, 2, 78, 45, 21, 56, 89, 12, 3]
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)
