import operaciones as op
import salida
import validacion as val

if __name__ == "__main__":
    """
    Programa Principal
    """      

    historial_operaciones = {}

    opcion_numero = 0
    while opcion_numero != 9:
        is_operacion = True    # Solo para resolver que sea una opción no válida y mostrar el resultado
        salida.mostrar_menu()

        opcion = input("Operación: ")
        opcion_numero = int(opcion)  
        
        if opcion_numero > 0 and opcion_numero < 5:  # +, -, *, %...   
            tipo_dato = val.leer_tipo_dato()
            numeros = []
            for i in range(1, 3):    # Se piden 2 números
                numero = val.validar_tipo_dato(tipo_dato, i) 
                numeros.append(numero)
        
            numero1, numero2 = numeros     # Se extraen de la lista como variables: [0] y [1]
        
            if opcion_numero == 1:  # sumar
                resultado = op.sumar(numero1, numero2)
            elif opcion_numero == 2:  # restar
                resultado = op.restar(numero1, numero2)
            elif opcion_numero == 3:  # multiplicar
                resultado = op.multiplicar(numero1, numero2)
            elif opcion_numero == 4:  # dividir
                resultado = op.dividir(numero1, numero2)
        else:
            if opcion_numero >= 5 and opcion_numero <= 8:    # Otras operaciones
                if opcion_numero == 5:  # abs
                    resultado = op.calcular_abs()
                elif opcion_numero == 6:  # Rendondeo de un float
                    resultado = op.calcular_round()
                elif opcion_numero == 7:  # char to ascci
                    resultado = op.calcular_ascii()
                elif opcion_numero == 8:  # char to ascci
                    resultado = op.calcular_caracter()
            else:
                is_operacion = False
                if opcion_numero == 10:  # Historial
                    salida.mostrar_historial(historial_operaciones)
                elif opcion_numero == 11:  # Repetir
                    salida.repetir_operacion(historial_operaciones)
                elif opcion_numero == 9:  # Bye
                    print("Bye!")
                else:
                    print("Opción no válida")

        if is_operacion:
            salida.generar_salida(historial_operaciones, resultado)