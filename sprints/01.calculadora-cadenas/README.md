# Sprint 2 sobre la Práctica 4. Calculadora
## Solución

**Iteración III**

El programa validará que los números introducidos se corresponden con el tipo seleccionado. Se asumirá que el usuario siempre introducirá un número válido. Por ejemplo, el usuario nunca introducirá valores del tipo 12a, 45.6.2 ó 3+8jk, pero sí puede confundirse a la hora de introducir el tipo. Por ejemplo, puede elegir un tipo de dato (int) para trabajar con números enteros e introducir un número float (23.5). En este caso, se le volverá a pedir el número al usuario. 

Para realizar estas validaciones deberéis repasar el aparatado **4.6.2 Operaciones básicas con strings**.

**Iteración IV**

Se deberá modificar el programa para validar que los datos introducidos son correctos. Ahora el usuario se puede equivocar al teclear. Como en el caso anterior, se pedirá nuevamente el dato al usuario:
- "45.6.2": se podrán introducir float con más de un punto decimal. Generará el mensaje de error: "Los tipos float solo pueden tener un punto decimal".
- "12a", "b12", "1a2": se podrán introducir números enteros con caracteres adicionales. Generará el mensaje de error: "Los tipos int solo pueden contener números".
- "3+8i", "3+8k", "3+8p": se podrán introducir números complejos bien formados excepto por la letra de su parte imaginaria que se puede ser otro carcter distinto a una "j". Generará el mensaje de error: "Los tipos complex deben tener la letra j".