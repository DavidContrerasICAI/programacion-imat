import pygame
from pygame.locals import *
from objetos import Plataforma, Jugador, Enemigo
from constantes import *
 
pygame.init()
 
screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("iMAT vs alumnos")

clock = pygame.time.Clock()
EVENT_ENEMIGO = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_ENEMIGO, 2000)
 
jugador = Jugador()    # Elemento principal que maneja el usuario: salta y desplaza con aceleración 
plataforma = Plataforma()    # Base azul del juego sobre la cual salta y camina 

grupo_sprites = pygame.sprite.Group()
grupo_sprites.add(plataforma)
grupo_sprites.add(jugador)

grupo_plataformas = pygame.sprite.Group()
grupo_plataformas.add(plataforma)

grupo_enemigos = pygame.sprite.Group()   # Todos los enermigos se gestionarán igual

running = True

while running: 
    colision = pygame.sprite.spritecollide(jugador, grupo_plataformas, False)

    for event in pygame.event.get():
        if event.type == KEYDOWN:    
            if event.key == K_SPACE:
                jugador.saltar(colision)
        elif event.type == EVENT_ENEMIGO:
            enemigo = Enemigo()
            grupo_enemigos.add(enemigo)
            grupo_sprites.add(enemigo)
        elif event.type == QUIT:
            running = False
         
    screen.fill((0,0,0))
    jugador.actualizar_colision(colision)
 
    for sprite in grupo_sprites:
        sprite.mover()
        screen.blit(sprite.surf, sprite.rect)

    if pygame.sprite.spritecollideany(jugador, grupo_enemigos):
        jugador.kill()
        running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()