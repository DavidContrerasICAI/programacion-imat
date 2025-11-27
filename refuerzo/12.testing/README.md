# Programa completo de Testing, Excepciones y Ficheros

Se quiere desarrollar una pequeña aplicación de línea de comandos en Python para gestionar el catálogo de coches de un concesionario a partir de varios ficheros de texto.

El programa debe estar organizado en varios módulos:

* **`main.py`**: programa principal que se ejecuta desde la línea de comandos.
* **`funciones.py`**: contiene las funciones de lectura, validación y guardado de datos.
* **`excepciones.py`**: define las excepciones propias de la aplicación.
* **`constantes.py`**: almacena las constantes usadas en las validaciones (por ejemplo, potencia mínima, longitud máxima, etc.).

Los datos de entrada se encuentran en los ficheros `datos/coches1.txt`, `datos/coches2.txt` y `datos/coches3.txt`. Cada uno de estos ficheros contiene una cabecera en la primera línea y, a partir de la segunda, una lista de coches con el siguiente formato:

```text
Nombre del coche, potencia_en_CV, precio
```

Por ejemplo:

```text
Toyota Corolla 1.8, 140, 25.000
```

Se pide:

1. **Lectura y validación de datos**

   * Leer la información de los ficheros `coches1.txt`, `coches2.txt` y `coches3.txt`, lamacenando en la estructura de datos que elija el alumno los coches válidos.

   * La potencia (`cv`) se recibe como cadena y debe convertirse a entero mediante la función `transformar_cv(cv_str)` siempre que se pueda.

     * Solo se aceptan potencias:
       * De longitud menor o igual a `LONGITUD_MAX`.
       * Numéricas.
       * Mayores o iguales a `POTENCIA_MINIMA`.
     * En caso contrario, se debe lanzar una excepción propia `PotenciaError`.
   * El precio se recibe como cadena (puede contener puntos, letras u otros caracteres) y debe limpiarse mediante la función `transformar_precio(precio_str)`, quedándose únicamente con las cifras numéricas.
     * Por ejemplo, `"25.000"` → `25000`, `"32x0x00"` → `32000`.
     * Si no se puede obtener ningún número válido, se lanzará una excepción propia `PrecioError`.

2. **Gestión de errores**

   * Todos los **errores de potencia** (`PotenciaError`) que se produzcan al procesar las líneas de los ficheros de entrada se deben registrar en el fichero `datos/errores.txt`.
   * Cada línea de error debe indicar:

     * El nombre del fichero.
     * El número de línea.
     * El mensaje de error.
     * La línea original que causó el problema.
```
datos/coches1.txt:4 <Potencia inferior a 100cv> -> Seat Ibiza 1.0 TSI, 95, 20000
datos/coches1.txt:5 <Potencia demasiado larga (+3)> -> Renault Clio 1.3 TCe, 130a, 15000
datos/coches2.txt:4 <Potencia no numérica> -> Hyundai i30 1.6 CRDi, 13z, 19000
...
```

   * Si alguno de los ficheros `cochesX.txt` no existe, se debe capturar la excepción `FileNotFoundError` y mostrar un mensaje adecuado por pantalla.

3. **Guardado de resultados**

   * Implementar la función `guardar_coches(diccionario_coches)` que guarde el contenido del diccionario resultante en el fichero `datos/coches.csv`, con el formato:

     ```text
   Toyota Corolla 1.8, 140, 25000
   Volkswagen Golf 2.0 TDI, 150, 32000
   Peugeot 308 1.5 BlueHDi, 130, 28000
     ```

4. **Interfaz por línea de comandos**
   El programa principal (`main.py`) deberá comportarse de la siguiente forma:

   * **Ejecución sin argumentos**

     ```bash
     > python main.py
     ```

     * Lee y procesa los ficheros de entrada.
     * Guarda todos los coches válidos en `datos/coches.csv`.
     * Los errores los guarda en `errores.txt`

   * **Mostrar todos los coches procesados**

     ```bash
     > python main.py show
     ```

     * Tras leer y procesar los ficheros, muestra por pantalla la lista de coches almacenados en el diccionario, con el siguiente formato:

       ```text
       COCHES
         - Toyota Corolla 1.8: 140 (25000€)
         - ...
       ```
     * Finalmente, guarda los datos en `datos/coches.csv` y los errores en `datos/errores.txt`.

   * **Búsqueda de un coche por nombre**

     ```bash
     > python main.py Toyota Corolla 1.8
     ```

     * El programa busca ese coche en el diccionario.
     * Si lo encuentra, muestra por pantalla:

       ```text
       Toyota Corolla 1.8 (140CV) - Precio: 25000€
       ```
     * Independientemente de que lo encuentre o no, actualiza/guarda el fichero `datos/coches.csv` con todos los coches válidos.

5. **Pruebas**

   * Proporcionar un pequeño script de pruebas que verifique el comportamiento de las funciones `transformar_cv` y `transformar_precio`, comprobando tanto casos correctos como casos que deben lanzar las excepciones `PotenciaError` y `PrecioError`.

   * Salida de la ejecución del código de test. Se berá nostrar True si la función se ha ejeuctado de forma correcta a partir del dato de entrada.
   ```
   Testing CV: 12a --> True: Potencia no numérica
   Testing CV: 120 --> True: 120
   Testing PRECIO: 25.000 --> True: 25000
   Testing PRECIO: xxxxx --> True: Precio no es numérico
   ```

En resumen, se debe crear una aplicación robusta que lea datos de varios ficheros, filtre y valide la información utilizando excepciones propias, registre los errores detectados y proporcione una interfaz por línea de comandos para consultar y mostrar la información de los coches.
