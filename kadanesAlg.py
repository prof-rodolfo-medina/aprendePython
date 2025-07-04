def kadane(lista):
    """Implementación del algoritmo de Kadane para encontrar la sublista con la suma máxima.
    Args:
        lista (list): Lista de números enteros.
    Returns:
        int: La suma máxima de la sublista.
    """
    max_ending_here = max_so_far = lista[0]
    for x in lista[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Ejemplo de uso
lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = kadane(lista)
print(f"La suma máxima de la sublista es: {resultado}")
# Ejemplo de uso con una lista diferente
lista2 = [1, 2, 3, -2, 5]
resultado2 = kadane(lista2)
print(f"La suma máxima de la sublista es: {resultado2}")
# Ejemplo de uso con una lista que contiene un solo elemento
lista3 = [-1]   
resultado3 = kadane(lista3)
print(f"La suma máxima de la sublista es: {resultado3}")
# Ejemplo de uso con una lista que contiene todos elementos negativos
lista4 = [-2, -3, -1, -5]
resultado4 = kadane(lista4)
print(f"La suma máxima de la sublista es: {resultado4}")
# Ejemplo de uso con una lista que contiene todos elementos positivos
lista5 = [2, 3, 5, 7]
resultado5 = kadane(lista5)
print(f"La suma máxima de la sublista es: {resultado5}")
# Ejemplo de uso con una lista que contiene ceros
lista6 = [0, 0, 0, 0]   
resultado6 = kadane(lista6)
print(f"La suma máxima de la sublista es: {resultado6}")
# Ejemplo de uso con una lista que contiene números grandes