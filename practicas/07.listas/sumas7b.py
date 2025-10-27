import matplotlib.pyplot as plt

X_MIN = -5
X_MAX = 5

eje_x = []
f_x = []
g_x = []

for x in range(X_MIN, X_MAX):
    eje_x.append(x)
    for ticks in range(1, 4):
        eje_x.append(x + ticks/4)

eje_x.append(X_MAX)

for x in eje_x:
    f_x.append(x**2 - 3*x + 5)
         
for x in eje_x:
    g_x.append(-5*x**2 + 4*x + 25)

plt.plot(eje_x, f_x)
plt.plot(eje_x, g_x)
plt.show()

print("Tabla de puntos de la función f(x): (x, y)")

cont = 0
for x in eje_x:
    print(f"({x}, {f_x[cont]})")
    cont += 1