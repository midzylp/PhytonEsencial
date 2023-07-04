#La herencia nos habla de clases padres y clases hijas
#Las clases hijas aprovechan atributos y métodos de la clase padre para reusar codigo

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños numero {self.edad} {self.nombre}")


#En este caso la clase Persona será la clase padre y la clase empleado será la clase hija, con la adición
#De que esta ultima podrá trabajar


#Entre parentesis se pone el nombre de la clase padre, solo se coloca si es hija de otra clase
class Empleado(Persona):
    def __init__(self, horasTotales, nombre, edad):
        super(Empleado,self).__init__(nombre, edad)
        self.horasTotales = horasTotales

    def trabajar(self, horas):
        self.horasTotales += horas
        print(f"Usted ha trabajado {horas} horas")
        print(f"Usted ha trabajado en total {self.horasTotales}")

#El error que se experimenta se debe a que el constructor de Empleado fue sobreescrito y ya no hereda el mismo de la clase Persona

#Debe recibir atributos nombre y edad porque los está heredando directamente de la clase persona
paco = Empleado(nombre="Paco",edad= 24, horasTotales=30)
paco.trabajar(7)
paco.cumplir_anios()



