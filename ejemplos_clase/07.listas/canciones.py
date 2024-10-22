cantantes = ["Adele", "Ed Sheeran", "Beyoncé", "Bruno Mars", "Billie Eilish"]
print("CANTANTES")
for cantante in cantantes:
    print(cantante)

canciones_adele = ["Someone Like You", "Hello", "Rolling in the Deep", "Set Fire to the Rain", "Easy On Me"]

# Con la segunda lista de canciones se simula la entrada por teclado, por ejemplo, y se agrega una a una
canciones_ed = []
canciones_ed.append("Shape of You")
canciones_ed.append("Perfect")
canciones_ed.append("Thinking Out Loud")
canciones_ed.append("Castle on the Hill") 
canciones_ed.append("Bad Habits")

# Opción 1 
todas_canciones = [canciones_adele, canciones_ed]

# Opción 2
todas_canciones = []
todas_canciones.append(canciones_adele)
todas_canciones.append(canciones_ed)

for i in range(len(todas_canciones)):
    print(cantantes[i])
    print("=" * 30)
    canciones_de_un_cantante = todas_canciones[i]
    for cancion in canciones_de_un_cantante:
        print(" -", cancion)
    print()