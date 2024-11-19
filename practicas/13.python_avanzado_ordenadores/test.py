import funciones as f

COLOR_VERDE = "\033[1;32m"
COLOR_ROJO = "\033[1;31m"
COLOR_DEFECTO = "\033[0m"

OK = COLOR_VERDE + "OK" + COLOR_DEFECTO
ERROR = COLOR_ROJO + "ERROR" + COLOR_DEFECTO

print("Ejecutando tests....")

try:
    print("- Función inicializar_datos(): ", end = "") 
    f.inicializar_datos()
    print(f"{OK}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función limpiar_datos(ordenador:str): ", end = "") 
    linea = "HC, Intel+ i7,16, HD1: 512Gb1"
    ordenador = f.limpiar_datos_tupla(linea)
    print(linea, end = " - ")
    if ordenador == ("HP", "i7", 16, 512) :
        print(f"{OK}")
    else:
        print(f"{ERROR}")
except Exception as error:
    print(f"{ERROR}")
    print("\t\t", error)

try:
    print("- Función normalizar_marcas(marca_entrada:str): ", end = "") 
    linea = "levo"
    marca = f.normalizar_marcas(linea)
    print(marca, "vs", linea, end = " - ")
    if marca == "Lenovo":
        print(f"{OK}")
    else:
        print(f"{ERROR}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función normalizar_cpu(cpu_entrada:str): ", end = "") 
    linea = "Intel PRO+ i8"
    cpu = f.normalizar_cpu(linea)
    print(cpu, "vs", linea, end = " - ")
    if cpu == "i7":
        print(f"{OK}")
    else:
        print(f"{ERROR}")
except Exception as error:
    print(f"{ERROR}")
    print(error)

try:
    print("- Función normalizar_hd(hd_entrada:str): ", end = "") 
    linea = "HD1: 512Gb1"   # --> 512
    #linea = "ssd64"
    hd = f.normalizar_hd(linea)
    print(hd, "vs", linea, end = " - ")
    if hd == "512":
        print(f"{OK}")
    else:
        print(f"{ERROR}")
except Exception as error:
    print(f"{ERROR}")
    print("\t\t", error)
    
print("Fin de los tests")