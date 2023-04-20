# John Kutbay

import pygame
from pygame.locals import *
import sys
import time
import functions
from button import Button

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
#def __init__(self,font,color,colorL,colorD,width,height,text)
startButton = Button(pygame.font.SysFont('arialblack', int(X/16)), (160,160,160), (192,192,192), (128,128,128), 250, 100, pygame.font.SysFont('arialblack', int(X/16)).render('Start', True, (255,255,255)))
#sbfont = pygame.font.SysFont('arialblack', int(X/16))
#sbcolor = (160,160,160)
#sbcolorL = (192,192,192)
#sbcolorD = (128,128,128)
#sbwidth = 250
#sbheight = 100
#sbtext = sbfont.render('Start', True, (255,255,255))

pygame.display.flip()

run = True
while run == True:
    mouse = pygame.mouse.get_pos()
    functions.startmouse(mouse, startButton.width, startButton.height, startButton.color, startButton.colorD, startButton.colorL, startButton.text)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (X/2)-(startButton.width/2) <= mouse[0] <= (X/2)-(startButton.width/2)+startButton.width and (Y/2)-(startButton.height/2) <= mouse[1] <= (Y/2)-(startButton.height/2)+startButton.height:
                run = False
                break
    pygame.display.flip()

# while the game is being played
while True:
    # start with initial dealings
    init()
    users = functions.deal(2,1,users,cards)
    dealers = functions.deal(2,2,dealers,cards)
    quit()



