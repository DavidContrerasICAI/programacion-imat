import funciones as f
import sys

"""
Ejecución sin output:
> python main.py

Muestra los coches procesados:
> python main.py show

Ejecución con el nombre del coche:
> python main.py Toyota Corolla 1.8
Output: Toyota Corolla 1.8 (140CV) - Precio: 25000€ 

"""

if __name__ == "__main__":
    diccionario_coches = f.leer_coches()

    if len(sys.argv) == 2 and sys.argv[1] == "show":
        print("COCHES")
        for coche, carcateristicas in diccionario_coches.items():
            cv, precio = carcateristicas
            print(f"  - {coche}: {cv} ({precio}€)")
    else:
        if len(sys.argv) >= 2:
            nombre_coche = ""
            for parte in sys.argv[1:]:
                nombre_coche += parte + " "
            nombre_coche = nombre_coche.strip()
            if nombre_coche in diccionario_coches:
                cv, precio = diccionario_coches[nombre_coche]
                print(f"{nombre_coche} ({cv}CV) - Precio: {precio}€")

    f.guardar_coches(diccionario_coches)
