# Mini-práctica de Excepciones

## Enunciado
Implementa una función `crear_persona(informacion: str) -> tuple[str, int]` que reciba una cadena de texto con el nombre y la edad de una persona en el siguiente formato:

```text
"Nombre, edad"
```

La función debe:

1. **Separar** el nombre y la edad a partir de la cadena de entrada, usando la coma como separador.
2. **Eliminar espacios en blanco** sobrantes alrededor del nombre y de la edad.
3. **Validar el nombre** con los siguientes criterios:
   * Debe tener una longitud comprendida entre **4 y 10 caracteres**.
   * Debe comenzar por **letra mayúscula**. No se podrá utilizar el método `isupper()`.
4. **Convertir y validar la edad**:
   * La edad debe poder convertirse a entero.
   * Su valor debe estar comprendido entre **18 y 99** (ambos incluidos).

En caso de que alguna de las condiciones anteriores no se cumpla, la función debe lanzar una excepción `ValueError` con un mensaje descriptivo del problema.

Si todo es correcto, la función devolverá una **tupla** `(nombre, edad)` donde:

* `nombre` es una cadena con el nombre validado.
* `edad` es un entero con la edad validada.


## Valores de entrada a probar
```
"Manuel, 22"
"luis, 33"
"Ana,18"
"Marta, 16"
"Federico, ??"
```

## Output
```
('Manuel', 22)
Error: El nombre debe empezar por mayúsculas
Error: La longitud del nombre debe estar entre 4 y 10 caracteres
Error: La edad debe estar comprendida entre 18 y 99 años
Error: La edad ?? no es un número
```
