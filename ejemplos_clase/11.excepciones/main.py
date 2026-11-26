index_str = input("Posición: ")
try:    
    print("....")
    index = int(index_str)
    print(index, "es un número")
    
    cadena = "hola"
    if index >= 0 and index < len(cadena):
        s = cadena[index]
        print(s)
except:
    print("El str introducido no es un número")
print("Terminé la evaluación")

