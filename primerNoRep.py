def primer_caracter_no_repetido( s:str) -> str | None:
    """
    Devuelve el primer caracter no repetido en la cadena s.
    Si no hay caracteres no repetidos, devuelve una cadena vacía.
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