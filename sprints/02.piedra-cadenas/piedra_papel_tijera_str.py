import random

PIEDRA = "P"
PAPEL = "p"
TIJERA = "T"

ELEMENTOS = PIEDRA + PAPEL + TIJERA
LOGICA_JUEGO = (PIEDRA + TIJERA) + (TIJERA + PAPEL) + (PAPEL + PIEDRA)  # "PTTppP" Determina las combinaciones ganadoras: P-T, T-p, p-P

JUGADAS_MAX = 5

NUMERO_DIGITOS_RESULTADO = 3
INDEX_RESULTADO_VICTORIA = 0
INDEX_RESULTADO_EMPATE = NUMERO_DIGITOS_RESULTADO
INDEX_RESULTADO_DERROTA = NUMERO_DIGITOS_RESULTADO * 2
resultado = "000000000"   # 000 (Ganadas) 000 (Empatadas) 000 (Perdidas)

nombre_usuario = input("Nombre: ")

numero_partidas = int(input("¿Cuántas partidas quieres jugar [1, 5]? "))
while numero_partidas < 1 or numero_partidas > JUGADAS_MAX:
    numero_partidas = int(input("¿Cuántas partidas quieres jugar [1, 5]? "))

partida = 0
while partida < numero_partidas:
    # Lectura de la elección del usuario
    eleccion_ok = False
    while not eleccion_ok:
        eleccion_usuario = input("\n¿[P]iedra, [p]apel o [T]ijera? ")
        i = 0
        while i < len(ELEMENTOS) and not eleccion_ok:
            if eleccion_usuario == ELEMENTOS[i]:
                eleccion_ok = True
            i += 1
            
    print(f"USER: {eleccion_usuario}", end = "")

    # Generación aleatoria de la elección de la máquina
    aleatorio = random.randint(0, 2)
    eleccion_maquina = ELEMENTOS[aleatorio]

    print(f" - MÁQUINA: {eleccion_maquina} >>> ", end = "")

    indice_juego = 0
    usuario_win = False
    while indice_juego < 3 and not usuario_win:
        usuario_win = LOGICA_JUEGO[indice_juego*2] == eleccion_usuario \
                        and LOGICA_JUEGO[indice_juego*2+1] == eleccion_maquina
        indice_juego += 1
        
    # Acumulación de resultados
    indice_resultado = 0
    if eleccion_usuario == eleccion_maquina:
        indice_resultado = INDEX_RESULTADO_EMPATE
        print("EMPATE")
    elif usuario_win:
        indice_resultado = INDEX_RESULTADO_VICTORIA
        print("GANAS")
    else:
        indice_resultado = INDEX_RESULTADO_DERROTA
        print("PIERDES")

    # Procesado Binario - Decimal
    numero_binario_str = resultado[indice_resultado:indice_resultado+NUMERO_DIGITOS_RESULTADO]
    numero = int(numero_binario_str, 2) + 1
    numero_binario = bin(numero)
    numero_binario = numero_binario[2:]
    while len(numero_binario) != NUMERO_DIGITOS_RESULTADO:
        numero_binario = "0" + numero_binario
    
    # Actualización de la cadena
    i = 0
    resultado_actualizado = ""
    while i < len(resultado):
        if i == indice_resultado:
            resultado_actualizado += numero_binario
        else:
            resultado_actualizado += resultado[i:i+NUMERO_DIGITOS_RESULTADO]
        i += NUMERO_DIGITOS_RESULTADO

    resultado = resultado_actualizado
    partida += 1
    
victorias_usuario = int(resultado[INDEX_RESULTADO_VICTORIA:INDEX_RESULTADO_VICTORIA+NUMERO_DIGITOS_RESULTADO], 2)
empates = int(resultado[INDEX_RESULTADO_EMPATE:INDEX_RESULTADO_EMPATE+NUMERO_DIGITOS_RESULTADO], 2)
victorias_maquina = int(resultado[INDEX_RESULTADO_DERROTA:INDEX_RESULTADO_DERROTA+NUMERO_DIGITOS_RESULTADO], 2)
    
# Acumulación de resultados
print("\nResultado Final".center(20))
print("="*20)
print(f"{nombre_usuario} {victorias_usuario} - {victorias_maquina} MÁQUINA")
print(f"Empates: {empates}")