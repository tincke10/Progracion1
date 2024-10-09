#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


# nombre = input ("Ingrese su nombre: ")

# print (nombre.upper(), "tiene", len(nombre), "letras")


#--------------------------------------------------------------------------------------
#Escribir un programa que ingrese dos cadenas y determine cual es la mas larga

# cadena1 = input ("Digite una cadena: ")
# cadena2 = input ("Digite otra cadena: ")

# if len(cadena1) > len(cadena2):
#     print ("es la cadena más larga es:", cadena1)
# elif len(cadena1) < len(cadena2):
#     print ("es la cadena más larga es:", cadena2)
# else:
#     print ("Ambas cadenas son iguales en  longitud")
    
    
    
# --------------------------------------------------------------------------------------

#Dado un numero entero N de 12 cifras ingresado por el usuario, elimine de el todos los digitos mayores a 5. Imprima el numero resultante


numero = input("Digite un número de 12 cifras: ")

if len(numero) != 12 or not numero.isdigit():
    print("El número no tiene 12 cifras o contiene caracteres no numéricos")
else:
    numero = "".join([i for i in numero if int(i) <= 5])
    print("Los numeros son:", numero)
    
