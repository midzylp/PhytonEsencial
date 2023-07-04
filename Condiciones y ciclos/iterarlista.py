#Iterando sobre una lista

lenguajes = ["Python", "C++","C","Java","JavaScript"]

for lenguaje in lenguajes:
    print(lenguaje)

#Se puede iterar de forma distinta, por ejemplo

for index in range(len(lenguajes)):
    print("Indice", index)
    print("Elemento", lenguajes[index])

#Tambien se puede iterar mediante ciclo while

print("Iterando con ciclo while")

i=0
while i < len(lenguajes):
    print(lenguajes[i])
    i +=1

