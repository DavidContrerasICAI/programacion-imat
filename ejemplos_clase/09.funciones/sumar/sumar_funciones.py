def leer_numero(ordinal:int) -> int:
    a_str = "-"
    while not a_str.isdecimal():
        a_str = input(f"Número {ordinal}: ")
    numero = int(a_str)
    return numero

a = leer_numero(1)
b = leer_numero(2)
print(f"La suma de {a} y {b} es {a+b}")
