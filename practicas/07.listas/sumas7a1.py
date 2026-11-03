import random

numeros = []
i = 0
while i < 20:
    numeros.append(random.randint(1, 10))
    i += 1

numero_objetivo = random.randint(1, 10)

print(f"Lista: {numeros}")
print(f"Número objetivo: {numero_objetivo}")
i = 0
while i < len(numeros)-1:
    if numeros[i] + numeros[i+1] == numero_objetivo:
        print(f"{numeros[i]} + {numeros[i+1]}")
    i += 1