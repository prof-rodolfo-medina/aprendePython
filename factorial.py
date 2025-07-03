def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    # ejemplo de uso
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1    
# print(factorial(-1))  # Uncommenting this line will raise a ValueError
# print(factorial(1.5))  # Uncommenting this line will raise a TypeError
# print(factorial("5"))  # Uncommenting this line will raise a TypeError