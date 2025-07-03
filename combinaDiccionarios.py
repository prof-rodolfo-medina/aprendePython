def combina_diccionarios(d1,d2):        
    """
    Combina dos diccionarios, sumando los valores de las claves comunes.
    
    :param d1: Primer diccionario
    :param d2: Segundo diccionario
    :return: Diccionario combinado
    """
    resultado = d1.copy()  # Copia el primer diccionario
    for clave, valor in d2.items():
        if clave in resultado:
            resultado[clave] += valor  # Suma los valores si la clave ya existe
        else:
            resultado[clave] = valor  # Añade la nueva clave y su valor
    return resultado

# Ejemplo de uso
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 3, 'c': 4, 'd': 5}
resultado = combina_diccionarios(diccionario1, diccionario2)    

print(resultado)  # Salida esperada: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
# El resultado combina los valores de las claves comunes y añade las nuevas claves.