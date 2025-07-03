
def es_palindromo(frase):
    frase = frase.lower().replace(" ", "")
    return frase == frase[::-1]

frase="Anita lava la tina"

print(f"La frase '{frase}' es un palíndromo: {es_palindromo(frase)}")