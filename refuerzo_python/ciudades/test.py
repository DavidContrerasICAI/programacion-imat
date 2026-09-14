import funciones as f
print(True == f.validar_linea_persona([], "Mariano;18;Calle del viento, 18;28760;Madrid"))
print(False == f.validar_linea_persona([], "Mariano;18;Calle del viento;28760;Madrid"))

