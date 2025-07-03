def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)  

# ejemple de uso
lista = [3, 6, 8, 10, 1, 2, 1]
print("Lista original:", lista)     
print("Lista ordenada:", quicksort(lista))  # salida: [1, 1, 2, 3, 6, 8, 10]
print("Lista ordenada:", quicksort([]))  # salida: []   
print("Lista ordenada:", quicksort([5]))  # salida: [5]
print("Lista ordenada:", quicksort([5, 3, 8, 6, 2, 7, 4, 1]))  # salida: [1, 2, 3, 4, 5, 6, 7, 8]
print("Lista ordenada:", quicksort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista ordenada:", quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista ordenada:", quicksort([5, 5, 5, 5, 5]))  # salida: [5, 5, 5, 5, 5]
print("Lista ordenada:", quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]))  # salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
print("Lista ordenada:", quicksort([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # salida: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
