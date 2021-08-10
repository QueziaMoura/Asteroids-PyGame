import random
import pygame
from config import LARGURA, ALTURA, METEORO_LARGURA, METEORO_ALTURA, METEORO2_LARGURA,METEORO2_ALTURA, NAVE_LARGURA, NAVE_ALTURA
from assets import NAVE_IMG, PEW_SOUND, METEOR_IMG, METEOR2_IMG, PEW_SOUND, TIRO_IMG, EXPLOSAO_ANIM


class Nave(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[NAVE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y -= self.speedy

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            novo_tiro = Tiro(self.assets, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(novo_tiro)
            self.groups['all_bullets'].add(novo_tiro)
            self.assets[PEW_SOUND].play()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[METEOR_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA-METEORO_LARGURA)
        self.rect.y = random.randint(-100, -METEORO_LARGURA)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            self.rect.x = random.randint(0, LARGURA-METEORO_LARGURA)
            self.rect.y = random.randint(-100, -METEORO_LARGURA)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            self.rect.x = random.randint(0, LARGURA-METEORO_LARGURA)
            self.rect.y = random.randint(-100, -METEORO_LARGURA)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)


class Meteor2(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[METEOR2_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA-METEORO2_LARGURA)
        self.rect.y = random.randint(-100, -METEORO2_LARGURA)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            self.rect.x = random.randint(0, LARGURA-METEORO2_LARGURA)
            self.rect.y = random.randint(-100, -METEORO2_LARGURA)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)


# Classe Tiro que representa os tiros
class Tiro(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[TIRO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

# Classe que representa uma explosão de meteoro
class Explosion(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = assets[EXPLOSAO_ANIM]

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
