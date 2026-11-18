# https://pythontutor.com/visualize.html#mode=edit

a = 1
b = 2
s = "hola"
lista = []

def sumar(a:int, b:int) -> int:
    """
    Suma rara de dos números
    """
    a += 1
    s = "Adios"
    total = s + str(a) + "Hola"
    print("Variable a en sumar (local):", a)
    numero3 =  2 #random()
    numero4 = 4 #int(input("ewe"))

    suma_ejemplo = a + b + numero3 + numero4
    return suma_ejemplo


def gestionar_lista(opcion:int, valor:str)-> None:
    lista_ana = [1, 2, 3]
    for i in lista_ana:
        print(i)
    if opcion == 1:
        lista.append(valor)
    elif opcion == 2 and valor in lista:
        lista.remove(valor)
    elif opcion == 3:
        lista.insert(0, valor)

suma_de_david = sumar(a, b)
print("Variable a en main (global):", a)
print("Variable s en main (global):", s)
print("Resultado de suma rara:", suma)
print("Lista inicial:", lista)
gestionar_lista(1, "Uno")
gestionar_lista(1, "Dos")
gestionar_lista(1, "Tres")

gestionar_lista(2, "Dos")

gestionar_lista(3, "Cero")

print(lista)

print(lista_ana)

print("Esta línea dará error, por eso está la última:", suma_ejemplo)