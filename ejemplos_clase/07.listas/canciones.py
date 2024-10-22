cantantes = ["Adele", "Ed Sheeran", "Beyoncé", "Bruno Mars", "Billie Eilish"]
print("CANTANTES")
for cantante in cantantes:
    print(cantante)

canciones_adele = ["Someone Like You", "Hello", "Rolling in the Deep", "Set Fire to the Rain", 
                        "Easy On Me"]
canciones_ed = ["Shape of You", "Perfect", "Thinking Out Loud", "Castle on the Hill", "Bad Habits"]

todas_canciones = [canciones_adele, canciones_ed]

for i in range(len(todas_canciones)):
    print(cantantes[i])
    print("=" * 30)
    canciones_de_un_cantante = todas_canciones[i]
    for cancion in canciones_de_un_cantante:
        print(" -", cancion)
    print()