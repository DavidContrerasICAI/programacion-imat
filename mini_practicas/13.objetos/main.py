import objetos as obj

if __name__ == "__main__":
    notas = dict() 

    alumno = obj.Alumno("Luis", 2222, "1ºA")
    asignatura1 = obj.Asignatura("Progra", 7.5)
    asignatura2 = obj.Asignatura("Álgebra", 4)
    asignatura3 = obj.Asignatura("Cálculo", 5.0)

    notas[alumno] = [asignatura1, asignatura2, asignatura3]

    alumno = obj.Alumno("Ana", 1111, "1ºB")
    asignatura1 = obj.Asignatura("Progra", 4.0)
    asignatura2 = obj.Asignatura("Álgebra", 8.5)
    asignatura3 = obj.Asignatura("Cálculo", 6.0)

    notas[alumno] = [asignatura1, asignatura2, asignatura3]

    for alumno, asignaturas in notas.items():
        print(f"Notas de {alumno}")
        for asignatura in asignaturas:
            print(f" - {asignatura}")
