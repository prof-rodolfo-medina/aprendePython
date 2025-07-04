import string

def contar_palabras(archivo):
    """
    Cuenta la frecuencia de cada palabra en un archivo de texto,
    ignorando mayúsculas y signos de puntuación.
    Retorna un diccionario con los resultados.
    
    :param archivo: Ruta al archivo de texto.
    :return: Diccionario con palabras como claves y sus frecuencias como valores.
    """
    conteo = {}

    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea_limpia = linea.translate(str.maketrans('', '', string.punctuation)).lower()
            palabras = linea_limpia.split()
            for palabra in palabras:
                conteo[palabra] = conteo.get(palabra, 0) + 1

    return conteo

# Ejemplo de uso:
# resultado = contar_palabras('mi_archivo.txt')
# print(resultado)
