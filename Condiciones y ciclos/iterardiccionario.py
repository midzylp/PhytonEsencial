#Definiendo un diccionario

datos = {
    "nombre" : "Luis",
    "apellido": "Sánchez",
    "edad": 26,
    "signo": "Capricornio"
}

#Con ciclo for

for llave in datos:
    print("Llave", llave)
    print("Valor", datos[llave])

#Iterando con keys
print("-----------------------------------------------------")
print("Iterando con keys")

for elemento in datos.keys():
    print(elemento)

#Iterando con values
print("-----------------------------------------------------")
print("Iterando con values")

for elemento in datos.values():
    print(elemento)