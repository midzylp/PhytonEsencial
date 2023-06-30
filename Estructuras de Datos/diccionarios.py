#A diferencia de las listas y las tuplas aquí se guardan los datos como llave y valor o clave y valor, no son ordenadas
#Se definen entre llaves
lenguaje = {
    "nombre":"python",
    "creador":"Guido",
    "año": 1991
}

print(lenguaje)

#Acceder a sus elemento se hace por medio de la llave
print(lenguaje["creador"])

#Añadir nuevos elementos
lenguaje["año de aprendizaje"] = 2023
print(lenguaje)

#Las llaves son valores unicos, no pueden ser repetidos

#Tambien pueden tener una lista como valor, por ejemplo
lenguaje["caracteristicas"] = ["sencillo","facil","util"]
print(lenguaje)

#Algunas de las funciones que se le atribuyen a las listas son los siguientes

#items, retorna tuplas con las llaves y valores de el diccionario
print("Función items")
print(lenguaje.items())

#keys, retorna todas las llaves del diccionario
print("Función keys")
print(lenguaje.keys())

#values, retorna todos los valores del diccionario
print("Función values")
print(lenguaje.values())