#Levantar excepciones
#Estas excepciones ocurren durante la ejecución del programa aunque el codigo esté bien escrito

def validar_x(x):
    if x <1:
        raise Exception("La variable X debe ser mayor a 1")
    else:
        print(f"El numero que introdujiste fue {x}")

validar_x(0)

#raise Exception es util cuando queremos que se alce una excepción en nuestro programa, en este caso al introducir un numero menor a 1