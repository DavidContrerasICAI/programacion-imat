import operaciones as op
import salida
import validacion as val

if __name__ == "__main__":
    """
    Programa Principal
    """      
    opcion_numero = 0
    while opcion_numero != 9:

        salida.mostrar_menu()

        opcion = input("Operación: ")
        opcion_numero = int(opcion)  
        
        if opcion_numero > 0 and opcion_numero < 5:  # +, -, *, %...   
            """
            Iteración II: el tipo de dato coincida con lo introducido
            """
            tipo_dato = val.leer_tipo_dato()
            
            """
            Iteración III: el tipo de dato coincida con lo introducido
            """
            numeros = []
            for i in range(1, 3):
                numero = val.validar_tipo_dato(tipo_dato, i) 
                numeros.append(numero)
        
            """
            Código equivalente al de abajo
            numero1 = numeros[0]
            numero2 = numeros[1]
            """
            numero1, numero2 = numeros
        
            if opcion_numero == 1:  #sumar
                op.sumar(numero1, numero2)
            elif opcion_numero == 2:  #restar
                op.restar(numero1, numero2)
            elif opcion_numero == 3:  #multiplicar
                op.multiplicar(numero1, numero2)
            elif opcion_numero == 4:  #dividir
                op.dividir(numero1, numero2)

        elif opcion_numero == 5:  # abs
            op.calcular_abs()
        elif opcion_numero == 6:  # Rendondeo de un float
            op.calcular_round()
        elif opcion_numero == 7:  # char to ascci
            op.calcular_ascii()
        elif opcion_numero == 8:  # char to ascci
            op.calcular_caracter()
        elif opcion_numero == 9:  # Bye
            print("Bye!")
        elif opcion_numero == 10:  # Historial
            salida.mostrar_historial()
        elif opcion_numero == 11:  # Repetir
            salida.repetir_operacion()
        else:
            print("Opción no válida")