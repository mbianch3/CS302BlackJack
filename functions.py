import pygame
from pygame.locals import *
import sys
import random
global screen
X=1080
Y=720
pygame.init()

# DISPLAY:
def startWindow():
  global screen
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/startscreen.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  
def startmouse(mouse, sbwidth, sbheight, sbcolorD, sbcolorL, sbtext):
  if (X/2)-(sbwidth/2) <= mouse[0] <= (X/2)+(sbwidth/2) and (Y/2)-(sbheight/2) <= mouse[1] <= (Y/2)+(sbheight/2):
    startButton = pygame.image.load('graphics/buttons/startButtonL.png').convert_alpha()
  else:
    startButton = pygame.image.load('graphics/buttons/startButton.png').convert_alpha()
  startButton = pygame.transform.scale(startButton, (sbwidth, sbheight))
  screen.blit(startButton, (X/2 - sbwidth/2 + X/43, Y/2 - sbheight/2))

def dealmouse(mouse, dbwidth, dbheight, dbcolorD, dbcolorL, dbtext):
  if (X/2)-(dbwidth/2) <= mouse[0] <= (X/2)+(dbwidth/2) and (Y/2)-(dbheight) <= mouse[1] <= (Y/2):
    dealButton = pygame.image.load('graphics/buttons/dealButtonL.png').convert_alpha()
  else:
    dealButton = pygame.image.load('graphics/buttons/dealButton.png').convert_alpha()
  dealButton = pygame.transform.scale(dealButton, (dbwidth,dbheight))
  screen.blit(dealButton, (X/2-dbwidth/2, Y/2-dbheight))

def hitmouse(mouse, hwidth, hheight, hcolorD, hcolorL, htext):
  if (X/2)-(3*hwidth/2)-100 <= mouse[0] <= (X/2)-(3*hwidth/2)+hwidth-100 and (Y/2)-(hheight) <= mouse[1] <= (Y/2):
    hitButton = pygame.image.load('graphics/buttons/hitButtonL.png').convert_alpha()
  else:
    hitButton = pygame.image.load('graphics/buttons/hitButton.png').convert_alpha()
  hitButton = pygame.transform.scale(hitButton, (hwidth, hheight))
  screen.blit(hitButton, ((X/2)-(3*hwidth/2)-100, (Y/2)-(hheight)))

def standmouse(mouse, swidth, sheight, scolorD, scolorL, stext):
  if (X/2)+(swidth/2)+100 <= mouse[0] <= (X/2)+(swidth/2)+swidth+100 and (Y/2)-(sheight) <= mouse[1] <= (Y/2):
    standButton = pygame.image.load('graphics/buttons/standButtonL.png').convert_alpha()
  else:
    standButton = pygame.image.load('graphics/buttons/standButton.png').convert_alpha()
  standButton = pygame.transform.scale(standButton, (swidth, sheight))
  screen.blit(standButton, ((X/2)+(swidth/2)+100, (Y/2)-(sheight)))
  
def gameOvermouse(mouse, gowidth, goheight, dbcolorD, dbcolorL, dbtext):
  if (X/2)-(gowidth/2) <= mouse[0] <= (X/2)+(gowidth/2) and (Y/2)-(goheight) <= mouse[1] <= (Y/2):
    gameOverButton = pygame.image.load('graphics/buttons/gameOverButtonL.png').convert_alpha()
  else:
    gameOverButton = pygame.image.load('graphics/buttons/gameOverButton.png').convert_alpha()
  gameOverButton = pygame.transform.scale(gameOverButton, (gowidth,goheight))
  screen.blit(gameOverButton, (X/2-gowidth/2, Y/2-goheight))
  
def playAgainmouse(mouse, pawidth, paheight, pacolorD, dbcolorL, dbtext):
  if (X/2)-(pawidth/2) <= mouse[0] <= (X/2)+(pawidth/2) and (Y/2)-(paheight) <= mouse[1] <= (Y/2):
    playAgainButton = pygame.image.load('graphics/buttons/playAgainButtonL.png').convert_alpha()
  else:
    playAgainButton = pygame.image.load('graphics/buttons/playAgainButton.png').convert_alpha()
  playAgainButton = pygame.transform.scale(playAgainButton, (pawidth,paheight))
  screen.blit(playAgainButton, (X/2-pawidth/2, Y/2-paheight))

def chipMouse(mouse, val, chip, cwidth, cheight, xpos, ypos):
  if True:
    mouse


def gameWindow():
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/newtable.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  pygame.display.flip()
  return [screen, background]

def displayText(text, x, y, size):
  Font = pygame.font.SysFont('arialblack', size)
  Text = Font.render(text, True, 'black')
  TextRect = Text.get_rect()
  TextRect.center = (x,y)
  screen.blit(Text,TextRect)


