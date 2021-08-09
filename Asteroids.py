# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import LARGURA, ALTURA, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
janela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Asteroids')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(janela)
    elif state == GAME:
        state = game_screen(janela)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

