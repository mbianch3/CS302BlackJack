import pygame
from pygame.locals import *
import sys
import random
global screen
X=1080
Y=720
pygame.init()

def startWindow():
  global screen
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/table.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  
def startmouse(mouse, sbwidth, sbheight, sbcolor, sbcolorD, sbcolorL, sbtext):
  if (X/2)-(sbwidth/2) <= mouse[0] <= (X/2)-(sbwidth/2)+sbwidth and (Y/2)-(sbheight/2) <= mouse[1] <= (Y/2)-(sbheight/2)+sbheight:
    pygame.draw.rect(screen, sbcolorL,[(X/2)-(sbwidth/2),(Y/2)-(sbheight/2),sbwidth,sbheight] ,0,7)
  else:
    pygame.draw.rect(screen,sbcolorD,[(X/2)-(sbwidth/2),(Y/2)-(sbheight/2),sbwidth,sbheight],0,7)
  screen.blit(sbtext, (X/2 - sbwidth/2 + 25, Y/2 - sbheight/2))

def gameWindow():
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/table.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  pygame.display.flip()

def displayText(text, x, y, size):
  Font = pygame.font.SysFont('arialblack', size)
  Text = Font.render(text, True, (255,255,255))
  TextRect = Text.get_rect()
  TextRect.center = (x,y)
  screen.blit(Text,TextRect)



def initcards(cards):
  for i in range(0,51):
    cards.append(0)
  return cards

def deal(num,player,pcards, cards): 
  for card in range(0,num):
    index = random.randint(0,51)
    while cards[index] != 0:
      index = random.randint(0,51)
    cards[index] = player
    pcards.append(index)
  return pcards
