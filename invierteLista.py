class Nodo:
    """Representa un nodo de una lista enlazada."""
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def invertir_lista_enlazada(cabeza):
    """
    Invierte una lista enlazada.
    Retorna la nueva cabeza de la lista invertida.
    """
    anterior = None
    actual = cabeza

    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    return anterior

def crear_lista(valores):
    """Crea una lista enlazada a partir de una lista de valores y retorna la cabeza."""
    if not valores:
        return None
    cabeza = Nodo(valores[0])
    actual = cabeza
    for valor in valores[1:]:
        actual.siguiente = Nodo(valor)
        actual = actual.siguiente
    return cabeza

def imprimir_lista(cabeza):
    """Imprime los valores de una lista enlazada.
    
    Args:        cabeza (Nodo): La cabeza de la lista enlazada. 
    returns: None
    """
    valores = []
    actual = cabeza
    while actual:
        valores.append(str(actual.valor))
        actual = actual.siguiente
    print(" -> ".join(valores))

# Ejemplo de uso:
if __name__ == "__main__":
    cabeza = crear_lista([1, 2, 3, 4])
    print("Lista original:")
    imprimir_lista(cabeza)
    invertida = invertir_lista_enlazada(cabeza)
    print("Lista invertida:")
    imprimir_lista(invertida)
