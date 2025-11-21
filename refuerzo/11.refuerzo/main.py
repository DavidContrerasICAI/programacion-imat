import funciones as f

if __name__ == "__main__":
    diccionario_coches = f.leer_coches()
    print("COCHES")
    for coche, cv in diccionario_coches.items():
        print(f"  - {coche}: {cv}")
    f.guardar_coches(diccionario_coches)
