# Progreso de códigos con Programación estructurada

Este ejemplo recoge distintas versiones de un mismo ejercicio en **Python** para mostrar como va evolucionando la solucion a medida que se simplifica y mejora el codigo.

## Objetivo del ejercicio

Comprobar si una cadena de texto contiene una letra determinada.

En los ejemplos se trabaja con:

```python
s = "Hola esto es una pruebaX"
LETRA = "X"
```

---

## Evolucion de las soluciones

### 1. Primera version - recorrer toda la cadena

[Ver `main1.py`](./main1.py)

La primera solucion utiliza:

- una variable booleana (`encontrado`);
- un indice (`i`);
- un bucle `while`;
- una condicion `if`.

El programa recorre toda la cadena y cambia `encontrado` a `True` cuando encuentra la letra buscada.

**Conceptos practicados:** variables booleanas, indices, `while`, `if` y acceso a caracteres de una cadena.

---

### 2. Segunda version - condición de parada mediante un booleano

[Ver `main2.py`](./main2.py)

Se mejora la condicion del bucle:

```python
while i < len(s) and not encontrado:
```

Ahora el recorrido puede terminar en cuanto se encuentra la letra, evitando comprobar caracteres innecesarios.

**Mejora principal:** introducir una condicion de parada anticipada.

---

### 3. Tercera version - simplificar la asignacion booleana

[Ver `main3.py`](./main3.py)

La comprobacion:

```python
if s[i] == LETRA:
    encontrado = True
```

se sustituye por una asignacion directa:

```python
encontrado = s[i] == LETRA
```

Esto hace el codigo mas compacto y muestra que una comparacion ya produce directamente un valor booleano (`True` o `False`).

**Concepto nuevo:** usar directamente el resultado de una expresion booleana.

---

### 4. Cuarta version - eliminar la variable booleana

[Ver `main4.py`](./main4.py)

En esta version ya no hace falta utilizar `encontrado`.

El propio indice permite saber que ha ocurrido:

```python
while i < len(s) and s[i] != LETRA:
    i += 1
```

Al terminar:

- si `i == len(s)`, se ha llegado al final sin encontrar la letra;
- en caso contrario, el bucle se ha detenido porque encontro `LETRA`.

**Mejora principal:** una solucion mas directa, con menos variables y aprovechando la condicion del propio bucle.

---

## Resumen del progreso

| Version | Idea principal | Mejora |
|---|---|---|
| [`main1.py`](./main1.py) | Booleano + recorrido completo | Primera solucion funcional |
| [`main2.py`](./main2.py) | Parada anticipada | Evita seguir buscando despues de encontrar la letra |
| [`main3.py`](./main3.py) | Expresion booleana directa | Simplifica el cuerpo del bucle |
| [`main4.py`](./main4.py) | El indice indica el resultado | Elimina la variable `encontrado` |

## Conceptos aprendidos

A lo largo de estas versiones se practican:

- cadenas de caracteres;
- acceso mediante indices;
- `len()`;
- bucles `while`;
- condiciones `if / else`;
- operadores logicos como `and` y `not`;
- valores booleanos;
- condiciones de parada;
- simplificacion y mejora progresiva de algoritmos.

---

## Proximo paso

Una posible siguiente evolucion seria resolver el mismo problema utilizando herramientas propias de Python, por ejemplo:

```python
if LETRA in s:
    print(f"La cadena tiene al menos una {LETRA}")
else:
    print(f"La cadena no tiene ninguna {LETRA}")
```

Sin embargo, las versiones anteriores son utiles para aprender **como funciona internamente una busqueda secuencial** antes de utilizar soluciones mas compactas del lenguaje.
