import sys
import funciones as func

if __name__ == "__main__":
    dict_reemplazos = func.crear_diccionario_reemplazos("fichero")
    dict_ropas = func.crear_diccionario_ropa(dict_reemplazos)
    args = sys.argv
    if len(args) == 1:
        func.listar_ropa(dict_ropas)
    else:
        ropa = args[1]
        if ropa in dict_ropas:
            precio, _ = dict_ropas[ropa]
            print(f"{precio}€")
        else:
            print("No existe esa ropa")
