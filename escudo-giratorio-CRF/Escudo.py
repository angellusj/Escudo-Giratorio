import pygame
import sys
import math

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Escudo do C.R. Flamengo")

escudo_img = pygame.image.load("escudo-flamengo.png").convert_alpha()

largura_escudo = escudo_img.get_width() // 6
altura_escudo = escudo_img.get_height() // 6
escudo_img = pygame.transform.scale(escudo_img, (largura_escudo, altura_escudo))

escudo_rect = escudo_img.get_rect(center=(largura//2, altura//2))

clock = pygame.time.Clock()

tempo = 0
flip = False

while True:
    for escudo_CRF in pygame.event.get():
        if escudo_CRF.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill((0, 0, 0))

    deslocamento_y = 20 * math.sin(tempo)
    tempo += 0.05

    escala_x = abs(math.cos(tempo))
    escala_x = max(escala_x, 0.05)

    if math.cos(tempo) < 0:
        img_atual = pygame.transform.flip(escudo_img, True, False)
    else:
        img_atual = escudo_img

    nova_largura = int(escudo_rect.width * escala_x)
    nova_altura = escudo_rect.height
    img_redimensionada = pygame.transform.scale(img_atual, (nova_largura, nova_altura))

    novo_rect = img_redimensionada.get_rect(center=(largura//2, altura//2 + deslocamento_y))

    tela.blit(img_redimensionada, novo_rect)

    pygame.display.update()
    clock.tick(60)
