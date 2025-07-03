def parentesis_balanceados(cadena):
    """
    Verifica si los paréntesis en una cadena están balanceados.
    
    :param cadena: Cadena con paréntesis a verificar.
    :return: True si los paréntesis están balanceados, False en caso contrario.
    """
    pila = []
    parentesis_apertura = '({['
    parentesis_cierre = ')}]'
    for char in cadena:
        if char in parentesis_apertura:
            pila.append(char)
        elif char in parentesis_cierre:
            if not pila or parentesis_apertura.index(pila[-1]) != parentesis_cierre.index(char):
                return False
            pila.pop()
    return len(pila) == 0

# Ejemplo de uso
cadena = "((a + b) * (c - d))"
print(f"¿La cadena '{cadena}' tiene paréntesis balanceados? {parentesis_balanceados(cadena)}")
# Output esperado: True
cadena = "((a + b) * (c - d))]"
print(f"¿La cadena '{cadena}' tiene paréntesis balanceados? {parentesis_balanceados(cadena)}")
# Output esperado: False
cadena = "{[(a + b) *2+(c)]* (c - d)}"
print(f"¿La cadena '{cadena}' tiene paréntesis balanceados? {parentesis_balanceados(cadena)}")
# Output esperado: True
cadena = "([a + b) * (c - d])"
print(f"¿La cadena '{cadena}' tiene paréntesis balanceados? {parentesis_balanceados(cadena)}")