#Los sets guardan elementos unicos, se definen entre llaves
set1= {1,2,3}
print(set1)

#No son estructuras de datos ordenados, contienen elementos unicos, es decir que no podemos guardar el mismo valor varias veces
set2={1,1,1,2,3} #Esto solo guarda el 1, una sola vez

#No se pueden acceder a los elementos mediante indices al no ser ordenados

#Pueden contener diferentes tipos de elementos, por ejemplo

set3={"hola",2,3.5}
print(set3)

#Son mutables al igual que las listas pero no se pueden modificar los valores previamente establecidos
#Se añaden elementos a los sets con la función add
set1.add(4)
print(set1)

#Tambien pueden añadirse varios elementos con la función update, por ejemplo
set1.update([5,6,7])
print(set1)

#Se pueden eliminar elementos con discard
set1.discard(7)
print(set1)

#Función clear, y función remove
