NEGRITA = "\033[1m"
DEFECTO = "\033[0m"
INVERSO = "\033[7m"
SUBRAYADO = "\033[4m"

def N(s:str)->str:
    return NEGRITA + s + DEFECTO

def I(s:str)->str:
    return INVERSO + s + DEFECTO

def S(s:str)->str:
    return SUBRAYADO + s + DEFECTO
