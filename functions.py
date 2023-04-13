import graphics
import time
import pygame
from pygame.locals import *
import random

Tcards = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', '10C', '10D', '10H', '10S', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS', 'AC', 'AD', 'AH', 'AS',]

# deals hand to user, adding the card and value to its class member
def deal(UHand):
  card = ""
  while (card == ""):
    card = random.choice(Tcards)
    Tcards.remove(card)
  
  UHand.add_cardF(card)
  if int(card[0]) > 73 or card[0] == '1':
    UHand.add_cardV(10)
  elif int(card[0]) == 65:
    UHand.add_cardV(11)
  else:
    UHand.add_cardV(int(card[0]))

# gets total of hand
def total(UHand):
  cards = UHand.get_cardV()
  total = 0
  for i in range(len(cards)):
    total += cards[i]

  return total

# need to look into what this function does
def draw(x, y, UHand):
  new = nextCard(userHand)
  graphics.draw_card(x, y, new)
  x = x+72
  return x

# checks if ace in pack and swaps value to one
def aceD(UHand, total):
  cards = UHand.get_cardV()
  if total > 21:
    if 11 in cards:
      index = cards.index(11)
      cards[index] = 1
      UHand.set_cardV(cards)

# need to look into and possibly make better changes for self
def dealerMove(UHand, x, y):
  total = total(UHand)

  while (total < 17):
    deal(UHand)
    x = draw(x, y, UHand)
    total = total(UHand)
    aceD(UHand, total)
    total = total(UHand)
    graphics.displayT(str(total), x, 13)
    time.sleep(3)

  return x

# gets last card
def lastCard(UHand):
  tcards = UHand.get_cardF()
  card = tcards[len(tcards)-1]
  return card




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