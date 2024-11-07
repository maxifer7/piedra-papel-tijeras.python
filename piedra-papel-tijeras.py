nombre1 = input("Nombre del jugador 1: ")
nombre2 = input("Nombre del jugador 2: ")

print("Hola, ", nombre1)
jugador1 = input("Qué elijes? Piedra, papel o tijeras?: ")
print("Hola, ", nombre2)
jugador2 = input("Qué elijes? Piedra, papel o tijeras?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate!!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", nombre1)
else:
    print("Ha ganado:", nombre2)