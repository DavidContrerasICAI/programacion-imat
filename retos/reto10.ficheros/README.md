# Gestor de valoraciones de películas por alumnos - FICHEROS

Crear un programa Python que almacene las películas que han visto los alumnos por género de la forma que considere el alumno para que el acceso a la información que se indica a continuación (por alumno y por género) sea lo más eficiente posible. Cada película deberá tener además, una **valoración numérica** (0–10). 

Implementa un programa en Python que:

1. **Creación de la estructura**
    * Le del fichero `personas.txt` la siguiente información y almacena en la estructura de datos que consideres con la información por defecto que se suministra:

```
Nombre, Género, Película, Valoración
alumno1, acción, peli1, 10
alumno1, acción, peli5, 6 
alumno1, terror, peli8, 2 
alumno1, terror, peli6, 6 
alumno2, acción, peli3, 8 
alumno2, acción, peli7, 2 
alumno2, terror, peli8, 2 
alumno2, terror, peli6, 6 
alumno3, acción, peli1, 6 
alumno3, acción, peli3, 4 
alumno3, terror, peli6, 4 
alumno3, terror, peli4, 6 
```


1. **Actualización de datos**
   * Añada una nueva valoración para un alumno concreto en un género determinado (p. ej., insertar `("peli3", 6)` en el género `"acción"` de `"alumno1"`).

2. **Consulta personalizada (favoritas por alumno y género)**
   * Pedir por teclado un **nombre de alumno** y un **género** a buscar.
   * Si existen, muestre por pantalla `Pelis favoritas de <alumno>` y, dentro de ese género, **solo** las películas con valoración **strictamente mayor** que 5.
   * Representa la valoración con **estrellas** (`⭐`) tantas como indique la nota y capitaliza el nombre de la película.
3. **Catálogo por géneros (sin duplicados)**
   * Muestra todas las películas agregadas por género. No tendrán que existir duplicados.
4. **Catálogo por géneros con medias**
   * Se deberá mostrar esta vez la valoración media de todos los usuarios por cada película.
   * Calcule la **media aritmética** por película y muéstrela con:
     * Estrellas `⭐` equivalentes a la **parte entera** de la media.
     * La media numérica con **un decimal**.
   * Encabezado: `Películas agregadas por GÉNERO con VALORACIONES MEDIAS`.

**OUTPUT**
```
Alumno: alumno1
Género: acción
Pelis favoritas de alumno1 valoradas con más de un 5
  - Peli1 ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
  - Peli5 ⭐⭐⭐⭐⭐⭐

Películas agregadas por GÉNERO
🎞️  Acción 🎞️
  🎥 Peli1
  🎥 Peli5
  🎥 Peli3
  🎥 Peli7
🎞️  Terror 🎞️
  🎥 Peli8
  🎥 Peli6
  🎥 Peli4

Películas agregadas por GÉNERO con VALORACIONES MEDIAS
🎞️  Acción 🎞️
  🎥 Peli1 ⭐⭐⭐⭐⭐⭐⭐⭐ 8.0
  🎥 Peli5 ⭐⭐⭐⭐⭐⭐ 6.0
  🎥 Peli3 ⭐⭐⭐⭐ 4.7
  🎥 Peli7 ⭐⭐ 2.0
🎞️  Terror 🎞️
  🎥 Peli8 ⭐⭐ 2.0
  🎥 Peli6 ⭐⭐⭐⭐⭐ 5.3
  🎥 Peli4 ⭐⭐⭐⭐⭐⭐ 6.0
```
