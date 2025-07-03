def busqueda_binaria(lista, objetivo)->bool:
    """
    Realiza una búsqueda binaria en una lista ordenada.
    :param lista: Lista ordenada de números enteros.
    :return: True si el número 5 está en la lista, False en caso contrario.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False
# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(busqueda_binaria(numeros, 5))  # Debería devolver True