def init(mi_lista:list) -> list:
    mi_lista.append("aaaa")
    mi_lista.append("bbbb")
    return mi_lista

def add(my_list:list, cadena:str) -> list:
    my_list.append(cadena)
    return my_list

def show(l:list) -> None:
    print(l)
