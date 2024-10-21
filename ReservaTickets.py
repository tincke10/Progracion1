# Genera un sistema de ticket donde se utilize matrices para almacenar los asientos de un teatro. 
# El sistema debe permitir la reserva de asientos por usuarios el cual puede reservar los que desee.
# cada vez que reserva  uno se le debe preguntar si quiere reservar otro y cuando sea false se le debe mostrar a siguiente usuario los lugares reservados y los disponibles. 
# El sistema debe mostrar el estado de los asientos en todo momento.

def mostrar_asientos(asientos):
    for fila in asientos:
        print(" ".join(fila))
    print()

def reservar_asiento(asientos):
    while True:
        try:
            fila = int(input("Ingrese el número de fila (0-10): "))
            columna = int(input("Ingrese el número de columna (0-10): "))
            if asientos[fila][columna] == 'O':
                asientos[fila][columna] = 'X'
                print("Asiento reservado con éxito.")
            else:
                print("Este asiento se encuentra reservado.")
        except (IndexError, ValueError):
            print("Error. Ingrese un número de fila y columna válidos.")
        
        mostrar_asientos(asientos)
        
        otro = input("¿Desea reservar otro asiento? (s/n): ").lower()
        if otro != 's':
            break

def main():
    filas = 5
    columnas = 4
    asientos = [['O' for _ in range(columnas)] for _ in range(filas)]

    while True:
        print("Estado actual de los asientos:")
        mostrar_asientos(asientos)
        
        reservar_asiento(asientos)
        
        otro_usuario = input("¿Se terminara la sesion y otro cliente tendra el turno de reserva, estas seguro que deseas salir? (s/n): ").lower()
        if otro_usuario != 's':
            break

if __name__ == "__main__":
    main()