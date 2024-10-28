import random

numeros = []
for x in range(20):
    numeros.append(random.randint(1, 10))

numero_objetivo = random.randint(1, 10)

print(f"Lista: {numeros}")
print(f"Número objetivo: {numero_objetivo}")
for i in range(len(numeros)-1):
    for j in range(i+1, len(numeros)):
        if numeros[i] + numeros[j] == numero_objetivo:
            print(f"{numeros[i]} + {numeros[j]}")