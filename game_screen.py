import pygame
from config import FPS, LARGURA, ALTURA, BLACK, GREEN, RED
from assets import load_assets, DESTRUICAO_SOM, EXPLOSAO_SOM, FUNDO, PONTOS_FONT
from sprites import Nave, Meteor, Tiro, Explosion


def game_screen(janela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_meteors = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()

    groups = {}

    groups['all_sprites'] = all_sprites
    groups['all_meteors'] = all_meteors
    groups['all_bullets'] = all_bullets
    

    # Criando o jogador
    player = Nave(groups, assets)
    all_sprites.add(player)

    # Criando os meteoros
    for i in range(6):
        meteor = Meteor(assets,1)
        all_sprites.add(meteor)
        all_meteors.add(meteor)

    # Criando meteoros que tira duas vidas
    for i in range(2):
        meteor = Meteor(assets,2)
        all_sprites.add(meteor)
        all_meteors.add(meteor)


    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    estado = PLAYING

    keys_down = {}
    pontos = 0
    vidas = 5

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while estado != DONE:
        clock.tick(FPS)
        
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                estado = DONE
            # Só verifica o teclado se está no estado de jogo
            if estado == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_DOWN:
                        player.speedy -= 8
                    if event.key == pygame.K_UP:
                        player.speedy += 8
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
                        if event.key == pygame.K_DOWN:
                            player.speedy += 8
                        if event.key == pygame.K_UP:
                            player.speedy -= 8


        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        if estado == PLAYING:
            # Verifica se houve colisão entre tiro e meteoro
            hits = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True, pygame.sprite.collide_mask)
            for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                assets[DESTRUICAO_SOM].play()
                m = Meteor(assets, meteor.forca)
                all_sprites.add(m)
                all_meteors.add(m)

                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(meteor.rect.center, assets)
                all_sprites.add(explosao)

                # Ganhou pontos!
                pontos += 100
                if pontos % 1000 == 0:
                    vidas += 1
                if pontos % 1500 == 0:
                    # Criando os meteoros:
                    for i in range(5):
                        meteor = Meteor(assets)
                        all_sprites.add(meteor)
                        all_meteors.add(meteor)

            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, all_meteors, True, pygame.sprite.collide_mask)
            for meteor in hits:
                # Toca o som da colisão
                assets[EXPLOSAO_SOM].play()
                player.kill()
                vidas -= meteor.forca
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                estado = EXPLODING
                keys_down = {}
                momento_explosao = pygame.time.get_ticks()
                explosao_duracao = explosao.frame_ticks * len(explosao.explosion_anim) + 400


        elif estado == EXPLODING:
            now = pygame.time.get_ticks()
            if now - momento_explosao > explosao_duracao:
                if vidas <= 0:
                    estado = DONE
                else:
                    estado = PLAYING
                    player = Nave(groups, assets)
                    all_sprites.add(player)

        # ----- Gera saídas
        janela.fill(BLACK)  # Preenche com a cor branca
        janela.blit(assets[FUNDO], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(janela)

        # Desenhando o score
        text_surface = assets[PONTOS_FONT].render("{:08d}".format(pontos), True, GREEN)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (LARGURA / 2,  10)
        janela.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[PONTOS_FONT].render(chr(9829) * vidas, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, ALTURA - 10)
        janela.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
