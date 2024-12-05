import pygame
from pygame.locals import *
from constantes import *

# Se utiliza mejor Vector2como tipo para trabajar con x, y en lugar de hacerlo con
# una tupla y referenciarlo como [0] y [1]. Además un Vector2 es mutable
# Se cambia el nombre del tipo a Punto, me gusta más
Punto = pygame.math.Vector2 

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ##self.surf = pygame.Surface((30, 30))
        ##self.surf.fill((128,255,40))   # Color de fondo, si no hubiese imagen 
        self.surf = pygame.image.load("iMAT.png").convert()
        self.rect = self.surf.get_rect()
   
        self.posicion = Punto(ANCHO_PANTALLA/2, 360)
        self.velocidad = Punto(0, 0)
        self.aceleracion = Punto(0, 0)
 
    def mover(self):
        self.aceleracion = Punto(0, 0.5)
    
        teclas_pressed = pygame.key.get_pressed()
                
        if teclas_pressed[K_LEFT]:
            self.aceleracion.x = -ACELERACION
        if teclas_pressed[K_RIGHT]:
            self.aceleracion.x = ACELERACION
                 
        self.aceleracion.x += self.velocidad.x * ROZAMIENTO
        self.velocidad += self.aceleracion
        self.posicion += self.velocidad + 0.5 * self.aceleracion
         
        if self.posicion.x > ANCHO_PANTALLA:
            self.posicion.x = 0
        if self.posicion.x < 0:
            self.posicion.x = ANCHO_PANTALLA
             
        self.rect.midbottom = self.posicion
 
    def saltar(self, colision):
        if colision:
           self.velocidad.y = -15
 
    def actualizar(self, colision):
        if self.velocidad.y > 0:    
            if colision:
                self.velocidad.y = 0
                platform = colision[0]
                self.posicion.y = platform.rect.top + 1

class Plataforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((ANCHO_PANTALLA, 20))
        self.surf.fill((36, 64, 142))   # Fondo azul
        self.rect = self.surf.get_rect(center = (ANCHO_PANTALLA/2, ALTO_PANTALLA - 10))
 
    def mover(self):
        pass