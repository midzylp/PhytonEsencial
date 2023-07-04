#Podemos definir diferentes atributos, estos se refieren a las caracteristicas que definen las caracteristicas del objeto


#Estos atributos se añaden en el constructor de la clase, de la misma forma que se añaden parametros en las funciones
class Persona:
    atributo = 123
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#La instrucción self.nombre se usa para declarar que ese atributo estará presente en toda la clase, posteriormente le añadimos el valor que recibimos del constructor

#De esta forma podemos asignarle los atributos al momento de instanciar a una persona

paco = Persona("Paco", 25)

print("El nombre del objeto persona paco es", paco.nombre, "y su edad es", paco.edad)

#Tambien es posible declarar atributos de clase, estos seran compartidos por todos los objetos de esta clase
#En este caso lo declaramos fuera del constructor, en este ejemplo el atributo con nombre atributo

print(paco.atributo)