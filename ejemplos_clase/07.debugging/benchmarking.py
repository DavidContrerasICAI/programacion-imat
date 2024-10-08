import matplotlib.pyplot as plt
import timeit

plt.figure(figsize=(8, 6))

cadena = ""
i = 0
t0 = timeit.default_timer()
while i < 10**5:
    cadena += "A"
    i += 1
t1 = timeit.default_timer()
print(t1-t0)
plt.bar(1, t1-t0, label = "10^5")

cadena = ""
i = 0
t0 = timeit.default_timer()
while i < 10**6:
    cadena += "A"
    i += 1
t1 = timeit.default_timer()
print(t1-t0)
plt.bar(2, t1-t0, label = "10^6")


cadena = ""
i = 0
t0 = timeit.default_timer()
while i < 10**7:
    cadena += "A"
    i += 1
t1 = timeit.default_timer()
print(t1-t0)
plt.bar(3, t1-t0, label = "10^7")
plt.legend()
plt.show()


