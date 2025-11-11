# Ejercicio de refuerzo de Diccionarios
## Enunciado
Desarrollar un programa que permita reproducir las canciones de una playlist de un usuario. Para ello el programa deberá pedir el login al usuario: usuario y contraseña. 

A continuación se le pedirá la opción a elegir:
1. Agregar una canción a una playlist. Se le pedirá el nombre de la playlist y a continuación el nombre de la canción. 
2. Reproducir una playlist. Se pedirá el nombre de la playlist y se reproducirán las canciones.

La forma de reproducir las canciones será mostrando el texto "Reproduciendo nombre de la canción 1...". A los 3 segundos se saltará a la siguiente canción: "Reproduciendo nombre de la canción 2...". Cuando no existan más canciones se mostrará el texto "Fin de la reproducción".

```python
import time

time.sleep(segundos_de_espera)
```

El acceso a toda la información deberá ser lo más rápido posible.