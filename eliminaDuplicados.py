def elimina_duplicados(lista):
    """
    Elimina los elementos duplicados de una lista.
    
    :param lista: Lista de elementos, puede contener duplicados.
    :return: Lista sin duplicados.
    """
    return list(set(lista))

lista = [1, 2, 3, 4, 5, 1, 2, 3]
print(elimina_duplicados(lista))  # Salida: [1, 2, 3, 4, 5]