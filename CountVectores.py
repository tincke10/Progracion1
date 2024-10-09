# Realice un programa que ingresando 10 numeros,  se indique la cantidad total de numero pares ingresados, mostrando la posición de carga de cada uno.
# Entrada:
# 1
# 8
# 4
# 2
# 7
# 2
# 9
# 19
# 3
# 1

# Salida:
# Cantidad: 4
# Numeros: 
# 1
# 2
# 3
# 5

#---------------------Activida 1--------------------------------

def main():
    numeros = []
    cantidad_pares = 0
    posiciones_pares = []

    # Leer los números uno a uno porque el vpl no lo acepta en una linea
    for i in range(10):
        numero = int(input("Ingrese el número {}: ".format(i + 1)))
        numeros.append(numero)
        if numero % 2 == 0:
            cantidad_pares += 1
            posiciones_pares.append(i)

    print("Cantidad: {}".format(cantidad_pares))
    print("Numeros:")
    for posicion in posiciones_pares:
        print(posicion)

if __name__ == "__main__":
    main()