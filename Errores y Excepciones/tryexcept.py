#Se puede utilizar bloque try y catch para el manejo de excepciones en python

def calcularPromedio(lista):
    #assert len(lista) > 0 , "La lista debe tener al menos 1 elemento"
    return sum(lista) / len(lista)

try:
    promedio = calcularPromedio(lista=[])
    print(promedio)
except Exception as e:
    print("La función no calculó el promedio")
    print(e)