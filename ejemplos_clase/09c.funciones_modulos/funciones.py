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


def gestionar_lista(mi_lista:list, opcion:int, valor:str)-> None:
    """
    Gestiona la lista que recibe como parámetro.
    como se trabaja por referencia con la lista y no como valor,
    no es necesario hacer return 
    """
    if opcion == 1:
        mi_lista.append(valor)
    elif opcion == 2 and valor in mi_lista:
        mi_lista.remove(valor)
    elif opcion == 3:
        mi_lista.insert(0, valor)
