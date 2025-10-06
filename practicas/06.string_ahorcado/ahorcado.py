VERDE = "\033[1;42m"
ROJO = "\033[1;41m"
DEFECTO = "\033[0m"

DIBUJO_0 = """
  +---+
  |   |
      |
      |
      |
      |
========="""
DIBUJO_1 = """
  +---+
  |   |
  O   |
      |
      |
      |
========="""
DIBUJO_2 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
========="""
DIBUJO_3 = """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========="""
DIBUJO_4 = """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========="""
DIBUJO_5 = """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""

titulo = """
\t\t\t\t██╗  ██╗ █████╗ ███╗   ██╗ ██████╗  ███╗   ███╗ █████╗ ███╗   ██╗
\t\t\t\t██║  ██║██╔══██╗████╗  ██║██╔════╝  ████╗ ████║██╔══██╗████╗  ██║
\t\t\t\t███████║███████║██╔██╗ ██║██║  ███╗ ██╔████╔██║███████║██╔██╗ ██║
\t\t\t\t██╔══██║██╔══██║██║╚██╗██║██║   ██║ ██║╚██╔╝██║██╔══██║██║╚██╗██║
\t\t\t\t██║  ██║██║  ██║██║ ╚████║╚██████╔╝ ██║ ╚═╝ ██║██║  ██║██║ ╚████║
\t\t\t\t╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

PALABRA_OBJETIVO = "SALON"
INTENTOS_MAX = 5

letras_ok = ""
letras_ko = ""
contador_letras = 0

print(titulo)

intentos = 0
while intentos < INTENTOS_MAX and contador_letras != 5:

    if intentos == 0:
        dibujo = DIBUJO_0
    elif intentos == 1:
        dibujo = DIBUJO_1
    elif intentos == 2:
        dibujo = DIBUJO_2
    elif intentos == 3:
        dibujo = DIBUJO_3
    elif intentos == 4:
        dibujo = DIBUJO_4
    elif intentos == 5:
        dibujo = DIBUJO_5

    print(f"{dibujo} {intentos}\n")

    palabra = ""
    while len(palabra) != len(PALABRA_OBJETIVO):
        palabra = input("## Palabra: ")
    palabra = palabra.upper()
    contador_letras = 0
    print()
    i = 0
    while i < len(PALABRA_OBJETIVO):
        if palabra[i] == PALABRA_OBJETIVO[i]:
            color = VERDE
            contador_letras += 1
            letras_ok += palabra[i]
        else:
            color = ROJO
            existe = False

        print(f"{color} {palabra[i]} {DEFECTO} ", end = "")  
        i += 1

    print()
    intentos += 1

print()
if contador_letras == 5:
    print("¡¡¡ GANASTE !!!")
else:
    print(f"¡¡¡ AHORCADO !!!\nPalabra a acertar: {PALABRA_OBJETIVO}")