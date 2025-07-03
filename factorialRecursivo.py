def factorial_recursive(n):
    """Calcula el factorial de un número entero no negativo de forma recursiva.
    :param n: Número entero no negativo del cual se desea calcular el factorial.
    :return: El factorial de n.
    :raises ValueError: Si n es negativo.
    :raises TypeError: Si n no es un entero.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
    # ejemplo de uso

print(factorial_recursive(5))  # Output: 120
print(factorial_recursive(0))  # Output: 1      
print(factorial_recursive(1))  # Output: 1
print(factorial_recursive(10))  # Output: 3628800      
print(factorial_recursive(-1))  # Uncommenting this line will raise a ValueError
