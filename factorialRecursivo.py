def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
    # ejemplo de uso

print(factorial_recursive(5))  # Output: 120
print(factorial_recursive(0))  # Output: 1      
print(factorial_recursive(1))  # Output: 1
print(factorial_recursive(10))  # Output: 3628800       
