# Mini-prácticas 10. Ficheros

## Objetivo
Esta práctica pretende alcanzar los siguientes resultados de aprendizaje:
- Dominar las operaciones básicas de lectura y escritura.
- Entender la importancia de las codificaciones de los ficheros.

## Enunciado

Se realizarán 3 mini-programas que se describen a continuación, teniendo en cuenta que en el proceso de apertura de un fichero se puede especificar la codificación que se desea seguir a la hora de abrir un fichero. Éste es un buen momento para recodar que detrás de todo caracter hay una combinación de bits que lo representan. El problema es que hay muchas codificaciones distintas... :(
```python
with open("a.txt", "r", encoding = "utf-8") as fichero:
```

### main01.py

Seguir los siguientes pasos:
- Abrir el editor de texto Sublime Text.
- Escribir caracteres como acentos y "ñ".
- Guardarlo como "a.txt".
- Guardarlo nuevamente siguiendo los siguientes pasos:
    + File --> Save with encoding --> Western (Windows 1252)
- Realizar un programa Python que lea el fichero abriéndolo con las siguientes codificaciones:
    + sin especificar ninguna.
    + "cp1252"
    + "utf-8"


### main02.py

Escribir un programa Python que cree un fichero llamado "fichero-utf8.txt" con codificación "utf-8" con el siguiente contenido:
```
Una línea
Otra con ñs y ás, és, ís...
Otra con 😀
```

Abrir ese mismo fichero a continuación y mostrar su contenido utilizando las siguientes codificaciones:
- sin especificar ninguna.
- "utf-8"
- "iso-8859-1"
- "ascii"


### main03.py

Crear un fichero llamado "personas.txt" en un editor de texto, como por ejemplo el Bloc de Notas o Sublime Text, con el siguiente contenido:
```
Luis
22
Madrid
Ana
18
Barcelona
Lucía
19
Madrid
Manuel
20
Valencia
```

A continuación, crear un programa Python que tome la información del fichero y la estructure en un diccionario con la estructura:
```
{nombre: (edad, ciudad)}

{Luis: (22, "Madrid")}
```

Es importante saber que este fichero puede contener la información de n personas, no debe programarse solo para las que figuran como ejemplo, ya que en un futuro podrá haber más. La parte más importante es saber que siempre existirán en bloques de 3 líneas, las líneas estarán siempre en el orden que aparecen (nombre, edad, ciudad) y que la edad siempre será un número entero válido.
