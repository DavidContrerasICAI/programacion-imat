# Proyecto Final de Programación
## Objetivo

Al finalizar la asignatura se deberá entregar un proyecto que ponga de manifiesto las competencias adquiridas por el alumno durante la asignatura.

Cada alumno deberá elegir entre tres tipos de proyectos:
- **Hundir la flota**: proyecto planificado por el profesor de la asignatura. Se orientará sobre cómo diseñarlo/programarlo y se definirán unos objetivos funcionales y temporales de cada incremento a desrrollar. 
- **Juego a elegir por el alumno**: la temática y diseño del juego lo decidirá el propio alumno. Necesitará el visto bueno del profesor.
- **Desarrollo en Minecraft a elegir por el alumno**: la funcionalidad dentro del juego la decidirá el propio alumno. Necesitará el visto bueno del profesor.

Los proyectos son indivudales. Solo se podrán realizar en pareja con el visto bueno del profesor.

## Utilización de Inteligencia Artificial Generativa (GenAI)

Todo el código escrito en este proyecto **deberá ser entendido, poseerá el estilo de programación desarrollado en clase propio del alumno y podrá ser explicado por el alumno ante el profesor**. Dicho de otra forma, no se podrá incluir código simplemente por C&P generado por fuentes externas.

Se podrá utilizar GenAI para el conocimiento y entendimiento de librerías o códigos no vistos en clase (por ejemplo, uso de Pygame).

Cualquier indicio de incumplimiento de esta norma implicará un 0 en la calificación del proyecto.


## Entrega

**Fecha de entrega**: domingo 11 de enero a las 23:59. 

**Lugar**: Moodle 

**Archivos a entregar**: 
- Se desarrollará un módulo de testing (test.py) que probará el funcionamiento de al menos dos funciones.
- Se entregará un **zip** con todos los módulos Python desarrollados y ficheros complementarios necesarios (csv, txt, jpg, etc.). El alumno deberá comprobar que el programa funciona también en otro directorio distinto al Workspace o directorio de desarrollo.
- Todas las funciones deberán estar documentadas (DocString) y tipificadas. 
- Se entregará un **póster en PDF** en el que se presenten los resultados más importantes del desarrollo. La plantilla se suministra en Moodle. Este póster lo conservará el alumno como resultado de los proyectos que ha ido haciendo en la carrera. 

## Proyecto: Hundir la Flota

Existirán dos tableros, uno del usuario con la colocación de sus barcos y otro con la información de los disparos que ha realizado sobre el tablero oponente.

### Requisitos mínimos

- Se cuidará la UX (User Experience).
- No podrá tener errores.

### Funcionalidad obligatoria
- La partida se realizará entre dos jugadores.
- Se elegirá el número de barcos a crear: [2, 5].
- El tamaño de los barcos será siempre decreciente desde 5 celdas hasta 2, según el número de marcos elegido.
- La colocación de los barcos será elegida por el usuario.
- Las partidas podrán ser guardadas para continuarlas cuando se desee.


### Funcionalidad opcional
- El usuario podrá jugar contra la máquina.
- La colocación de los barcos podrá ser automática.


## Posible intefaz a realizar

Se deberán crear dos matrices que contendrán la configuración de los barcos del usuario y del oponente. Las matrices de los jugadores solo contendrán las celdas propias del juego, es decir, las posiciones propias de los barcos. No formarán parte de la matriz las etiquetas de las filas ni las columnas (las letras y los números).

Las celdas de las matrices podrán contener la siguiente información:
- "··": Agua
- "##": Barco 
- "\*\*": Barco tocado
- "!!": Barco hundido
- "++": Agua en el disparo realizado

### Salida

Se deberá crear la pantalla del juego con los dos tableros que incorporen una información de ejemplo similando acciones del juego: posición de los barcos, disparos, etc.

```
            USUARIO                           OPONENTE            

   1  2  3  4  5  6  7  8  9 10      1  2  3  4  5  6  7  8  9 10
A ## ## ** ## ## ·· ·· ·· ·· ··    A ·· ·· ·· ·· ·· ·· ·· ·· ·· ··
B ·· ## ## ## ## ·· ·· ·· !! ··    B ·· ·· ++ ·· ·· ·· ** ** ·· ··
C ·· ·· ·· ·· ·· ·· ·· ·· !! ··    C ·· ·· ·· ·· ·· ·· ·· ·· ·· ··
D ·· ## ·· ·· ·· ·· ·· ·· ·· ··    D ·· ·· ·· ·· ++ ·· ·· ·· ·· ··
E ·· ## ·· ·· ·· ·· ·· ·· ·· ··    E ·· !! !! ·· ·· ·· ·· ·· ·· ··
F ·· ** ·· ·· ·· ·· ·· ·· ·· ··    F ·· ·· ·· ·· ·· ·· ·· ·· ·· ··
G ·· ·· ·· ·· ·· ·· ·· ·· ·· ··    G ·· ·· ·· ·· ·· ++ ·· ·· ·· ··
H ·· ·· ·· ·· ·· ·· ·· ·· ·· ··    H ·· ·· ·· ·· ·· ·· ·· ·· ·· ··
I ·· ·· ·· ·· ·· ·· ·· ·· ·· ··    I ·· ·· ·· ·· ·· ·· ·· ·· ·· ··
J ·· ·· ·· ·· ·· ·· ·· ·· ·· ··    J ·· ·· ·· ·· ·· ·· ·· ·· ·· ··
```

