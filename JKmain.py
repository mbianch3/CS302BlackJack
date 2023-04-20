# John Kutbay

import pygame
from pygame.locals import *
import sys
import time
import functions

def init():
    global users
    global dealers
    global cards
    users = []
    dealers = []
    cards = []
    cards = functions.initcards(cards)
    

pygame.init()
clock=pygame.time.Clock()
X=1080
Y=720

# pygame window:
functions.startWindow()

# Intial text:
functions.displayText('Welcome To Blackjack!', int(X/2), int(Y/5), int(X/20))

# Initial Start Button:
sbfont = pygame.font.SysFont('arialblack', int(X/16))
sbcolor = (160,160,160)
sbcolorL = (192,192,192)
sbcolorD = (128,128,128)
sbwidth = 250
sbheight = 100
sbtext = sbfont.render('Start', True, (255,255,255))

pygame.display.flip()

run = True

while run == True:
    mouse = pygame.mouse.get_pos()
    functions.startmouse(mouse, sbwidth, sbheight, sbcolor, sbcolorD, sbcolorL, sbtext)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (X/2)-(sbwidth/2) <= mouse[0] <= (X/2)-(sbwidth/2)+sbwidth and (Y/2)-(sbheight/2) <= mouse[1] <= (Y/2)-(sbheight/2)+sbheight:
                run = False
                break
    pygame.display.flip()



