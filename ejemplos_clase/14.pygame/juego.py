import pygame
from pygame.locals import *
from objetos import Plataforma, Jugador
from constantes import *
 
pygame.init()
 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("iMAT Jumping")
 
plataforma = Plataforma()
jugador = Jugador()
 
sprites = pygame.sprite.Group()
sprites.add(plataforma)
sprites.add(jugador)

plataformas = pygame.sprite.Group()
plataformas.add(plataforma)

running = True

while running: 
    colision = pygame.sprite.spritecollide(jugador, plataformas, False)

    for event in pygame.event.get():
        if event.type == KEYDOWN:    
            if event.key == K_SPACE:
                jugador.saltar(colision)
        elif event.type == QUIT:
            running = False
         
    screen.fill((0,0,0))
    jugador.actualizar(colision)
 
    for sprite in sprites:
        screen.blit(sprite.surf, sprite.rect)
        sprite.mover()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()