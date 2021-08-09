import pygame
import os
from config import METEORO_LARGURA, METEORO_ALTURA,METEORO2_LARGURA, METEORO2_ALTURA, NAVE_LARGURA, NAVE_ALTURA, IMG_DIR, SND_DIR, FNT_DIR


FUNDO = 'background'
METEOR_IMG = 'meteor_img'
METEOR_IMG = 'meteor_img'

METEOR2_IMG = 'meteor2_img'
METEOR2_IMG = 'meteor2_img'

NAVE_IMG = 'ship_img'
NAVE_IMG = 'ship_img'
TIRO_IMG = 'bullet_img'
EXPLOSAO_ANIM = 'explosion_anim'
PONTOS_FONT = 'score_font'
EXPLOSAO_SOM = 'boom_sound'
DESTRUICAO_SOM = 'destroy_sound'
PEW_SOUND = 'pew_sound'


def load_assets():
    assets = {}
    assets[FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'starfield.png')).convert()
    assets[METEOR_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'meteorBrown_med1.png')).convert_alpha()
    assets[METEOR_IMG] = pygame.transform.scale(assets['meteor_img'], (METEORO_LARGURA, METEORO_ALTURA))

    assets[METEOR2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Elefante_img.png')).convert_alpha()
    assets[METEOR2_IMG] = pygame.transform.scale(assets['meteor2_img'], (METEORO2_LARGURA, METEORO2_ALTURA))

    assets[NAVE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[NAVE_IMG] = pygame.transform.scale(assets['ship_img'], (NAVE_LARGURA, NAVE_ALTURA))
    assets[TIRO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()

    explosion_anim = []

    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets[EXPLOSAO_ANIM] = explosion_anim
    assets[PONTOS_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[EXPLOSAO_SOM] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[DESTRUICAO_SOM] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets
