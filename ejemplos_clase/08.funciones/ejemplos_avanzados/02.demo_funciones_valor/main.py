import funciones as f

"""
Ejemplo de paso de variables por referencia (list) 
y por valor (int y str)
"""

if __name__ == "__main__":
    lista = [1, 2, 3]
    numero = 3
    cadena = "hola"
    f.transformar(lista, numero, cadena)
    print(lista, numero, cadena)