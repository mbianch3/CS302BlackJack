#Various helper functions for buttons/windows/cards
import pygame
from pygame.locals import *
global screen
X=1080
Y=720
pygame.init()

# DISPLAY:
#Used for starting screen background
def startWindow():
  global screen
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/startscreen.png')
  background = pygame.image.load('graphics/startscreen.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))

#Used for actual game screen background  
def gameWindow():
  screen = pygame.display.set_mode((1080,720), HWSURFACE | DOUBLEBUF)
  background = pygame.image.load('graphics/newtable.png')
  background = pygame.transform.scale(background, screen.get_size())
  screen.blit(background, (0,0))
  pygame.display.flip()
  return [screen, background]

#helper functon for displaying Text to screen
def displayText(text, x, y, size):
  Font = pygame.font.SysFont('arialblack', size)
  Text = Font.render(text, True, 'black')
  TextRect = Text.get_rect()
  TextRect.center = (x,y)
  screen.blit(Text,TextRect)

#Returns path location for the image of the corresponding card
def cardsPics(cardValue):
    #convert_alphas cardValue to a string for comparison
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

#The following functions update the buttons to a lighter version of the image if the mouse is hovering over it

#start button function
def startmouse(mouse, sbwidth, sbheight, sbImage, sbImageL):
  if (X/2)-(sbwidth/2) <= mouse[0] <= (X/2)+(sbwidth/2) and (Y/2)-(sbheight) <= mouse[1] <= (Y/2):
    startButton = pygame.image.load(sbImageL).convert_alpha()
  else:
    startButton = pygame.image.load(sbImage).convert_alpha()
  startButton = pygame.transform.scale(startButton, (sbwidth, sbheight))
  screen.blit(startButton, (X/2-sbwidth/2, Y/2-sbheight))
  
#deal button function
def dealmouse(mouse, dbwidth, dbheight, dbImage, dbImageL):
  if (X/2)-(dbwidth/2) <= mouse[0] <= (X/2)+(dbwidth/2) and (Y/2)-(dbheight) <= mouse[1] <= (Y/2):
    dealButton = pygame.image.load(dbImageL).convert_alpha()
  else:
    dealButton = pygame.image.load(dbImage).convert_alpha()
  dealButton = pygame.transform.scale(dealButton, (dbwidth,dbheight))
  screen.blit(dealButton, (X/2-dbwidth/2, Y/2-dbheight))

#hit button function
def hitmouse(mouse, hwidth, hheight, hImage, hImageL):
  if (X/2)-(3*hwidth/2)-100 <= mouse[0] <= (X/2)-(3*hwidth/2)+hwidth-100 and (Y/2)-(hheight) <= mouse[1] <= (Y/2):
    hitButton = pygame.image.load(hImageL).convert_alpha()
  else:
    hitButton = pygame.image.load(hImage).convert_alpha()
  hitButton = pygame.transform.scale(hitButton, (hwidth, hheight))
  screen.blit(hitButton, ((X/2)-(3*hwidth/2)-100, (Y/2)-(hheight)))

#stand button function
def standmouse(mouse, swidth, sheight, sImage, sImageL):
  if (X/2)+(swidth/2)+100 <= mouse[0] <= (X/2)+(swidth/2)+swidth+100 and (Y/2)-(sheight) <= mouse[1] <= (Y/2):
    standButton = pygame.image.load(sImageL).convert_alpha()
  else:
    standButton = pygame.image.load(sImage).convert_alpha()
  standButton = pygame.transform.scale(standButton, (swidth, sheight))
  screen.blit(standButton, ((X/2)+(swidth/2)+100, (Y/2)-(sheight)))

#gameOver button function
def gameOvermouse(mouse, gowidth, goheight, dbImage, dbImageL):
  if (X/2)-(gowidth/2) <= mouse[0] <= (X/2)+(gowidth/2) and (Y/2)-(goheight) <= mouse[1] <= (Y/2):
    gameOverButton = pygame.image.load(dbImageL).convert_alpha()
  else:
    gameOverButton = pygame.image.load(dbImage).convert_alpha()
  gameOverButton = pygame.transform.scale(gameOverButton, (gowidth,goheight))
  screen.blit(gameOverButton, (X/2-gowidth/2, Y/2-goheight))

#play again button function
def playAgainmouse(mouse, pawidth, paheight, paImage, paImageL):
  if (X/2)-(pawidth/2) <= mouse[0] <= (X/2)+(pawidth/2) and (Y/2)-(paheight) <= mouse[1] <= (Y/2):
    playAgainButton = pygame.image.load(paImageL).convert_alpha()
  else:
    playAgainButton = pygame.image.load(paImage).convert_alpha()
  playAgainButton = pygame.transform.scale(playAgainButton, (pawidth,paheight))
  screen.blit(playAgainButton, (X/2-pawidth/2, Y/2-paheight))

#Clear bet Button function  
def clearBetmouse(mouse, cbwidth, cbheight, cbImage, cbImageL):
  if (X/14)-(cbwidth/2) <= mouse[0] <= (X/14)+(cbwidth/2) and (Y/1.2)-(cbheight) <= mouse[1] <= (Y/1.2):
    clearBetButton = pygame.image.load(cbImageL).convert_alpha()
  else:
    clearBetButton = pygame.image.load(cbImage).convert_alpha()
  clearBetButton = pygame.transform.scale(clearBetButton, (cbwidth,cbheight))
  screen.blit(clearBetButton, (X/14-cbwidth/2, Y/1.2-cbheight))

#Chip Button function
def chipMouse(mouse, chipImage, chipImageL, cwidth, cheight, xpos, ypos):
  if xpos <= mouse[0] <= xpos + cwidth and ypos <= mouse[1] <= ypos + cheight:
    chipButton = pygame.image.load(chipImageL).convert_alpha()
  else:
    chipButton = pygame.image.load(chipImage).convert_alpha()
  chipButton = pygame.transform.scale(chipButton, (cwidth, cheight))
  screen.blit(chipButton, (xpos, ypos))

