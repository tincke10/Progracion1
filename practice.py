# Longitud de una cadena
cadena = "Hola, mundo"
print(len(cadena))  # 11

# Convertir a cadena
numero = 123
print(str(numero))  # "123"

# Dividir una cadena
frase = "Hola mundo"
print(frase.split())  # ['Hola', 'mundo']

# Unir una lista de cadenas
lista = ['Hola', 'mundo']
print(' '.join(lista))  # "Hola mundo"

# Reemplazar en una cadena
print(cadena.replace("mundo", "Python"))  # "Hola, Python"

# Eliminar espacios en blanco
cadena_con_espacios = "  Hola  "
print(cadena_con_espacios.strip())  # "Hola"

#----------------Manipulacion de Listas--------------

# Agregar elementos
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# Extender una lista
lista.extend([5, 6])
print(lista)  # [1, 2, 3, 4, 5, 6]

# Insertar en una posición específica
lista.insert(2, 'a')
print(lista)  # [1, 2, 'a', 3, 4, 5, 6]

# Eliminar un elemento
lista.remove('a')
print(lista)  # [1, 2, 3, 4, 5, 6]

# Eliminar y devolver el último elemento
print(lista.pop())  # 6
print(lista)  # [1, 2, 3, 4, 5]

# Ordenar una lista
lista.sort()
print(lista)  # [1, 2, 3, 4, 5]

# Invertir una lista
lista.reverse()
print(lista)  # [5, 4, 3, 2, 1]

# Índice de un elemento
print(lista.index(3))  # 2

# Contar ocurrencias
print(lista.count(3))  # 1

# -----------------Manipulacion de Diccionarios----------------

# Crear un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Obtener claves
print(diccionario.keys())  # dict_keys(['a', 'b', 'c'])

# Obtener valores
print(diccionario.values())  # dict_values([1, 2, 3])

# Obtener pares clave-valor
print(diccionario.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Obtener valor con clave
print(diccionario.get('a'))  # 1

# Actualizar un diccionario
diccionario.update({'d': 4})
print(diccionario)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Eliminar un elemento
print(diccionario.pop('a'))  # 1
print(diccionario)  # {'b': 2, 'c': 3, 'd': 4}

# -----------------Manipulacion de Conjuntos----------------

# Crear un conjunto
conjunto = {1, 2, 3}

# Agregar un elemento
conjunto.add(4)
print(conjunto)  # {1, 2, 3, 4}

# Eliminar un elemento
conjunto.remove(4)
print(conjunto)  # {1, 2, 3}

# Unión de conjuntos
conjunto2 = {3, 4, 5}
print(conjunto.union(conjunto2))  # {1, 2, 3, 4, 5}

# Intersección de conjuntos
print(conjunto.intersection(conjunto2))  # {3}

# Diferencia de conjuntos
print(conjunto.difference(conjunto2))  # {1, 2}


# -----------------Manejo de Archivos----------------

# Escribir en un archivo
with open('archivo.txt', 'w') as f:
    f.write('Hola, mundo')

# Leer de un archivo
with open('archivo.txt', 'r') as f:
    contenido = f.read()
    print(contenido)  # "Hola, mundo"
    
    
# ----------------Funciones Matematicas y Estadisticas----------------

import math
import statistics

# Suma
print(sum([1, 2, 3]))  # 6

# Mínimo y máximo
print(min([1, 2, 3]))  # 1
print(max([1, 2, 3]))  # 3

# Valor absoluto
print(abs(-5))  # 5

# Redondear
print(round(3.14159, 2))  # 3.14

# Funciones del módulo math
print(math.sqrt(16))  # 4.0

# Funciones del módulo statistics
print(statistics.mean([1, 2, 3]))  # 2

#----------------Control de Flujo----------------

# Condicionales
x = 10
if x > 5:
    print("Mayor que 5")
elif x == 5:
    print("Igual a 5")
else:
    print("Menor que 5")

# Bucles for
for i in range(5):
    print(i)  # 0 1 2 3 4

# Bucles while
i = 0
while i < 5:
    print(i)  # 0 1 2 3 4
    i += 1

# Break y continue
for i in range(5):
    if i == 3:
        break
    print(i)  # 0 1 2

for i in range(5):
    if i == 3:
        continue
    print(i)  # 0 1 2 4
    
    
#-----------------Manejo de Excepciones----------------

try:
    x = 1 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto siempre se ejecuta")

# Lanzar una excepción
raise ValueError("Un error ocurrió")

#-----------Programacion Funcional--------------
# Map
print(list(map(lambda x: x * 2, [1, 2, 3])))  # [2, 4, 6]

# Filter
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # [2, 4]

# Reduce
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # 10

# Listas por comprensión

# List comprehension
print([x * 2 for x in range(5)])  # [0, 2, 4, 6, 8]

# Dictionary comprehension
print({x: x * 2 for x in range(5)})  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Set comprehension
print({x * 2 for x in range(5)})  # {0, 2, 4, 6, 8}

# ---------------Manejo de Fechas y Tiempo ----------------

import datetime
import time

# Fecha y hora actuales
print(datetime.datetime.now())

# Esperar 2 segundos
time.sleep(2)
print("Han pasado 2 segundos")

# ---------- Manejo de Modulos y Paquetes ---------------

# Importar un módulo
import math
print(math.pi)  # 3.141592653589793

# Importar una función específica
from math import sqrt
print(sqrt(16))  # 4.0

# Importar con alias
import math as m
print(m.pi)  # 3.141592653589793