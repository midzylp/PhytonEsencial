#Aquí hablaremos de parametros, estos pueden ser recibidos por la función y se colocan en los parentesis

def funcionArgumentos(num1, num2):
    sum = num1 + num2
    print(f"La suma de {num1} + {num2} es igual a = {sum}")

funcionArgumentos(5,10)

#Usando strings deberia concatenar el texto, veamos

funcionArgumentos("Soy Luis", " Sánchez")

#Tambien es posible pasar parametros usando el nombre de los mismos y su valor, por ejemplo

funcionArgumentos(num1= 20, num2=30)