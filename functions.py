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
  background = pygame.image.load('graphics/testscreen.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  
def startmouse(mouse, sbwidth, sbheight, sbcolorD, sbcolorL, sbtext):
  if (X/2)-(sbwidth/2) <= mouse[0] <= (X/2)+(sbwidth/2) and (Y/2)+sbheight <= mouse[1] <= (Y/2)+2*sbheight:
    pygame.draw.rect(screen, sbcolorL,[(X/2)-(sbwidth/2),(Y/2)+sbheight,sbwidth,sbheight] ,0,7)
  else:
    pygame.draw.rect(screen,sbcolorD,[(X/2)-(sbwidth/2),(Y/2)+sbheight,sbwidth,sbheight],0,7)
  screen.blit(sbtext, (X/2 - sbwidth/2 + X/43, Y/2+sbheight))

def dealmouse(mouse, dbwidth, dbheight, dbcolorD, dbcolorL, dbtext):
  if (X/2)-(dbwidth/2) <= mouse[0] <= (X/2)+(dbwidth/2) and (Y/2)-(dbheight) <= mouse[1] <= (Y/2):
    pygame.draw.rect(screen, dbcolorL,[(X/2)-(dbwidth/2),(Y/2)-(dbheight),dbwidth,dbheight] ,0,7)
  else:
    pygame.draw.rect(screen,dbcolorD,[(X/2)-(dbwidth/2),(Y/2)-(dbheight),dbwidth,dbheight],0,7)
  screen.blit(dbtext, (X/2 - dbwidth/2 + X/35, Y/2 - dbheight+X/90))

def hitmouse(mouse, hwidth, hheight, hcolorD, hcolorL, htext):
  if (X/2)-(3*hwidth/2) <= mouse[0] <= (X/2)-(3*hwidth/2)+hwidth and (Y/2)-(hheight) <= mouse[1] <= (Y/2):
    pygame.draw.rect(screen, hcolorL,[(X/2)-(3*hwidth/2),(Y/2)-(hheight),hwidth,hheight] ,0,7)
  else:
    pygame.draw.rect(screen,hcolorD,[(X/2)-(3*hwidth/2),(Y/2)-(hheight),hwidth,hheight],0,7)
  screen.blit(htext, ((X/2)-3*hwidth/2 + X/25, Y/2 - hheight + Y/72))

def standmouse(mouse, swidth, sheight, scolorD, scolorL, stext):
  if (X/2)+(swidth/2) <= mouse[0] <= (X/2)+(swidth/2)+swidth and (Y/2)-(sheight) <= mouse[1] <= (Y/2):
    pygame.draw.rect(screen, scolorL,[(X/2)+(swidth/2),(Y/2)-(sheight),swidth,sheight] ,0,7)
  else:
    pygame.draw.rect(screen,scolorD,[(X/2)+(swidth/2),(Y/2)-(sheight),swidth,sheight],0,7)
  screen.blit(stext, (X/2 + swidth/2 + X/40, Y/2 - sheight + Y/72))

def gameWindow():
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/newtable.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  pygame.display.flip()
  return [screen, background]

def displayText(text, x, y, size):
  Font = pygame.font.SysFont('arialblack', size)
  Text = Font.render(text, True, (255,255,255))
  TextRect = Text.get_rect()
  TextRect.center = (x,y)
  screen.blit(Text,TextRect)


