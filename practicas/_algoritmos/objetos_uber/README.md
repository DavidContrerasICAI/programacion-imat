# Práctica 12. Objetos UBER

## Objetivo
Esta práctica pretende alcanzar los siguientes resultados de aprendizaje:
- Saber diseñar un programa con el paradigma de orientación a objetos.
- Dominar la definición de objetos mediante clases.
- Potenciar el uso de los métodos para delegar acciones en los objetos y concentrar su lógica.
- Dominar la modularización de código.
- Aprender a no trabajar con valores fijos en un programa que luego puedan cambiar.

## Enunciado

### Funcionalidad

Se desea desarrollar un programa basado en objetos que simule el comportamiento de un servicio de taxi tipo Uber. 

El programa deberá trabajar con una matriz de 5 x 5 que representará la ciudad. Estos valores podrán ser modificados en un futuro, por lo que deberá programarse para cambiarlo fácilmente en el futuro.

En la ciudad existirán dos clientes y dos vehículos (se recomienda empezar por un cliente y un vehículo) que se posicionarán en la ciudad en estas posiciones:
```
coordenadas_ubers = [(0, 2), (4, 4)]
coordenadas_clientes = [(3, 0), (4, 2)]
nombres_clientes = ["Luis", "Ana"]
```
Cuando se inicie el programa asignaremos al cliente mediante el teclado el destino al cual deberá ir, mediante unas coordenadas x, y. El formato obligatorio de entrada deberá ser "numero,numero", pudiéndo aceptarse entradas con cualquier número de espacios: 3,5 ó 3, 5 ó 3 , 5 ó 3   ,5... El usuario podrá introducir cualquier tipo de dato, por lo que el programa deberá gestionar los errores de la mejor forma posible, no pudiendo interrumpirse la ejecución en ningún caso.
```
Introduzca el destino del cliente #1 (x,y):
```
A partir de este momento el cliente comunicará al taxi su posición actual para que le pueda recoger. El taxi deberá tomar la lógica de búsqueda que considere para llegar al cliente desplazándose por la matriz. En el momento que el taxi llegue hasta esa posición, el cliente le indicará su destino y le dirigirá hasta él. Igualmente se podrá seguir la lógica que se desee.

Al llegar al destino el vehículo Uber deberá indicarle al cliente el coste del recorrido, que será igual a una cantidad establecida antes de empezar el programa en € por el número de celdas recorridas (recogida del cliente + transporte al destino). El coste por defecto será 5€/celda.

#### Parte avanzada

Preparar el programa para que pueda trabajar con n ubers para n clientes.

### Restriccciones

- Los movimientos del vehículo no podrán ser en diagonal, solo se podrá desplazar en horizontal o vertical.
- Se asume que no hay conflicto de posiciones con otros objetos.

### Salida generada

La salida del programa constará de varias partes de forma incremental, según vaya avanzando el alumn@ en la práctica:
- Geolocalización del Uber: celdas en la que se encuentra en cada momento.
- Coste solo al finalizar el servicio.
- Coste durante todo el servicio.
- Geolocalización visual de la ciudad imprimiendo la matriz en cada instante.

#### Posible leyenda y constantes a utilizar en el programa
```python
    CHAR_VACIO        =  "_........_"     # Símbolo en la matriz para representar una celda vacía
    CHAR_UBER         =  "_..oT=o.._"      # Símbolo en la matriz para representar un UBER
    CHAR_CLIENTE      =  "_. =:-) ._"      # Símbolo en la matriz para representar un CLIENTE/PASAJERO

    COLOR_VERDE = "\033[1;32m"
    COLOR_ROJO = "\033[1;31m"
    COLOR_AMARILLO = "\033[1;33m"
    COLOR_AZUL = "\033[1;34m"
    COLOR_DEFECTO = "\033[0m"
```

```python
    print("\n\n### Leyenda:\n")
    print(f"{COLOR_AMARILLO+CHAR_CLIENTE+COLOR_DEFECTO}: Cliente de Uber")
    print(f"{COLOR_VERDE+CHAR_UBER+COLOR_DEFECTO}: Uber libre, no tiene servicio")
    print(f"{COLOR_AZUL+CHAR_UBER+COLOR_DEFECTO}: Uber buscando cliente")
    print(f"{COLOR_ROJO+CHAR_UBER+COLOR_DEFECTO}: Uber llevando cliente")
```

Si no se muestran los colores en la consola de ejecución en VSC, escribir el siguiente comando en una Consola (Símbolo del Sistema) como administrador:
```
reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f
```

#### Pantalla de ejecución

![Output](output.jpg)

