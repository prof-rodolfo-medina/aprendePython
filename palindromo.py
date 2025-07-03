
def es_palindromo(frase):
    """    
    Verifica si una frase es un palíndromo.
    Un palíndromo es una palabra, frase o secuencia que se lee igual hacia adelante y hacia atrás, ignorando espacios, mayúsculas y puntuación.
    
    :param frase: Frase a verificar.
    :return: True si la frase es un palíndromo, False en caso contrario.
    """
    frase = frase.lower().replace(" ", "")
    return frase == frase[::-1]

frase="Anita lava la tina"

print(f"La frase '{frase}' es un palíndromo: {es_palindromo(frase)}")