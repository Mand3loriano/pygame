import pygame 
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('fundo.mp3')
barulho_colisao = pygame.mixer.Sound('colisão.wav')
pygame.mixer.music.play(-1)


largura = 640 
altura = 480

x = largura/2
y = altura/2

x_azul = randint(40,600)
y_azul = randint(50,430)

fonte = pygame.font.SysFont('gabriola', 40, True, True)

tela = pygame.display.set_mode((largura,altura)) 
pygame.display.set_caption('ola mundo')
temp = pygame.time.Clock()

pontos = 0
while True:
    temp.tick(30)
    tela.fill((0,0,0))
    msg = f'Pontos: {pontos}'
    texto = fonte.render(msg, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            pygame.quit() 
            exit()

    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20
    if pygame.key.get_pressed()[K_UP]:
        y = y - 20
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 20

    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    red = pygame.draw.rect(tela, (255,255,0), (x,y,40,50))
    blue = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    if red.colliderect(blue):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos + 1
        barulho_colisao.play()
    tela.blit(texto, (450,40))
    pygame.display.update()
