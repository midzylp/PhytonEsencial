#Mi primer comentario
print("Hello, world ") #Comando para imprimir

""" Se pueden usar las triples comillas 
para realizar comentarios multilinea """

nombre = input("Escribe tu nombre\n") #Declarando una variable llamada nombre con un String "Anita"
edad = input("Escribe tu edad, está sera de tipo String\n")
print("Hello " + nombre +  "\nTu edad es " + edad)

#Declarando otras variables

edadint = 26 #Variable tipo int
estatura = 1.64 #Variable tipo float
positivo = True #Variable booleana true
negativo = False #Variable booleana false

#Se puede determinar el tipo de una variable con la función type

print("La variable edad int es de tipo " + str(type(edadint)))
print("La variable estatura es de tipo " + str(type(estatura)))
print("La variable positivo es de tipo " + str(type(positivo)))
print("La variable negativo int es de tipo " + str(type(negativo)))