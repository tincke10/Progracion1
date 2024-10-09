# En una institución educativa, el director quiere organizar las celebraciones de cumpleaños de los estudiantes de manera más eficiente. Para ello, necesita saber en qué meses del año se concentran la mayor cantidad de cumpleaños y, por el contrario, en qué meses no hay cumpleaños de estudiantes. Con esta información, el director podrá planificar mejor las actividades, agrupando las celebraciones en los meses más concurridos y evitando las festividades en aquellos meses donde no hay ningún cumpleaños. Como encargado del sistema de información de la institución, se te ha solicitado desarrollar un programa que permita registrar el mes de cumpleaños de cada estudiante. Además, el programa debe ser capaz de: Determinar cuál o cuáles son los meses con mayor cantidad de cumpleaños. Identificar los meses en los que no se registren cumpleaños de ningún estudiante.

def register_birthdays():
    birthdays = {}
    for month in range(1, 13):
        birthdays[month] = 0
    
    while True:
        try:
            month = int(input("Ingrese el mes de cumpleaños del estudiante (1-12) o 0 para terminar: "))
            if month == 0:
                break
            if 1 <= month <= 12:
                birthdays[month] += 1
            else:
                print("Mes inválido. Por favor, ingrese un número entre 1 y 12.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    
    return birthdays

def find_max_birthdays(birthdays):
    max_birthdays = max(birthdays.values())
    max_months = [month for month, count in birthdays.items() if count == max_birthdays]
    return max_months, max_birthdays


def find_no_birthdays(birthdays):
    no_birthdays = [month for month, count in birthdays.items() if count == 0]
    return no_birthdays

def main():
    birthdays = register_birthdays()
    max_months, max_birthdays = find_max_birthdays(birthdays)
    no_birthdays = find_no_birthdays(birthdays)
    
    print(f"El/Los mes(es) con más cumpleaños ({max_birthdays}): {', '.join(map(str, max_months))}")
    if no_birthdays:
        print(f"El/Los mes(es) sin cumpleaños: {', '.join(map(str, no_birthdays))}")
    else:
        print("Todos los meses tienen al menos un cumpleaños.")

if __name__ == "__main__":
    main()