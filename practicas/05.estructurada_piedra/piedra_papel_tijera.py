import random

print()
PIEDRA = "P"
PAPEL = "p"
TIJERA = "T"
JUGADAS_MAX = 5

nombre_usuario = input("Nombre: ")

numero_partidas = int(input("¿Cuántas partidas quieres jugar [1, 5]? "))
while numero_partidas < 1 or numero_partidas > JUGADAS_MAX:
    numero_partidas = int(input("¿Cuántas partidas quieres jugar [1, 5]? "))

victorias_usuario = 0
victorias_maquina = 0
empates = 0

partida = 0
while partida < numero_partidas:
    # Lectura de la elección del usuario
    eleccion_usuario = input("\n¿[P]iedra, [p]apel o [T]ijera? ")
    while eleccion_usuario != PIEDRA and eleccion_usuario != PAPEL and eleccion_usuario != TIJERA:
        eleccion_usuario = input("¿[P]iedra, [p]apel o [T]ijera? ")
        
    print(f"USER: {eleccion_usuario}", end = "")

    # Generación aleatoria de la elección de la máquina
    aleatorio = random.randint(1, 3)

    if aleatorio == 1:
        eleccion_maquina = PIEDRA
    elif aleatorio == 2:
        eleccion_maquina = PAPEL
    else:
        eleccion_maquina = TIJERA

    print(f" - MÁQUINA: {eleccion_maquina} >>> ", end = "")

    usuario_win = eleccion_usuario == PIEDRA and eleccion_maquina == TIJERA \
                    or eleccion_usuario == PAPEL and eleccion_maquina == PIEDRA \
                    or eleccion_usuario == TIJERA and eleccion_maquina == PAPEL
    
    # Acumulación de resultados
    if eleccion_usuario == eleccion_maquina:
        empates += 1
        print("EMPATE")
    elif usuario_win:
        victorias_usuario += 1
        print("GANAS")
    else:
        victorias_maquina += 1
        print("PIERDES")
 
    partida += 1

# Acumulación de resultados
print("\nResultado Final".center(20))
print("="*20)
print(f"{nombre_usuario} {victorias_usuario} - {victorias_maquina} MÁQUINA")
print(f"Empates: {empates}")
