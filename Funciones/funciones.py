#En python existen dos tipos de funciones, las built-in-functions que ya vimos anteriormente
#Y las user-defined-functions, son funciones creadas por el usuario

#Declarando una función/palabra reservada def
""" Sintaxis
def nombreFuncion(paránmetros):
    Instrucciones a ejecutar

 """


#Las variables locales generalmente se escriben en mayuscula y pueden ser usadas dentro y fuera de funciones, por ejemplo APELLIDO

APELLIDO = "Sánchez"

def funcion():
    nombre = "Luis" #Se pueden declarar variables dentro de funciones, sin embargo estas solo pueden ser usadas dentro de la misma
    print("Hello, world", nombre, APELLIDO)
    


funcion()
funcion()
funcion()
#print(nombre) Esto no puede realizarse porque la variable solo está definida dentro de la función
#Llamando al apellido desde fuera de la función
print("La variable global apellido tambien puede ser llamada fuera, como en este ejemplo", APELLIDO)