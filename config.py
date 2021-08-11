from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
LARGURA = 480 # Largura da tela
ALTURA = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos
METEORO_LARGURA= 50
METEORO_ALTURA = 38

METEORO2_LARGURA= 100
METEORO2_ALTURA = 76

TIRO_LARGURA = 20
TIRO_ALTURA = 50

NAVE_LARGURA = 60
NAVE_ALTURA = 48

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

