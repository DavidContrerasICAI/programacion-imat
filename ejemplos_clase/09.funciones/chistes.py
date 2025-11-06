import pyjokes

def contar_chistes(numero:int = 1):
    print(f"Contando {numero} chistes...")
    for i in range(numero):
        print(f"  - #{i+1}: {pyjokes.get_joke()}")


contar_chistes()
contar_chistes(5)
contar_chistes(3)
