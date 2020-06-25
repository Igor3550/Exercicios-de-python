# faça um programa  que abra e reproduza o audio de um arquuivo mp3
import pygame
pygame.init()
screen = pygame.display.set_mode((300, 100))
music = pygame.mixer.Sound('ex021.wav')

sair = False
while not sair:

    music.play()
    music.set_volume(0.2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sair = True
