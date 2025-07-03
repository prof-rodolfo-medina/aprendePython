def mas_frecuente(lista):
    """
    Devuelve el elemento más frecuente en la lista.
    Si hay un empate, devuelve el primero que aparece.
    """
    if not lista:
        return None

    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1

    max_frecuencia = max(frecuencia.values())
    for elemento in lista:
        if frecuencia[elemento] == max_frecuencia:
            return elemento
        
# Ejemplo de uso
lista = [1, 2, 3, 2, 4, 3, 2]
print(mas_frecuente(lista))  # Salida: 2