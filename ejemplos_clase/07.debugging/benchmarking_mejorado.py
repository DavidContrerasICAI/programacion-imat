import matplotlib.pyplot as plt
import timeit

plt.figure(figsize=(8, 6))

NUM_INICIAL = 3
ejecuciones = NUM_INICIAL
while ejecuciones < NUM_INICIAL + 3:
    cadena = ""
    i = 0
    t0 = timeit.default_timer()
    while i < 10**ejecuciones:
        cadena += "A"*10
        i += 1
    t1 = timeit.default_timer()
    tiempo = (t1-t0)*1000
    print(f"{10**ejecuciones:}={tiempo:.2f}")
    plt.bar(ejecuciones-(NUM_INICIAL-1), t1-t0, label = f"10^{ejecuciones}")
    ejecuciones += 1

plt.xlabel("Experimento")
plt.ylabel("Tiempo (ms)")
plt.legend()
plt.show()


