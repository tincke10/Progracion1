# Realice un programa que ingresando 10 numeros,  muestre solamente los numeros que se encuentran en posiciones pares.


numeros = []

# Ingresar 10 números
for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

# Mostrar los números en posiciones pares
for i in range(0, 10, 2):
    print(numeros[i])