import graphics
import time
import pygame
from pygame.locals import *
import random

def newpack():
  cards = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', '10C', '10D', '10H', '10S', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS', 'AC', 'AD', 'AH', 'AS',]
  return cards

def deal(UHand):
  card = ""
  while (card == ""):
    






def deal(num, player):
  for i in range(0,num):
    cardN = random.randint(0,9)
    while cards[cardN] != 0:
      cardN = random.randint(0,9)
    cards[cardN] = player
    if player == 1:
      users.append(cardV[int(cardN % 13)] + cardS[int(cardN / 13)])
    else:
      dealers.append(cardV[int(cardN % 13)] + cardS[int(cardN / 13)])
    
def score(player):
  scoreVal = 0

  for i in range(52):
    if cards[i] == player:
      if (i%13) < 10 and (i%13) != 0:
        scoreVal += (i%13)+1
      elif (i%13) >= 10:
        scoreVal += 10
      else:
        if (scoreVal + 11 > 21):
          scoreVal += 1
        else:
          scoreVal += 11
  return scoreVal