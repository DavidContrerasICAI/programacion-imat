def inicializar_datos(source:int = 0) -> list:
    """
    Carga la información en el programa, según el argumento que se envíe.
    Si no se pasa nada, se leerá del fichero. Si no, se cargará con valores por defecto.
    
    Return:
        ordenadores (list): lista de todos los ordenadores leídos.
    """
    ordenadores = []
    if source == 1:
        ordenadores.append("DEL  ,i5,8,256GB")
        ordenadores.append("H, Intel i7,8,HD: 128")
        ordenadores.append("Lenvo  ,Intel i5,8,  200")
        ordenadores.append("DLL,  Inteli5,8,ssd256")
        ordenadores.append("Lnovo, i7,  8,512gb")
        ordenadores.append("HC, Intel+ i7,16, HD1: 512Gb1")
        ordenadores.append("DLL,  Inteli5,8,ssd6")
    else:
        with open("ordenadores.csv") as file:
            file.readline()
            for fila in file:
                ordenadores.append(fila.rstrip())

    return ordenadores

def limpiar_datos_objetos(ordenador:str) -> tuple[str, str, int, int]:
    """
    Convierte un string sucio a un a tupla procesada y limpia.

    Return:
        ordenador (tuple): una tupla con todos los valores 
                                inicializados como atributos.
    Raises:
        error (Exception): error general de cualquiera de las funciones de procesamiento de limpieza.

    Examples:
        "DLL,  Inteli5,8,ssd256" --> Ordenador("DELL", "i5", 8, 256)
    """
    try:
        ordenador = ordenador.replace(" ", "")
        valores_sucios = ordenador.split(",")
        #marca_dirty, cpu_dirty, ram_dirty, hd_dirty = ordenador.split(",")
        marca = normalizar_marcas(valores_sucios[0])
        cpu = normalizar_cpu(valores_sucios[1])
        ram = int(valores_sucios[2])
        hd = int(normalizar_hd(valores_sucios[3]))

        ordenador = (marca, cpu, ram, hd)   # se encapsula todo en una tupla
        return ordenador
    except Exception as error:
        raise error
    
def limpiar_datos_tupla(ordenador:str) -> tuple:
    try:
        ordenador = ordenador.replace(" ", "")
        valores_sucios = ordenador.split(",")
        #marca_dirty, cpu_dirty, ram_dirty, hd_dirty = ordenador.split(",")
        marca = normalizar_marcas(valores_sucios[0])
        cpu = normalizar_cpu(valores_sucios[1])
        ram = int(valores_sucios[2])
        hd = int(normalizar_hd(valores_sucios[3]))

        ordenador = (marca, cpu, ram, hd)
        return ordenador
    except Exception as error:
        raise error



def normalizar_marcas(marca_entrada:str) -> str:
    """
    Normaliza la marca recibida a una de las predefinidas.
    Si no encuentra ningún matching, se asignará a la primera: DELL.

    Returns:
        marca_normalizada (str): "DELL", "HP", "Lenovo"
    Examples:
        "DLL" --> "DELL"
    Raises:
        Ninguna exception
    """
    marcas_estandarizadas = ["DELL", "HP", "Lenovo"]
    marca_normalizada = ""

    if marca_entrada not in marcas_estandarizadas:
        coincidencias_lista = [] 
        for marca_estandarizada in marcas_estandarizadas:
            coincidencias = 0
            for letra in marca_entrada:
                coincidencias += marca_estandarizada.count(letra)
            coincidencias_lista.append(coincidencias)

        posicion = coincidencias_lista.index(max(coincidencias_lista))
    
        marca_normalizada = marcas_estandarizadas[posicion]
    else:
        marca_normalizada = marca_entrada

    return marca_normalizada

def normalizar_cpu(cpu_entrada:str) -> str:
    """
    Normmaliza la CPU a una válida según los modelos INTEL.
    Si se encuentra un número par, se convertirá al número inferior.

    Returns:
        cpu_normalizada  (str): i3, i5, i7

    Raises:
        ValueError: si no se ajusta al patrón de limpieza.
    
    Examples:
         i4 --> i3, Intel i7 --> i7, Inteli5 --> i5.
    """
    NUMERO_MAX_CARCACTERES = 2
    cpu_normalizada = ""
    for i in range(len(cpu_entrada)-1):
        if cpu_entrada[i] == "i" and cpu_entrada[i+1].isdecimal():   # Solo se toman 2 chars: i5
            num_procesador = int(cpu_entrada[i+1])
            if num_procesador >= 3 and num_procesador <=9:
                if num_procesador % 2 == 0:
                    num_procesador -= 1
                cpu_normalizada = cpu_entrada[i] + str(num_procesador)
    
    if len(cpu_normalizada) == NUMERO_MAX_CARCACTERES:
        return cpu_normalizada
    else:
        raise ValueError("La longitud de la CPU debe ser 2 digitos")

def normalizar_hd(hd_entrada:str) -> str:
    """
    Normaliza el HD a valores de números consecutivos de al menos 2 dígitos:

    Raises:
        ValueError
    Returns:
        hd_str  (int): 64, 128, 515...
    """
    hd_str = ""
    i = 0
    encontrado = False
    while i in range(len(hd_entrada)) and not encontrado:
        if hd_entrada[i].isdecimal():
            hd_str += hd_entrada[i]
        else:
            if len(hd_str) < 2:
                hd_str = ""
            else:
                encontrado = True
        i += 1
    
    if len(hd_str) < 2:   # Al menos dos dígitos consecutivos
        raise ValueError("El HD numérico debe tener al menos 2 dígitos: " + hd_entrada)
    else:
        return hd_str

