a_str = "-"
while not a_str.isdecimal():
    a_str = input("Número 1: ")
a = int(a_str)

b_str = "-"
while not b_str.isdecimal():
    b_str = input("Número 2: ")
b = int(b_str)

print(f"La suma de {a} y {b} es {a+b}")

