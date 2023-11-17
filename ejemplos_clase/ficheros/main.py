import funciones 

if __name__ == "__main__":
    opc = input("Operacion:")
    if opc == "W":
        personas = funciones.escribir_fichero_texto() 
        print(personas)
    elif opc == "R":
        funciones.leer_fichero_texto()

    elif