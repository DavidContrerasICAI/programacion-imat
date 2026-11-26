d_marcas = {"BMW": {"320": [40, 41, 39]} }

d_modelos = d_marcas["BMW"]
precios = d_modelos["320"]
precio2 = precios[1]
print(precio2)

print(d_marcas["BMW"]["320"][1])

print(d_modelos["320"])
d_modelos["420"] = 70