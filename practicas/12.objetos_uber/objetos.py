from constantes import *
import funciones as func

class Vehiculo:
    def __init__(self, x, y):
        """
        Args:
            x (int): coordenada inicial x
            y (int): coordenada inicial y
        """
        self.x = x
        self.y = y
        self.coste_viaje = 0
        self.cliente = None  # Viajero a transportar asignado
        self.ocupado = False  # Se ocupa cuando recoge al viajero

    def mover(self):
        if self.cliente != None:  # solo se mueve si tiene un objetivo: buscar o transportar clientes
            if self.ocupado:
                x_delta = self.cliente.x_destino - self.x
                y_delta = self.cliente.y_destino - self.y

                self.avanzar(x_delta, y_delta)

                if self.x == self.cliente.x_destino and self.y == self.cliente.y_destino:
                    self.cliente = None
            else:
                x_delta = self.cliente.x - self.x
                y_delta = self.cliente.y - self.y

                self.avanzar(x_delta, y_delta)

                if self.x == self.cliente.x and self.y == self.cliente.y:
                    self.ocupado = True

    def isMovimiento(self):
        return self.cliente != None

    def avanzar(self, x_delta, y_delta):
        func.borrar_en_ciudad(self)

        if x_delta > 0 and self.x < FILAS - 1:
            self.x += 1
        elif x_delta < 0 and self.x > 0:
            self.x -= 1
        elif y_delta > 0 and self.y < COLUMNAS - 1:
            self.y += 1
        elif y_delta < 0 and self.y > 0:
            self.y -= 1

        func.posicionar_en_ciudad(self)
        self.coste_viaje += 1

    def __str__(self):
        if self.cliente != None:
            if self.ocupado:
                estado = self.cliente.str_llevando()
            else:
                estado = self.cliente.str_buscando()
        else:
            estado = "Fin del servicio"

        return f"({self.x}, {self.y}) Coste: {self.coste_viaje * COSTE_POR_CELDA}€ -> {estado}" 

    def print_in_ciudad(self):
        if self.cliente == None:
            return COLOR_VERDE + CHAR_UBER + COLOR_DEFECTO
        elif self.ocupado:
            return COLOR_ROJO + CHAR_UBER + COLOR_DEFECTO
        else:
            return COLOR_AZUL + CHAR_UBER + COLOR_DEFECTO



class Cliente:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = x
        self.y = y

    def set_destino(self, x_destino, y_destino):
        self.x_destino = x_destino
        self.y_destino = y_destino

    def print_in_ciudad(self):
        return COLOR_AMARILLO + CHAR_CLIENTE + COLOR_DEFECTO

    def str_buscando(self):
        return f"Buscando a {self.nombre} en ({self.x}, {self.y})"

    def str_llevando(self):
        return f"Llevando a {self.nombre} a ({self.x_destino}, {self.y_destino})"

    def __str__(self):
        return f"{self.nombre} de ({self.x}, {self.y}) - a ({self.x_destino}, {self.y_destino})"