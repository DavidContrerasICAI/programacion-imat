"""
Definición de Funciones
"""

def concatenar(a:str, b:str, c:str, d:str) -> str :
    cadena = a + b + c + d
    cadena = cadena.upper()
    return cadena

def is_primo(numero:int) -> bool:
    divisible = False
    i = 2
    while i < numero and not divisible:
        if numero % i == 0: 
            divisible = True
        i += 1

    return not divisible

def leer_numero() -> int:
    a = int(input("Numero: "))
    print("***estoy en leer_numero:", a)
    return a

def decir_hola(mensaje:str) -> None:
    a = "***" + mensaje + "***"
    print(a)

def sumar(a:int, b:int) -> int:
    suma = a + b
    return suma

"""
Programa Principal
"""
a = 12
b = 24
suma = sumar(2, 4)
print(suma)
print(sumar(1, 7))

decir_hola("Hola")

x = leer_numero()
print(x)
y = leer_numero()
print(sumar(x, y))

mi_cadena = concatenar("aa", "bb", "cc", "dd")
print(mi_cadena)

print("Es primo el 6?", is_primo(6))
print("Es primo el 7?", is_primo(7)) 