def suma_dos(lista, objetivo):
    """    
    Encuentra dos números en una lista que sumen un objetivo. 
      
    :param lista: Lista de números enteros.
    :param objetivo: Número entero que representa la suma objetivo. 
    :return: Tupla con los índices de los dos números que suman el objetivo, o None si no se encuentran.
    """
    numeros_vistos = {}
    for indice in range(len(lista)):
        complemento = objetivo - lista[indice]
        if complemento in numeros_vistos:
            return (numeros_vistos[complemento], indice)
        numeros_vistos[lista[indice]] = indice
    return None
# Ejemplo de uso
lista = [2, 7, 11, 15]
objetivo = 22    
resultado = suma_dos(lista, objetivo)
print(f"Los índices de los números que suman {objetivo} son: {resultado}" if resultado else "No se encontraron dos números que sumen el objetivo.") 
# Output esperado:
# Los índices de los números que suman 9 son: (0, 1)    