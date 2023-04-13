#Matthew Bianchi

import pygame
from pygame.locals import *
from pygame import mixer # for music if want
from sys import exit
from cards import cards
import random


mixer.pre_init(44100, -16, -2, 2048) # need to look into what this does
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