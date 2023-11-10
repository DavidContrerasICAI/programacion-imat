def f1(a:int) -> int:
    a += 1
    return a

def f2(a:int) -> int:
    a += 2
    return a

def sumar(*numeros:tuple) -> int:
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

if __name__ == "__main__":
    x = sumar(1, 2, 3, 4, 5)
    print(x)
    a = None
    if a == None:
        a = 3