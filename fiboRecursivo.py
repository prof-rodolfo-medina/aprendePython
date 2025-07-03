def fibo(n):
    """    
    Calcula el n-ésimo número de la serie de Fibonacci de forma recursiva.
    
    :param n: Índice del número de Fibonacci a calcular (0-indexed).
    :return: El n-ésimo número de Fibonacci.
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

# Ejemplo de uso

print(fibo(10))  # Imprime el décimo número de Fibonacci
print(fibo(20))  # Imprime el vigésimo número de Fibonacci          
