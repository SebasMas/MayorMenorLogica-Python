#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

mayor = a

if mayor > b:
    mayor = a
else:
    mayor = b
if mayor > c:
    mayor = b
else: 
    mayor = c

print("El numero mayor es: ", mayor)

#Funcion que solicite n numeros para ingresar y después retorne el mayor de ellos
x = []
cantidad = int(input("Cuantos numeros: "))
for i in range(cantidad):
    numero = int(input("Ingrese un numero: "))
    x = x + [numero]
mayor = x[0]
for numero in x:
    if numero > mayor:
        mayor = numero
print(mayor)


#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

if a > b:
    print("El número mayor es: ", a)
else:
    print("El número mayor es: ", b)