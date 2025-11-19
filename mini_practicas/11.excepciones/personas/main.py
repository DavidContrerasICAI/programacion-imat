import funciones as func

if __name__ == "__main__":
    valores_test = ["Manuel, 22", "luis, 33", "Ana,18", "Marta, 16", "Federico, ??"]
    for valor in valores_test:
        try:
            resultado = func.crear_persona(valor)
            print(resultado)
        except ValueError as error:
            print("Error:", error)

