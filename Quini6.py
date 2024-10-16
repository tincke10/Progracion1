# Quini 6 Game

import random

# Genero numeros aleatoriamente
def generate_drawn_numbers():
    return random.sample(range(1, 61), 6)

def quini6_game(player_numbers, drawn_numbers):
    # Cuento las coincidencias
    matches = len(set(player_numbers) & set(drawn_numbers))
    
    # Determino segun  el numero de coincidencias
    if matches == 6:
        prize = "Premio mayor"
    elif matches == 5:
        prize = "Premio intermedio"
    elif matches == 4:
        prize = "Premio menor"
    else:
        prize = "Sin premio"

    return matches, prize

# solicito los numeros del jugador
player_numbers = []
print("Ingrese 6 números entre 1 y 60:")
for _ in range(6):
    num = int(input("Número: "))
    player_numbers.append(num)

# sorteo los numeros
drawn_numbers = generate_drawn_numbers()
print(f"Números sorteados: {drawn_numbers}")

# muestro el resultado al jugador
matches, prize = quini6_game(player_numbers, drawn_numbers)
print(f"Coincidencias: {matches}, Premio: {prize}")