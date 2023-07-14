#El assertion error es similar al raise exception sin embargo no es necesario especificar el error

def calcularPromedio(lista):
    assert len(lista) > 0 , "La lista debe tener al menos 1 elemento"
    return sum(lista) / len(lista)


promedio = calcularPromedio(lista=[10,20,30,40])

print(promedio)