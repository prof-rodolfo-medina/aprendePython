def fizzBuzz(n):
    """    
    Imprime los números del 1 al n, reemplazando:
    - Múltiplos de 3 por "Fizz"
    - Múltiplos de 5 por "Buzz"
    - Múltiplos de 3 y 5 por "FizzBuzz"
    
    :param n: Límite superior del rango a imprimir.
    """
    if n < 1:
        raise ValueError("El valor de n debe ser un entero positivo mayor o igual a 1")
    if not isinstance(n, int):
        raise TypeError("El valor de n debe ser un entero")
    lista = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append("FizzBuzz")
        elif i % 3 == 0:
            lista.append("Fizz")
        elif i % 5 == 0:
            lista.append("Buzz")
        else:
            lista.append(i)
    return str(lista)

# Ejemplo de uso
n = 15
print(f"La lista fizz-buzz de {n} es {fizzBuzz(n)}")
# Output esperado:
# 1     
# 2
# Fizz      
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz      
# 11
# Fizz  
# 13
# 14    
# FizzBuzz
fizzBuzz(7)