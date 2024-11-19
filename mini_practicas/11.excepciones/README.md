# Mini-práctica 10. Incluir gestión de excepciones en la Calculadora (Tema 10)
## Enunciado
A partir de la práctica 9 de la calculadora (código que se suministra) incluid gestión de excepciones en las siguientes partes del código para que no lance ningún error de ejecución el programa. 

No será necesario repetir la entrada de datos, simplemente mostrar un mensaje de error e impedir que el programa lance errores interrumpiendo su ejecución.

Funciones a modificar:
- Función validar_tipo_dato(): 
	+ Comportamiento actual: actualmente controla los valores introducidos (int, float y complex) de forma manual por la existencia o no de ciertos caracteres. 
	+ A desarrollar: delegar el proceso de validación del tipo en las funciones de conversión tratando el posible error que lance.
- Función repetir_operacion(): 
	+ Comportamiento actual: no se realiza ninguna comprobación de que la clave introducida exista. 
	+ A desarrollar: validar la existencia de la clave mediante excepciones. ¿Cuál sería la alternativa a esta programación?
- Función calcular_ascii():
	+ Comportamiento actual: si se introducen varios caracteres lanzará un error.  
	+ A desarrollar: validar la entrada mediante la excepción que lance el método ord().
- Función calcular_caracter(), calcular_abs() y calcular_round():
	+ Comportamiento actual: si la entrada no es numérica, lanzará un error.  
	+ A desarrollar: validar la entrada mediante la excepción.
- División por cero: ¿qué ocurre si se intenta hacer una división por cero? Soluciona este error mediante excepciones.