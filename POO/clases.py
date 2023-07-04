#Al igual que en Java para poder crear un objeto se necesita un prototipo/modelo, este recibe el nombre de clase
#Para crear una clase usamos la palabra reservada class

class Persona:
    pass


#Para crear un objeto de tipo persona(instanciar) se colocan las instrucciones de la siguiente manera
pedro = Persona()

print(type(pedro))

#Instanciando un nuevo objeto

paco = Persona()

print(type(paco))

#Podemos observar que los 2 objetos son de tipo persona, sin embargo si los comparamos obtendremos false

print(f"Es Pedro igual a Paco", pedro == paco)