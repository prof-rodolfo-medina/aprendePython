def fibonacci_serie(n, serie=None):
    """
    Genera la serie de Fibonacci de longitud n de manera recursiva.
    """
    if serie is None:
        serie = []
    if len(serie) == n:
        return serie
    if len(serie) < 2:
        serie.append(len(serie))
    else:
        serie.append(serie[-1] + serie[-2])
    return fibonacci_serie(n, serie)

# Ejemplo de uso:
print(fibonacci_serie(100))  # Salida: [0, 1, 1, 2, 3, 5, 8, 13]
