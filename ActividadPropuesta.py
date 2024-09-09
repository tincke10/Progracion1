# La profesora Soledad necesita calificar al grupo por su exposición en el TRABAJO FINAL:
# La escala de calificaciones es del 0 al 10.
# • Si la nota del T. FINAL es menor que 6 debe poner el siguiente mensaje: “Debe recuperar para REGULARIZAR”.
# • Si la nota del T. FINAL es mayor o igual que 8 debe poner el siguiente mensaje: “Felicitaciones PROMOCIONÓ”.
# • Si la nota del T. FINAL está entre 5 y 8, debemos saber la nota del Trabajo Prácticos y si esta es:
# ✓ Menor a 6, debe poner el siguiente mensaje: “Quedó LIBRE”.
# ✓ 6 , 7 u 8 debe poner el siguiente mensaje: “REGULARIZÓ”.
# ✓ Mayor o igual a 9, debe poner el siguiente mensaje: “Debe rendir un COLOQ

def main():
    # Ingreso de datos
    notaTrabajoFinal = int(input("Ingrese la nota del Trabajo Final: "))
    notaTrabajoPractico = int(input("Ingrese la nota del Trabajo Práctico: "))

    # Proceso
    if notaTrabajoFinal < 6:
        print("Debe recuperar para REGULARIZAR")
    elif notaTrabajoFinal >= 8:
        print("Felicitaciones PROMOCIONÓ")
    else: 
        if notaTrabajoPractico < 6:
            print("Quedó LIBRE")
        elif notaTrabajoPractico >= 6 and notaTrabajoPractico <= 8:
            print("REGULARIZÓ")
        elif notaTrabajoPractico >= 9:
            print("Debe rendir un COLOQUIO")
            
main()