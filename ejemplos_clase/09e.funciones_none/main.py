import funciones 

persona = funciones.crear_persona()
funciones.print_persona(persona)

# ¿Qué ocurre si intento obtener el return de una función que no devuelve nada?
retorno = funciones.print_persona(persona)
print(retorno)


# Errores comunes
lista = []
lista = lista.append("Hola")    # Mi lista acaba de convertirse en un None, append no devuelve nada porque las listas son mutables
print(lista)

print("-----------")
print("-----------")
print("-----------")

x = funciones.decir("HOLds fdsfdsfdsfdsA")
print(x)

suma = funciones.sumar(2, 3)
print("el reuslado de la suma", suma)