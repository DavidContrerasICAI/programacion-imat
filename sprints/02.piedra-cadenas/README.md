# Sprint 2 sobre la Práctica 5. Programación Estructurada - Piedra, papel o tijera
## Solución

### Objetivos
- Diseñar correctamente el flujo del programa para crear un programa correctamente estructurado.
- Elegir los operadores lógicos adecuados para conseguir un código legible y bien estructurado.
- Implementar una solución software a partir de unos requisitos dados.
- Saber identificar los incrementos para llegar a la solución final.

### Restricciones
- Se prohibe utilizar:
    + Estructura for.
    + Operador in.
    + Métodos de la clase **str**.

## Enunciado de la práctica

Se rediseñara el programa teniendo en cuenta las siguientes restricciones de diseño:
- Los elementos del juego a utilizar (P/p/T) deberán almacenarse obligatoriamente en una constante denominada ELEMENTOS. Toda validación o tratamiento interno de los elementos a seleccionar el usuario, deberá realizarse a través de esta constante. Esta nueva forma de trabajar permitirá en un futuro cambiar los alias de los elementos de un forma rápida.
```python
PIEDRA = "P"
PAPEL = "p"
TIJERA = "T"
ELEMENTOS = PIEDRA + PAPEL + TIJERA
```
- De igual manera, la lógica del propio juego vendrá determinada por la cadena de caracteres LOGICA_JUEGO. Esta constante indicará el criterio de victoria. Para determinar quién gana, se deberá consultar esta constante. Esta nueva forma de trabajar permitirá en un futuro la actualización cómoda y fácil de las reglas.
```python
LOGICA_JUEGO = (PIEDRA + TIJERA) + (TIJERA + PAPEL) + (PAPEL + PIEDRA)  # "PTTppP" Determina las combinaciones ganadoras: P-T, T-p, p-P
```
- El conteo de victorias, empates o derrotas no se podrá realizar con la utilización de tres variables sin más...Demasiado fácil. Se utilizará un string de 9 caracteres. Los 3 primeros representarán el valor binario de las victorias, los tres siguientes de los empates y los últimos de las derrotas. De esta manera, si el usuario ha ganado 2 veces, empatado 2 y perdido 3, el valor de esta variable será:
```
resultado = "010010011" 
```
- El interfaz de entrada y salida del juego será idéntico, no cambiará nada

## Salida

```
Nombre: David
¿Cuántas partidas quieres jugar [1, 5]? 7
¿Cuántas partidas quieres jugar [1, 5]? 3

¿[P]iedra, [p]apel o [T]ijera? X
¿[P]iedra, [p]apel o [T]ijera? P
USER: P - MÁQUINA: T >>> GANAS

¿[P]iedra, [p]apel o [T]ijera? p
USER: p - MÁQUINA: P >>> GANAS

¿[P]iedra, [p]apel o [T]ijera? T
USER: T - MÁQUINA: P >>> PIERDES
  
Resultado Final  
====================
David 2 - 1 MÁQUINA
Empates: 0
```