# John Kutbay

import random

test = "Hello"

def init():
    global cards
    cards = []
    global users
    global dealers
    users = []
    dealers = []
    global cardV
    global cardS
    cardV = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardS = ["P", "S", "C", "H"]
    for i in range(0,52):
        cards.append(0)

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




init()

print("WELCOME TO BLACKJACK!")
print('\n')

deal(2,1)
print("You have cards: ", end = '')
for i in range(len(users)):
  print(users[i] + " ", end = '')
print("(" + str(score(1)) + ")", end = '\n')

if score(1) == 21:
  print("Player wins!\n")
  exit(0)

deal(2, 2)
print("Dealer has cards: ", end = '')
for i in range(len(dealers)):
  print(dealers[i] + " ", end = '')
print("(" + str(score(2)) + ")", end = '\n')

if score(2) == 21:
  print("Dealer wins!\n")
  exit(0)

while True:

  hitStand = input("Hit or Stand?(h or s) ")
  
  if hitStand == 'h':
    deal(1,1)
    print("You have cards: ", end = '')
    for i in range(len(users)):
      print(users[i] + " ", end = '')
    print("(" + str(score(1)) + ")", end = '\n')

    if score(1) > 21:
      print("Player busts, Dealer wins!\n")
      exit(0)
    elif score(1) == 21:
      print("Player wins!\n")
      exit(0)

  elif hitStand == 's':

    while score(2) < 17 or score(2) < score(1):
      print("Dealer Hits! ", end = '')
      deal(1,2)
      for i in range(len(dealers)):
        print(dealers[i] + " ", end = '')
      print("(" + str(score(2)) + ")", end = '\n')

    if score(2) == 21:
      print("Dealer wins!\n")
      exit(0)
    elif score(2) > 21:
      print("Dealer busts!\n")
      exit(0)
    else:
      print("Dealer Stands.\n")
      break

if score(1) == score(2):
  print("Game is a draw!\n")
  exit(0)









