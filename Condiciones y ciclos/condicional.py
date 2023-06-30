#Las condicionales en python se pueden realizar mediante if, elif y else

a = 2
b = 2

if a<b:
    print("A es menor que B")
elif a==b :
    print("A es igual que B")
else:
    print("A es mayor que B")

#La identación es muy importante porque en pyton esto indica el alcance del bloque de codigo 

#Tambien se pueden evaluar condiciones booleanas de la siguiente forma

c = False

#if c está evaluando si la variable c es verdadera
if c:
    print("C es verdadero")
else:
    print("C es falso")

#Tambien se pueden combinar otras instrucciones, como el is, and y or, por ejemplo

if type(c) is bool:
    print("C es booleano")
else:
    print("C no es booleano")

#Aqui se utiliza and y or

numero1= 10
numero2= 5
numero3= 1

if numero1 > numero2 and numero2>numero3:
    print("10 es mayor que 5 y 5 es mayor que 1")
else:
    print("Whatever")

