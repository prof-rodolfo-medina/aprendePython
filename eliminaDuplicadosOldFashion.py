def elimina_duplicados_old_fashioned(lista):
    """
    Elimina los elementos duplicados de una lista de forma tradicional.

    :param lista: Lista de elementos que pueden contener duplicados.
    :return: Lista sin elementos duplicados.
    """
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

lista = [1, 2, 3, 4, 5, 1, 2, 3]
lista_sin_duplicados = elimina_duplicados_old_fashioned(lista)
print(lista_sin_duplicados)  # Salida: [1, 2, 3, 4, 5]