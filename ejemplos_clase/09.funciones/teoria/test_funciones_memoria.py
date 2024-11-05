def funcion_tipos_basicos(a:int) -> None:
    a += 1
    print("Valor de a en función:", a)

def funcion_tipos_complejos(x:list) -> None:
    x.append("B")

a = 1
print(a)
funcion_tipos_basicos(a)
print("Valor de a en el programa principal:", a)

lista = []
lista.append("A")
funcion_tipos_complejos(lista)
print(lista)
lista2 = lista
lista3 = lista
lista2.clear()
lista3.append("C")
print(lista)