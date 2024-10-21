# Ingresar una matriz de nxn, donde n no supera la decena y determinar si se trata de una matriz identidad.

# La entrada son los valores de la matriz cargando fila 1 columna 1, fila 1 columna 2, fila 1 columna n, y luego fila 2 columna 1, fila 2 columna 2, fila 2 columna n, y asi sucesivamente hasta fila n columna 1, fila n columna 2, fila n columna n

# La salida debe ser un texto que indique "Es Matriz Identidad", "No Es Matriz Identidad"

def es_matriz_identidad(matriz, n):
    for i in range(n):
        for j in range(n):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True 

def main():
    n = int(input())
    if n > 10:
        print("Error: N no puede ser mayor a 10")
        return

    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)

    if es_matriz_identidad(matriz, n):
        print("Es Matriz Identidad")
    else:
        print("No es Matriz Identidad")

if __name__ == "__main__":
    main()