# Ejercicio de Excepciones

## Enunciado

Se desea desarrollar una aplicación en Python para gestionar potencias de coches a partir de varios ficheros de texto.

En la carpeta `datos` se dispone de varios ficheros (`coches1.txt`, `coches2.txt` y `coches3.txt`) con información sobre distintos vehículos. Cada fichero contiene una primera línea de cabecera y, a continuación, varias líneas con el siguiente formato:

```text
nombre_coche#potencia
```

donde `nombre_coche` es una cadena y `potencia` es la potencia del coche en caballos (cv), expresada como texto.

Ejemplo:
```
Toyota Corolla 1.8#140
Volkswagen Golf 2.0 TDI#150
Seat Ibiza 1.0 TSI#95
Renault Clio 1.3 TCe#130a
Peugeot 308 1.5 BlueHDi#130
```


## Funcionalidad

1. **Leer los datos de los coches** desde los tres ficheros y almacenarlos en un diccionario de Python, donde:

   * La *clave* sea el nombre del coche.
   * El *valor* sea la potencia en cv como entero.

2. Antes de guardar cada potencia, debe validarse mediante una función `transformar_cv(cv_str)` que:

   * Comprueba que la longitud de la cadena no supera los 3 caracteres.
   * Verifica que la potencia es mayor o igual que una potencia mínima (por ejemplo, 100 cv).
   * Si la cadena no es numérica, es demasiado larga o la potencia es inferior al mínimo, lanza una excepción propia `PotenciaError` con un mensaje adecuado.

3. Todas las líneas con errores de potencia deberán anotarse en un fichero `datos/errores.txt`, indicando:
   * El nombre del fichero de origen.
   * El número de línea donde se ha producido el error.
   * El mensaje de la excepción y la línea original.

4. Una vez leído y validado todo, **guardar el diccionario de coches correcto** en un fichero `datos/coches.csv`, donde cada línea tenga el formato:

```text
nombre_coche, potencia
```

5. El programa principal deberá:

   * Llamar a la función de lectura para obtener el diccionario de coches.
   * Mostrar por pantalla el listado de coches y su potencia.
   * Llamar a la función de guardado para generar el fichero CSV.

Se debe programar mediante un buen diseño: módulos separados (`funciones.py`, `constantes.py`, `excepciones.py`), excepciones y el uso de constantes para los parámetros de validación.
