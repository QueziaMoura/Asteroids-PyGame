import pygame
import random
from os import path

from config import ALTURA, IMG_DIR, BLACK, FPS, GAME, LARGURA, QUIT


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'fundo_inicio1.png')).convert()
    background2 = pygame.image.load(path.join(IMG_DIR, 'fundo_inicio2.png')).convert()
    instrucoes = pygame.image.load(path.join(IMG_DIR, 'menu.png')).convert()
    background_rect = background.get_rect()

    running = True
    img0 = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        pygame.time.wait(600)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        if img0 == True:
            screen.blit(background, background_rect)
            img0 = False
        else:
            screen.blit(background2, background_rect)
            img0 = True

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        screen.blit(instrucoes, background_rect)
        pygame.display.flip()


    return state
