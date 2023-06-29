#Son elementos ordenados, se caracterizan por estar entre llaves

lenguajes = ["phyton","java","javascript"]
print(lenguajes)
#Mantienen el orden en el cual se declararon, permite elementos duplicados

#Tambien puede contener diferentes tipos de variables por ejemplo

listaVariada = [2.0, 5, True, "Aguacate", 2.0]
print(listaVariada)

#Se puede acceder a un elemento de la lista mediante su indice, por ejemplo
listaVariada[0] #Aquí se accede al elemento 2.0

#Se puede acceder a la longitud de una lista con la función len
print("La longitud de la listaVariada es ",len(listaVariada))

#Se puede acceder a un elemento especifico de la lista por su indice iniciando desde el final con -1
listaVariada[-1] #Esto traería el ultimo elemento de la lista, el -2 el penultimo y asi sucesivamente

#Se pueden traer ciertos elementos de una lista mediante esta manera
print(listaVariada[0:2]) #Esto imprime el elemento en el indice 0 y en el indice 1

#Tambien podemos tener listas anidadas, esto se puede realizar de esta forma

listaAnidada = [listaVariada, "elementoextra1" , "elementoextra2"]

print(listaAnidada) #Para acceder a un elemento en especifico de esta lista debemos hacer uso de doble corchete, por ejemplo listaAnidada[0][0]
#Ese comando imprimiria selecciona el elemento 2.0

#Las listas son mutables(pueden cambiar su valor una vez ya han sido declaradas, por ejemplo)
#listaVariada[0] = "Elemento intercambiado" esto modificaría el 2.0 y lo reemplazaria por "Elemento intercambiado"

#Existe una función para listas llamada append, esto agrega un elemento al final de una lista
listaVariada.append("Guayaba")

print(listaVariada)