#Matthew Bianchi

import pygame
from pygame.locals import *
from sys import exit
pygame.init()

screen = pygame.display.set_mode((720,480), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('Blackjack')
clock = pygame.time.Clock()

background = pygame.image.load('graphics/table.png')
background = pygame.transform.scale(background, screen.get_size())
screen.blit(background,(0,0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
            screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
            pygame.display.flip()
            
            
    pygame.display.update()
    clock.tick(60)