outfit = ["Zapatos", "Pantalón", "Camiseta", "Bañador", "otra", "más"]
marca = ["Zara", "Pepe Jeans", "Scuffers", "Gucci"]
precio = [90, 60, 20, 15]

longitud_min = len(precio)
if len(outfit) < len(precio):
    longitud_min = len(outfit)

print(outfit)
print(precio)

i = 0
while i < longitud_min:
    if precio[i] < 50:
        print(f"{outfit[i]} ({marca[i]}): {precio[i]}€")
    i += 1