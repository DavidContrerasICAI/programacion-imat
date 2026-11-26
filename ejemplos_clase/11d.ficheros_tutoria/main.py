PRECIO_MIN = 70000 


fichero_salida = open("coches_caros.txt", "w", encoding="utf-8")

with open("coches.csv", "r", encoding="utf-8") as fichero:  
    coches = []
    cabecera = fichero.readline()
    for linea in fichero:
        campos = linea.split(";")
        
        if len(campos) == 4:
            marca, modelo, precio, direccion = campos
        else:
            marca, modelo, precio = campos
            direccion = "-"

        marca = marca.strip()
        modelo = modelo.strip()
        precio = int(precio)
        direccion = direccion.strip()

        if precio > PRECIO_MIN:
            fichero_salida.write(f"{marca} {modelo}: {precio}€\n")

        coche = (marca, modelo, precio, direccion)
        
        #marca, modelo, precio, direccion = coche
        #coche = marca, modelo, precio*1.10, direccion 
        coches.append(coche)
        """
        if linea.count(";") == 3:
            direccion = campos[3]
        else:
            direccion = "-"

        try:
            direccion = campos[3]
        except IndexError as error:
            direccion = "-"
        """
    print(coches)

fichero_salida.close()