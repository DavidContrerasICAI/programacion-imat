a = 1
b = "a"

def funcion1() -> None:
    a = 2
    b = "b"
    print(f"Valores de a={a} y b={b} en la funcion1") 

def funcion2() -> None:
    global a, b
    a = 2
    b = "b"
    print(f"Valores de a={a} y b={b} en la funcion2") 

def funcion3(x:int) -> int:
    a = 3
    b = "c"
    print(f"Valores de a={a} y b={b} en la funcion3") 
    return a

funcion1()
print(f"Valores de a={a} y b={b} en el programa principal\n") 

funcion2()
print(f"Valores de a={a} y b={b} en el programa principal\n") 

a = funcion3(a)
print(f"Valores de a={a} y b={b} en el programa principal") 