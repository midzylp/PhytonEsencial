from creandomodulo import areaCuadrado, perimetroCuadrado
from figuras.circulo import areaCirculo, perimetroCirculo

#La forma correcta de importar un modulo es justo como se realiza en la parte superior

lado = 10

cuadrado = {
    "lado" : lado,
    "perimetro" : perimetroCuadrado(lado),
    "area" : areaCuadrado(lado)
}

print(cuadrado)

radio = 5
diametro = 10

circulo = {
    "radio" : radio,
    "diametro": diametro,
    "area" : areaCirculo(radio),
    "perimetro" : perimetroCirculo(diametro)
}

print(f"El area del circulo con radio {circulo['radio']} y con diametro {circulo['diametro']} es {circulo['area']} y su perimetro es {circulo['perimetro']}")