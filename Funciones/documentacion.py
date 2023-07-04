#Es importante documentar la función para que la persona que lea el codigo esté mas consciente de lo que hace
#Se puede declarar despues de declarar la función con comillas triples
#La primera linea corresponde a una descripción corta, es decir el titulo
def perimetro_cuadrado(lado):
    """ Calcula el perimetro de un cuadrado.
    
    Esta función recibe el valor de un lado de un cuadrado y a partir de este retorna su perimetro.

    Args:
        lado(int):El lado es la medida del lado del cuadrado

    Returns:
        perimetro(int): El perimetro del cuadrado

    """
    perimetro = lado * 4
    return perimetro

perimetro_cuadrado(lado=5)

