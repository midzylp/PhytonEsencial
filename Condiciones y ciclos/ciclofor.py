#El ciclo for nos permite iterar sobre cada elemento de la estructura de datos, o sobre strings

texto = "Parangaricutirimicuaro"

for letra in texto:
    print(letra)

#Asi es la sintaxis general de un ciclo for, letra es el nombre que se le da a cada uno de los elementos, in se utiliza para saber sobre 
#que elemento se debe iterar

lenguajes = ["Python", "C", "C++", "Java", "JavaScript"]

#Tambien es posible iterar sobre listas, estructuras de datos, etc

for lenguaje in lenguajes:
    print(lenguaje)
    if lenguaje == "C++":
        break

#Existen instrucciones que pueden modificar el flujo de un ciclo, como la secuencia break, en el caso de arriba, si la colocamos
#Observamos que se rompe el ciclo despues de la primera iteración, aunque generalmente se usa alguna condicion, en el caso de arriba se va a romper cuando encuentre a C++

#Tambien existe el continue, el cual hace que se salte la siguiente instrucción y continue con el codigo, por ejemplo

for lenguaje in lenguajes:
    if lenguaje == "C":
        continue
    print(lenguaje)

#Tambien existe la posibilidad de iterar sobre range, el cual crea una listades de 0 hasta un numero anterior al que se coloque

for numero in range(6):
    print(numero)

