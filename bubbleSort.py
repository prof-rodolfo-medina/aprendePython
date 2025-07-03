def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista    

# ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(lista)    
print("Lista ordenada:", sorted_list)
# salida esperada: Lista ordenada: [11, 12, 22, 25, 34, 64, 90]
# el algoritmo de ordenamiento burbuja (bubble sort) es un algoritmo de ordenamiento    