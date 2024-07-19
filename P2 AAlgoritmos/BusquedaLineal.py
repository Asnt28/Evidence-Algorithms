def linearsearch(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


arr = [1, 2, 3, 4, 5]
x = 0
n = len(arr)
position = linearsearch(arr, n, x)
if position == -1:
    print("Elemento no se encontro")
else:
    print("Elemento se encuenta en la lista", position)
