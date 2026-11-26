with open("coches.csv", "r", encoding="utf-8") as fichero:
    lista_coches = []
    dict_marcas = {}
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

        # CREAIÓN DEL DICCIONARIO A PARTIR DEL FICHERO
        if marca in dict_marcas:
            dict_modelos = dict_marcas[marca]
            dict_modelos[modelo] = (precio, direccion)
        else:
            dict_marcas[marca] = {modelo: (precio, direccion)}

        # CREAIÓN DE LA LISTA A PARTIR DEL FICHERO

        #marca, modelo, precio, direccion = coche
        coche = (marca, modelo, precio*1.10, direccion)
        lista_coches.append(coche)
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
print(lista_coches)
"""
[
    ('BMW', '320', 66000.0, '-'), 
    ('Audi', 'A8', 99000.0, 'Calle del Míngüezañitela, 34'), 
    ('Tesla', 'Y', 159500.0, '-'), 
    ('Aston Martin', 'DB8', 132000.0, 'Calle del Pez, 34'), 
    ('BMW', '420', 88000.0, '-')
]
"""
print(dict_marcas)
"""
{
    'BMW': {
            '320': (60000, '-'), 
            '420': (80000, '-')
            }, 
    'Audi': {'A8': (90000, 'Calle del Míngüezañitela, 34')}, 
    'Tesla': {'Y': (145000, '-')}, 
    'Aston Martin': {'DB8': (120000, 'Calle del Pez, 34')}
}
"""
