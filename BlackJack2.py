import random

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
    cardS = ["D", "S", "C", "H"]

    for i in range(0,52):
        cards.append(0)

def deal(num, player):
  for i in range(0,num):
    cardN = random.randint(0,9)
    while cards[cardN] != 0:
      cardN = random.randint(0,9)
    cards[cardN] = player
    if player == 1:
      users.append(cardV[int(cardN % 13) + cardS[int(cardN / 13)]])
    else:
      dealers.append(cardV[int(cardN % 13) + cardS[int(cardN / 13)]])
    
def score(player):
  





def main():
  
  while True:
    init()

    print("WELCOME TO BLACKJACK!")
    print('\n')

    deal(2, 2)
    print("Dealer has cards: ", end = '')
    for i in len(dealers):
      print(dealers[i] + " ", end = '')
    print('\n')










main()




