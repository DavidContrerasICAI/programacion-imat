Escribe un **programa de gestión sencilla de una tienda de ropa** que funcione desde la línea de comandos y haga lo siguiente:

En la carpeta `data/` se dispone de:

* Un fichero `ropa.csv` con información de las prendas, con el siguiente formato (la primera línea es la cabecera):

```text
nombre,precio,temporada
Camiseta blanca,9.99,verano
Pantalón vaquero,29.95,invierno
...
```

* Opcionalmente, un fichero `reemplazos.txt` que contiene reglas de reemplazo de caracteres para normalizar los nombres de las prendas. Cada línea tiene el formato:

```text
caracter_a_buscar:caracter_de_reemplazo
```

Si en una línea solo aparece un carácter sin ningún otro despues de `:`, significa que dicho carácter debe eliminarse del texto.

---

### Funcionamiento del programa

1. Al comenzar, el programa debe construir un **diccionario de reemplazos** llamando a la función:

   ```python
   crear_diccionario_reemplazos(tipo)
   ```

   * Si `tipo` es igual a `"fijo"`, la función devolverá un diccionario con una serie de reemplazos predefinidos (por ejemplo, eliminar `-` y `+`, y quitar acentos de las vocales).
   * Si `tipo` es igual a cualquir otro valor, la función leerá el fichero `data/reemplazos.txt` y construirá el diccionario con las reglas que haya allí.

2. Después, se debe leer el fichero `data/ropa.csv` y almacenar la información en la estructura de datos que considere el alumno:

   * Cada línea (excepto la cabecera) contiene: `nombre,precio,temporada`.
   * El nombre de la prenda se normalizará aplicando todos los reemplazos definidos en `dict_reemplazos`.

3. El programa principal se ejecutará desde la línea de comandos de dos formas:

   * **Sin argumentos**:

     ```bash
     python tienda.py
     ```

     En este caso, se debe mostrar por pantalla el listado completo de prendas.

     Cada línea mostrará el nombre de la prenda, su precio y su temporada con el formato:

     ```text
        Pantalon Vaquero: 50.0€ - Temporada: verano-invierno
        Camiseta chula: 15.0€ - Temporada: invierno
        Bañador: 20.0€ - Temporada: verano
        Calcetines: 10.0€ - Temporada: invierno
     ```

   * **Con el nombre de una prenda como argumento** (ya normalizado según las reglas de reemplazo):

     ```bash
     python tienda.py nombre_prenda
     ```

     En este caso:

     * Si la prenda existe en el diccionario, se mostrará únicamente su precio, por ejemplo:

       ```text
       >python main.py Calcetines
            10.0€
       ```
     * Si la prenda no existe, se mostrará el mensaje:

       ```text
       >python main.py Calcetines
            No existe esa ropa
       ```

