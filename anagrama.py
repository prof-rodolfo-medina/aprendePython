def anagrama(s1, s2):
    """
    Verifica si dos cadenas son anagramas.
    Un anagrama es una palabra o frase formada reordenando las letras de otra.
    
    :param s1: Primera cadena a verificar.
    :param s2: Segunda cadena a verificar.
    :return: True si las cadenas son anagramas, False en caso contrario.
    """
    return sorted(s1) == sorted(s2)

def anagrama_dictionary(s1, s2):
    """
    Verifica si dos cadenas son anagramas utilizando un diccionario para contar las letras.
    
    :param s1: Primera cadena a verificar.
    :param s2: Segunda cadena a verificar.
    :return: True si las cadenas son anagramas, False en caso contrario.
    """
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

def anagrama_counter(s1, s2):
    """
    Verifica si dos cadenas son anagramas utilizando la clase Counter de collections.
    
    :param s1: Primera cadena a verificar.
    :param s2: Segunda cadena a verificar.
    :return: True si las cadenas son anagramas, False en caso contrario.
    """
    from collections import Counter
    return Counter(s1) == Counter(s2)   
# Ejemplo de uso
s1 = "listen"
s2 = "silent"       
print(f"¿'{s1}' y '{s2}' son anagramas? {anagrama(s1, s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con diccionario)? {anagrama_dictionary(s1, s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con Counter)? {anagrama_counter(s1, s2)}")  
# Output esperado:
# ¿'listen' y 'silent' son anagramas? True  
# ¿'listen' y 'silent' son anagramas (con diccionario)? True
# ¿'listen' y 'silent' son anagramas (con Counter)? True
# Ejemplo de uso con cadenas no anagramas
s1 = "hello"    
s2 = "world"
print(f"¿'{s1}' y '{s2}' son anagramas? {anagrama(s1, s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con diccionario)? {anagrama_dictionary(s1, s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con Counter)? {anagrama_counter(s1, s2)}")
# Output esperado:  
# ¿'hello' y 'world' son anagramas? False
# ¿'hello' y 'world' son anagramas (con diccionario)? False     
# ¿'hello' y 'world' son anagramas (con Counter)? False
# Ejemplo de uso con cadenas con espacios y mayúsculas
s1 = "Dormitory"    
s2 = "Dirty room"
norm_s1 = s1.replace(" ", "").lower()
norm_s2 = s2.replace(" ", "").lower()
print(f"¿'{s1}' y '{s2}' son anagramas? {anagrama(norm_s1, norm_s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con diccionario)? {anagrama_dictionary(norm_s1, norm_s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con Counter)? {anagrama_counter(norm_s1, norm_s2)}")
# Output esperado:  
# ¿'Dormitory' y 'Dirty room' son anagramas? True
# ¿'Dormitory' y 'Dirty room' son anagramas (con diccionario)? True
# ¿'Dormitory' y 'Dirty room' son anagramas (con Counter)? True 
# Ejemplo de uso con cadenas con caracteres especiales
s1 = "Astronomer"   
s2 = "Moon starer"
norm_s1 = s1.replace(" ", "").lower()   
norm_s2 = s2.replace(" ", "").lower()
print(f"¿'{s1}' y '{s2}' son anagramas? {anagrama(norm_s1, norm_s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con diccionario)? {anagrama_dictionary(norm_s1, norm_s2)}")
print(f"¿'{s1}' y '{s2}' son anagramas (con Counter)? {anagrama_counter(norm_s1, norm_s2)}")
# Output esperado:  
# ¿'Astronomer' y 'Moon starer' son anagramas? True
# ¿'Astronomer' y 'Moon starer' son anagramas (con diccionario)? True
# ¿'Astronomer' y 'Moon starer' son anagramas (con Counter)? True   
# Ejemplo de uso con cadenas con números
s1 = "12345"    
s2 = "54321"
