import random

fichero = open("palabras.txt", "r")
lista_palabras = fichero.readlines()
print(lista_palabras)
index = random.randint(0, len(lista_palabras)-1)
palabra = lista_palabras[index].strip()
print(palabra)
