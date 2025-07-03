def primer_caracter_no_repetido( s:str) -> str | None:
    """ 
    Encuentra el primer caracter no repetido en una cadena de caracteres.
    Esta función recorre la cadena de caracteres y utiliza un diccionario
    para contar la frecuencia de cada caracter. Luego, busca el primer 
    caracter que tiene una frecuencia de 1, lo que indica que es no repetido.
    Si no se encuentra ningún caracter no repetido, devuelve None.

    :param s: Cadena de caracteres en la que se buscará el primer caracter no repetido.
    :return: El primer caracter no repetido en la cadena s, o None si no
    se encuentra ninguno.
    """
    contador = {}
    
    # Contar la frecuencia de cada caracter
    for caracter in s:
        if caracter in contador:
            contador[caracter] += 1
        else:
            contador[caracter] = 1
    
    # Buscar el primer caracter con frecuencia 1
    for caracter in s:
        if contador[caracter] == 1:
            return caracter
    
    return None  # Si no se encuentra, devolver cadena vacía


# Ejemplo de uso
cadena = "abacabadabacaba"
resultado = primer_caracter_no_repetido(cadena)     
print(f"El primer caracter no repetido en '{cadena}' es: {resultado if resultado is not None else 'No hay caracteres no repetidos'}")