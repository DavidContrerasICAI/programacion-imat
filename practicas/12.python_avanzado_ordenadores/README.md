# Práctica 12. Python avanzado - Data cleaning

## Objetivo
Esta práctica pretende alcanzar los siguientes resultados de aprendizaje:
- Crear unidades de test.
- Aprender a limpiar los datos de entrada mediante métodos de la clase string.
- Tipificación de funciones.
- Ejecutar programas por consola con envío de parámetros al programa principal.
- Aprender a seguir unos interfaces dados.

## Enunciado

El objetivo del programa será mostrar todos los ordenadores que posee una tienda de informática de una marca. La entrada de la marca se realizará mediante los argumentos del programa main por medio de la consola. Si no somos capaces de conseguir esta funcionalidad, se pedirá la marca a buscar por teclado. 

En el siguiente caso se buscarán los ordenadores de la marca Lenovo.

```
(base) C:\Users\davidcb\Python\asignatura\practicas\12.python_avanzado>C:/Users/davidcb/Anaconda3/python.exe c:/Users/davidcb/Python/practicas/12.python_avanzado/main.py Lenovo 
``` 

Como se mencionaba, si no se alcanza a trabajar con parámetros del programa main, se podría pedir inicialmente la marca por teclado.


El programa trabajará con la información de ordenadores que almacena el fichero ordenadores.csv, el cual presenta el siguiente contenido:

```python
marca, modelo, ram, hd
DEL  ,i5,8,256GB
H, Intel i7,8,HD: 128
Lenvo  ,Intel i5,8,  200
DLL,  Inteli5,8,ssd256
Lnovo, i7,  8,512gb
HC, Intel+ i7,16, HD1: 512Gb1
DLL,  Inteli5,8,ssd6
```

Como se puede ver, la información de partida que se suministra es una lista donde cada elemento es un string con la información del ordenador separada por comas. Esta información está sucia, con muchas erratas y necesita ser limpiada para procesarla posteriormente, como se suele hacer en cualquier proceso de ingesta de datos no estructurados.

Deberemos realizar una serie de funciones que se encargarán de limpiar o normalizar datos de la lista. Los criterios de limpieza de los datos son los siguientes:
- Marca: el texto de la lista que no sea exactamente una marca se deberá normalizar/corregir con la marca que más se parezca a las tres que existen en la tienda: DELL, HP y Lenovo. La similitud con cada marca la haremos por la mayor coincidencia en el número de caracteres a las marcas reales. 
    + Ejemplo:
        - DEL posee 4 letras de DELL, 0 de HP y 2 de Lenovo, por lo que la normalizaremos/corregiremos por DELL.
        - H posee 0 letras de DELL, 1 de HP y 0 de Lenovo, por lo que la normalizaremos/corregiremos por HP.
- CPU: todos los procesadores deberán tener 2 letras, empezarán por una "i" y terminarán con un número siempre impar superior o igual a 3. Por ejemplo: i3, i5, i7, hasta i9. Solo se admite un número de procesador. Si se encuentra un número par, se convertirá al número inferior:
    + Ejemplo:
        - i5 será i5.
        - i4 será i3.
        - Intel i7 será i7.
        - Inteli5 será i5.
- RAM: ahí hemos tenido suerte y todas las entradas son correctas y no debemos limpiar este dato.
- HD: el dato del disco duro, también viene muy sucio. El dato del disco duro vendrá descrito por al menos 2 números consecutivos.
    + Ejemplo:
        - 256GB será normalizado a 256.
        - HD: 128 será normalizado a 128.
        - HD1: 512Gb1 será normalizado a 512.
        - ssd6 no se podrá normalizar porque solo tiene un número.

Como se puede ver, la última entrada no cumplirá con el último requisito, solo tiene un número de 1 dígito, por lo que no se podrá leer y deberá comunicarse al usuario este hecho.

Una vez leídos los ordenadores se almacenarán en la estructura más rápida posible que consiga dar la información solicitada y con el diseño más apropiado para la estructura de información que se suministra.

Se trabajará con el mejor tratamiento de errores posible que nos lleve a un código limpio y estructurado. 

Se deberán tipificar todas las funciones.


### Interfaces del programa

De forma obligatoria, el programa principal deberá trabajar con las siguientes funciones que definen los interfaces siguientes. Si el profesor tomara las siguientes funciones y las llamara desde su main, el programa debería trabajar perfectamente.

Los errores no serán ni descriptivos ni específicos porque la entrada que esté mal, se eliminará y no habrá ninguna posibilidad de recuperación. Se dice que este tipo de procesos en los que no existe interacción con el usuario son **procesos batch**.

Versión sin objetos:
```python
def limpiar_datos(ordenador:str) -> tuple[str, str, int, int]
    raise Exception
```

La función limpiar_datos llamará a su vez a las siguientes funciones:

```python
def normalizar_marcas(marca_entrada:str) -> str
    raise ValueError

def normalizar_cpu(cpu_entrada:str) -> str
    raise ValueError

def normalizar_hd(hd_entrada:str) -> str
    raise ValueError
```

### Etapa de Testing

El programa deberá testeado (validado) en todo momento gracias a un módulo de test (test.py) que verifique la correcta funcionalidad de todas las funciones ejecutándolas de forma unitaria.

La salida será la siguiente:
```
p(base) C:\Users\davidcb\Dropbox\Departamentos\Python\asignatura\practicas\12.python_avanzado>python test.py
Ejecutando tests....
- Función inicializar_datos(): OK
- Función limpiar_datos(ordenador:str): HP i7 16 512 - OK
- Función normalizar_marcas(marca_introducida:str): Lenovo - OK
- Función normalizar_cpu(cpu_introducida:str): i5 - OK
- Función normalizar_hd(hd_introducido:str): 512 - OK
Fin de los tests
```

![Output](output_new.jpg)

### Salida generada

```
No se puedo procesar la entrada: DLL,  Inteli5,8,ssd6

Ordenadores Lenovo:
- Lenovo i5 8 200
- Lenovo i7 8 512
```




