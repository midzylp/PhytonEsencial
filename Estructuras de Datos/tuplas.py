#Las tuplas son muy parecidas a las listas, estás tambien mantienen el ordenamiento de los elementos
#Se denominan entre parentesis y no entre llaves

frutas = ("Manzana","Pera","Durazno","Piña")
print(frutas)

#Su principal diferencia radica en que estas son inmutables, es decir que no pueden cambiar sus elementos una vez declarados
#frutas[1] = "Aguacate"
#La instrucción anterior genera un error ya que esto no es posible de hacer en las tuplas


#Cuentan con otras funciones como las de las listas, como en el caso de len para determinar la longitud
print(len(frutas))

#Se puede acceder al elemento deseado de la misma forma que en las listas
print(frutas[1])
print(frutas[0:2])

