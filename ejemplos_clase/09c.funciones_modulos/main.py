import funciones

"""
Desde el módulo MAIN como os podéis imaginar, no tenemos 
visibilidad sobre las variables de OTRO MÓDULO
"""
# Estas variables solo existen en el MAIN
a = 1
b = 2
s = "hola"
lista = []

print("Variable a en main:", a)
print("Variable s en main:", s)

suma_de_david = funciones.sumar(a, b)
print("Resultado de suma rara:", suma_de_david)

print("Lista inicial:", lista)
funciones.gestionar_lista(lista, 1, "Uno")
funciones.gestionar_lista(lista, 1, "Dos")
funciones.gestionar_lista(lista, 1, "Tres")

funciones.gestionar_lista(lista, 2, "Dos")

funciones.gestionar_lista(lista, 3, "Cero")

# Reutilizamos el código de la función para trabajar con otra lista
otra_lista = []
funciones.gestionar_lista(otra_lista, 1, "1")
funciones.gestionar_lista(otra_lista, 1, "2")
funciones.gestionar_lista(otra_lista, 1, "3")

print(lista)
print("-"*20)
print(otra_lista)