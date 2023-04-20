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
  
def startmouse(mouse, sbwidth, sbheight, sbcolor, sbcolorD, sbcolorL, sbtext):
  if (X/2)-(sbwidth/2) <= mouse[0] <= (X/2)-(sbwidth/2)+sbwidth and (Y/2)-(sbheight/2) <= mouse[1] <= (Y/2)-(sbheight/2)+sbheight:
    pygame.draw.rect(screen, sbcolorL,[(X/2)-(sbwidth/2),(Y/2)-(sbheight/2),sbwidth,sbheight] ,0,7)
  else:
    pygame.draw.rect(screen,sbcolorD,[(X/2)-(sbwidth/2),(Y/2)-(sbheight/2),sbwidth,sbheight],0,7)
  screen.blit(sbtext, (X/2 - sbwidth/2 + 25, Y/2 - sbheight/2))

def gameWindow():
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/SolidBackground.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  pygame.display.flip()

def displayText(text, x, y, size):
  Font = pygame.font.SysFont('arialblack', size)
  Text = Font.render(text, True, (255,255,255))
  TextRect = Text.get_rect()
  TextRect.center = (x,y)
  screen.blit(Text,TextRect)

def cardsPics(cardValue):
    #Converts cardValue to a string for comparison
    cardValue = str(cardValue)
    if cardValue == '2D':
        return 'graphics/cards/diamonds/2_of_diamonds.png'
    if cardValue == '3D':
        return 'graphics/cards/diamonds/3_of_diamonds.png'
    if cardValue == '4D':
        return 'graphics/cards/diamonds/4_of_diamonds.png'
    if cardValue == '5D':
        return 'graphics/cards/diamonds/5_of_diamonds.png'
    if cardValue == '6D':
        return 'graphics/cards/diamonds/6_of_diamonds.png'
    if cardValue == '7D':
        return 'graphics/cards/diamonds/7_of_diamonds.png'
    if cardValue == '8D':
        return 'graphics/cards/diamonds/8_of_diamonds.png'
    if cardValue == '9D':
        return 'graphics/cards/diamonds/9_of_diamonds.png'
    if cardValue == '10D':
        return 'graphics/cards/diamonds/10_of_diamonds.png'
    if cardValue == 'JD':
        return 'graphics/cards/diamonds/jack_of_diamonds.png'
    if cardValue == 'QD':
        return 'graphics/cards/diamonds/queen_of_diamonds.png'
    if cardValue == 'KD':
        return 'graphics/cards/diamonds/king_of_diamonds.png'
    if cardValue == 'AD':
        return 'graphics/cards/diamonds/ace_of_diamonds.png'
    #Clubs
    if cardValue == '2C':
        return 'graphics/cards/clubs/2_of_clubs.png'
    if cardValue == '3C':
        return 'graphics/cards/clubs/3_of_clubs.png'
    if cardValue == '4C':
        return 'graphics/cards/clubs/4_of_clubs.png'
    if cardValue == '5C':
        return 'graphics/cards/clubs/5_of_clubs.png'
    if cardValue == '6C':
        return 'graphics/cards/clubs/6_of_clubs.png'
    if cardValue == '7C':
        return 'graphics/cards/clubs/7_of_clubs.png'
    if cardValue == '8C':
        return 'graphics/cards/clubs/8_of_clubs.png'
    if cardValue == '9C':
        return 'graphics/cards/clubs/9_of_clubs.png'
    if cardValue == '10C':
        return 'graphics/cards/clubs/10_of_clubs.png'
    if cardValue == 'JC':
        return 'graphics/cards/clubs/jack_of_clubs.png'
    if cardValue == 'QC':
        return 'graphics/cards/clubs/queen_of_clubs.png'
    if cardValue == 'KC':
        return 'graphics/cards/clubs/king_of_clubs.png'
    if cardValue == 'AC':
        return 'graphics/cards/clubs/ace_of_clubs.png'
    #Spades
    if cardValue == '2S':
        return 'graphics/cards/spades/2_of_spades.png'
    if cardValue == '3S':
        return 'graphics/cards/spades/3_of_spades.png'
    if cardValue == '4S':
        return 'graphics/cards/spades/4_of_spades.png'
    if cardValue == '5S':
        return 'graphics/cards/spades/5_of_spades.png'
    if cardValue == '6S':
        return 'graphics/cards/spades/6_of_spades.png'
    if cardValue == '7S':
        return 'graphics/cards/spades/7_of_spades.png'
    if cardValue == '8S':
        return 'graphics/cards/spades/8_of_spades.png'
    if cardValue == '9S':
        return 'graphics/cards/spades/9_of_spades.png'
    if cardValue == '10S':
        return 'graphics/cards/spades/10_of_spades.png'
    if cardValue == 'JS':
        return 'graphics/cards/spades/jack_of_spades.png'
    if cardValue == 'QS':
        return 'graphics/cards/spades/queen_of_spades.png'
    if cardValue == 'KS':
        return 'graphics/cards/spades/king_of_spades.png'
    if cardValue == 'AS':
        return 'graphics/cards/spades/ace_of_spades.png'
    #Hearts
    if cardValue == '2H':
        return 'graphics/cards/hearts/2_of_hearts.png'
    if cardValue == '3H':
        return 'graphics/cards/hearts/3_of_hearts.png'
    if cardValue == '4H':
        return 'graphics/cards/hearts/4_of_hearts.png'
    if cardValue == '5H':
        return 'graphics/cards/hearts/5_of_hearts.png'
    if cardValue == '6H':
        return 'graphics/cards/hearts/6_of_hearts.png'
    if cardValue == '7H':
        return 'graphics/cards/hearts/7_of_hearts.png'
    if cardValue == '8H':
        return 'graphics/cards/hearts/8_of_hearts.png'
    if cardValue == '9H':
        return 'graphics/cards/hearts/9_of_hearts.png'
    if cardValue == '10H':
        return 'graphics/cards/hearts/10_of_hearts.png'
    if cardValue == 'JH':
        return 'graphics/cards/hearts/jack_of_hearts.png'
    if cardValue == 'QH':
        return 'graphics/cards/hearts/queen_of_hearts.png'
    if cardValue == 'KH':
        return 'graphics/cards/hearts/king_of_hearts.png'
    if cardValue == 'AH':
        return 'graphics/cards/hearts/ace_of_hearts.png'

# GAME:
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

