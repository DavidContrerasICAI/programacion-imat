def concatenar1(a:str, b:str)->str:
    return a + " " + b

def concatenar2(a:str, b:str= "", c:str = "", d:str = "")->str:
    return a + " " + b + " " + c + " " + d

def concatenar3(*cadena)->str:
    x = ""
    for s in cadena:
       x += s + " "
    return x


resultado = concatenar1("Hola", "qué tal?") 
print(resultado)

resultado = concatenar2("Hola", "qué", "tal", "?") 
print(resultado)

resultado = concatenar3("Hola", "qué", "tal", "?", "Podríamos", "pasar", "infinitos", "parámetros", "...") 
print(resultado)


