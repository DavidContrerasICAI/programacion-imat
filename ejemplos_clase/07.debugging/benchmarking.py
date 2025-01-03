import matplotlib.pyplot as plt
import timeit

plt.figure(figsize=(8, 6))

NUM_INICIAL = 5
ejecuciones = NUM_INICIAL
while ejecuciones < 8:
    cadena = ""
    i = 0
    t0 = timeit.default_timer()
    while i < 10**ejecuciones:
        cadena += "A"
        i += 1
    t1 = timeit.default_timer()
    print(t1-t0)
    plt.bar(ejecuciones-(NUM_INICIAL-1), t1-t0, label = f"10^{ejecuciones}")
    ejecuciones += 1

plt.legend()
plt.show()


