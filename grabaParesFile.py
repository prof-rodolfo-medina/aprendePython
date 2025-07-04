def escribir_pares(nombre_archivo):
    """
    Escribe los números pares del 1 al 100 en un archivo, uno por línea.
    
    :param nombre_archivo: Nombre del archivo donde se guardarán los números pares.
    :return: None
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        for numero in range(1, 101):
            if numero % 2 == 0:
                f.write(f"{numero}\n")

# Ejemplo de uso:
# escribir_pares("pares.txt")
