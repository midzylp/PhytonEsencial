#Los objetos por si mismos no tienen ninguna propiedad, esas deben ser definidas por cada desarrollador

#El constructor en python se define con el método __init__, esté método siempre se ejecuta al instanciar un objeto
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños numero {self.edad} {self.nombre}")


paco = Persona("Paco", 25)

#Al igual que atributos, los objetos tambien cuentan con métodos, es decir acciones que pueden realizar, por ejemplo
#El metodo cumplir_anios(self), este debe llevar la palabra reservada self para saber que estamos haciendo referencia al objeto
#Tambien se define con def

paco.cumplir_anios()