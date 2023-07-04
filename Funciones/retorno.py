#Retorno de valores en una función

def perimetroCuadrado(lado):
    perimetro = lado *4
    return perimetro

def areaCuadrado(lado):
    area = lado * lado
    return area

#Return se utiliza cuando necesites hacer uso del resultado de una función

perimetro = perimetroCuadrado(lado=5)
area = areaCuadrado(lado=5)

print(f"El perimetro obtenido es de {perimetro} y el area corresponde a {area}")

#Si no se coloca el retorno, la variable recibe none como resultado, ya que la función no está retornando nada

#Es posible que una función retorne dos valores, esto se puede realiar de la siguiente manera

def cuadrado(lado):
    perimetro = lado *4
    area = lado * lado
    return perimetro, area


perimetroCuadrado, areaCuadrado = cuadrado(lado=5)

print(f"Esto se realiza mediante el retorno de 2 valores en una función: perimetro = {perimetroCuadrado}, area= {areaCuadrado}")

#En el caso de capturar 2 resultados en una sola variable se recibe una tupla, esto lo podemos ver a continuación

resultadoFuncion = cuadrado(lado=8)
print("---------------------------------------------")
print("En el caso de capturar 2 resultados en una sola variable se recibe una tupla, esto lo podemos ver a continuación")
print(resultadoFuncion)


