# Dada la cantidad de equipos de futbol por el usuario, solicitar que ingrese nombre y cantidad de puntos por equipo, para luego devolver como output quien fue el ganador del torneo teniendo en cuenta obviamente cual es el equipo que mas puntos hizo

# Dada la cantidad de equipos de futbol por el usuario, solicitar que ingrese nombre y cantidad de puntos por equipo, para luego devolver como output quien fue el ganador del torneo teniendo en cuenta obviamente cual es el equipo que mas puntos hizo

def main():
    num_teams = int(input("Ingrese la cantidad de equipos: "))
    max_points = -1
    winning_team = ""

    for _ in range(num_teams):
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        puntos_equipo = int(input("Ingrese la cantidad de puntos del equipo: "))
        
        if puntos_equipo > max_points:
            max_points = puntos_equipo
            winning_team = nombre_equipo

    print("El equipo ganador es: ", winning_team, "Con", max_points, "puntos")

main()