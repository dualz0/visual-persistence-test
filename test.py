import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((509, 867), 0, 32)
pygame.display.set_caption("test")
cage = pygame.image.load('cage.png').convert_alpha()
bird = pygame.image.load('bird2.png').convert_alpha()
interval = -1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(pygame.image.load('background.png').convert_alpha(), (0, 0))
    if interval < 0:
        screen.blit(cage, (0, 0))
        interval += 2
    else:
        screen.blit(bird, (120, 250))
        interval -= 2
    pygame.display.update()
