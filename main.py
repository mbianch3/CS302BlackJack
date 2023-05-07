# John Kutbay
# Matthew Bianchi

import pygame
from pygame.locals import *
import sys
import time
import MBfunctions
from button import Button
from button import chipButton
import random

# def init():
#     global users
#     global dealers
#     global cards
#     users = []
#     dealers = []
#     cards = []
#     cards = MBfunctions.initcards(cards)
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

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        faceCards = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        return f"{faceCards.get(self.value, str(self.value))}{self.suit}"

class CardDeck:
    
    def __init__(self, n=52):
        self.size = n * 4
        self.deck = [Card((i % 13) + 1, suit) for i in range(n) for suit in ['H', 'D', 'C', 'S']]
    #Shuffles Deck
    def shuffle(self):
        random.shuffle(self.deck)
        
    #Prints deck to console
    def display(self):
        print(*self.deck)
    #Deals cards
    
    def deal(self, hand):
        new_hand = hand + [self.deck[0]]
        self.deck.pop(0)
        self.size += -1
        return new_hand

    def handValue(self, hand):
        handTotal = 0
        #Calculates Values for 2 through K
        for card in hand:
            if card.value > 9:
                handTotal += 10
            elif card.value > 1:
                handTotal += card.value
        #Deals with Ace Values
        for card in hand:
            if card.value == 1:
                if handTotal + 11 > 21:
                    handTotal += 1
                else:
                    handTotal += 11
        return handTotal
    
    def drawDealerValue(self, value):
        font = pygame.font.Font('freesansbold.ttf', 32)
        dealerValueText = font.render(f"Hand Value: {value}", True, 'black')
        dealerValueRect = dealerValueText.get_rect()
        dealerValueRect.center = (screen.get_width() // 2, screen.get_height() // 3)
        screen.blit(dealerValueText, dealerValueRect)
    
    def drawPlayerValue(self, value):
        font = pygame.font.Font('freesansbold.ttf', 32)
        playerValueText = font.render(f"Hand Value: {value}", True, 'black')
        playerValueRect = playerValueText.get_rect()
        playerValueRect.center = (screen.get_width() // 2, screen.get_height() // 1.5)
        screen.blit(playerValueText, playerValueRect)  
        
    #Used for updating images
    def drawScreen(self, player, dealer):
        width = screen.get_width()
        deck.drawPlayerHand(player)
        for i in range(len(dealer)):
            card = pygame.image.load(cardsPics(dealer[i])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            screen.blit(card , (width//2-90 + 30*i ,5*i))
        deck.drawDealerValue(deck.handValue(dealer))
        deck.drawPlayerValue(deck.handValue(player))
    
    #Used for updating images
    def drawPlayerHand(self, player):
        width = screen.get_width()
        for i in range(len(player)):
            card = pygame.image.load(cardsPics(player[i])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            screen.blit(card , (width//2-90 + 30*(i) ,540 - 5*(i)))
        deck.drawPlayerValue(deck.handValue(player))
        
    def drawDealerHand(self, dealer):
        width = screen.get_width()
        cardback = pygame.image.load('graphics/cards/cardback.png').convert_alpha()
        cardback = pygame.transform.scale(cardback, (112.5, 164))
        screen.blit(cardback, (width//2-90 + 30*0 ,5*0))
        card = pygame.image.load(cardsPics(dealer[1])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        screen.blit(card , (width//2-90 + 30, 5))

    
    #Used for hitting        
    def displayPlayerHand(self, hand):
        width = screen.get_width()
        pygame.time.delay(250)
        card = pygame.image.load(cardsPics(hand[len(hand) - 1])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        screen.blit(card , (width//2-90 + 30*(len(hand) - 1) ,540-5*(len(hand) - 1)))
        pygame.display.update()
    
    #Used for hitting
    def displayDealerHand(self, hand):
        width = screen.get_width()
        height = screen.get_height()
        for i in range(len(hand)):
            if(i >= (len(hand) - 1) and i > 1):
                pygame.time.delay(300)
                card = pygame.image.load(cardsPics(hand[i])).convert_alpha()
                card = pygame.transform.scale(card, (112.5, 164))
                screen.blit(card , (width//2-90 + 30*i ,5*i))
                pygame.display.update()
            elif(len(hand) <= 2):
                card = pygame.image.load(cardsPics(hand[i])).convert_alpha()
                card = pygame.transform.scale(card, (112.5, 164))
                screen.blit(card , (width//2-90 + 30*i ,5*i))
                pygame.display.update()
                
    def initialDeal(self, player, dealer):
            width = screen.get_width()
            height = screen.get_height()
            
            pygame.time.delay(250)
            card = pygame.image.load(cardsPics(player[0])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            screen.blit(card , (width//2-90 + 30*(0) ,540 - 5*(0)))
            pygame.display.update()
            
            pygame.time.delay(250)
            cardback = pygame.image.load('graphics/cards/cardback.png').convert_alpha()
            cardback = pygame.transform.scale(cardback, (112.5, 164))
            screen.blit(cardback, (width//2-90 + 30*0 ,5*0))
            pygame.display.update()
            
            pygame.time.delay(250)
            card = pygame.image.load(cardsPics(player[1])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            screen.blit(card , (width//2-90 + 30*(1) ,540 - 5*(1)))
            pygame.display.update()
            
            pygame.time.delay(250)
            card = pygame.image.load(cardsPics(dealer[1])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            screen.blit(card , (width//2-90 + 30, 5))
            pygame.display.update()
            
            
        
            
    def winCheck(self):
        #Deals with win conditions
        if deck.handValue(player) > deck.handValue(dealer) and deck.handValue(player) <= 21:
            #print("Player Wins!\n")
            return "Player Wins!"
            #playerWin += 1
        elif deck.handValue(player) < deck.handValue(dealer) and deck.handValue(dealer) <= 21:
            #print("Dealer Wins!\n")
            return "Dealer Wins!"
            #dealerWin += 1
        elif deck.handValue(player) == deck.handValue(dealer):
            #print("Push!\n")
            return "Push!"
            #tie += 1
            
    def drawChips(self, chipSet, bank):
        i = 0
        chipButtons = []
        for val, chip in chipSet.items():
            if val <= bank:
                chipImage = pygame.image.load(chip).convert_alpha()
                #chipImage.pygame.PixelArray.PixelArray()
                chipImage = pygame.transform.scale(chipImage, (85, 85))
                screen.blit(chipImage, (5 + 90*i, screen.get_height() - 110))
                i += 1
                chipButtons.append(chipButton(val, chip, 85, 85, 5 + 90*i, 610))
        return chipButtons
    
    def displayMoney(self, bet):
        font = pygame.font.Font('freesansbold.ttf', 32)
        betText = font.render(f"BET: {bet}", True, 'black')
        betTextRect = betText.get_rect()
        betTextRect.center = (screen.get_width() // 5, screen.get_height() // 1.25)
        screen.blit(betText, betTextRect)
        
        bankText = font.render(f"BANK: {bank}", True, 'black')
        bankTextRect = bankText.get_rect()
        bankTextRect.center = (screen.get_width() // 5, screen.get_height() // 8)
        screen.blit(bankText, bankTextRect)
        
pygame.init()
clock=pygame.time.Clock()
X=1080
Y=720

# pygame window:
MBfunctions.startWindow()

# Intial text:
MBfunctions.displayText('Blackjack', int(X/2), int(Y/5), int(X/10))

# Initial Start Button:
# def __init__(self,font,color,colorL,colorD,width,height,text)
startButton = Button(None, (192,192,192), (128,128,128), 250, 100, pygame.font.Font('freesansbold.ttf', int(X/16)).render('Start', True, (255,255,255)))

chipSet = {10 : 'graphics/chips/green10Chip.png', 20 : 'graphics/chips/blue20Chip.png', 50 : 'graphics/chips/red50Chip.png', 100 : 'graphics/chips/black100Chip.png', 500 : 'graphics/chips/grey500Chip.png'}

bank = 1000


run = True
while run == True:
    mouse = pygame.mouse.get_pos()
    MBfunctions.startmouse(mouse, startButton.width, startButton.height, startButton.colorD, startButton.colorL, startButton.text)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (X/2)-(startButton.width/2) <= mouse[0] <= (X/2)-(startButton.width/2)+startButton.width and (Y/2)-(startButton.height/2) <= mouse[1] <= (Y/2)-(startButton.height/2)+startButton.height:
                run = False
                break
    pygame.display.flip()

tmp = MBfunctions.gameWindow()
screen = tmp[0]
background = tmp[1]

deck = CardDeck()
deck.shuffle()

playerTurn = True
winner = None
start = True
gameOver = False
betting = True
player = []
dealer = []

bet = 0

# def __init__(self,font,color,colorL,colorD,width,height,text)
dealButton = Button(None, None, None, 150, 75, None)
hitButton = Button(None, None, None, 150, 75, None)
standButton = Button(None, None, None, 150, 75, None)
GameOverButton = Button(None, None, None, 150, 75, None)
playAgainButton = Button(None, None, None, 150, 75, None)

pygame.display.flip()
while True:
        
    mouse = pygame.mouse.get_pos()
    if gameOver == True:
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
        start = False
        MBfunctions.gameOvermouse(mouse, GameOverButton.width, GameOverButton.height, GameOverButton.colorD, GameOverButton.colorL, GameOverButton.text)  
    elif start == True:
        winner = None
        betting = True
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
        chipButtons = deck.drawChips(chipSet, bank)
        
        deck.displayMoney(bet)
        
        if(bet > 0):
            MBfunctions.dealmouse(mouse, dealButton.width, dealButton.height, dealButton.colorD, dealButton.colorL, dealButton.text)
            playerTurn = True
    elif winner == None and playerTurn == True and start == False:
        MBfunctions.hitmouse(mouse, hitButton.width, hitButton.height, hitButton.colorD, hitButton.colorL, hitButton.text)
        MBfunctions.standmouse(mouse, standButton.width, standButton.height, standButton.colorD, standButton.colorL, standButton.text)
    elif winner != None and start == False and playerTurn == False:
        MBfunctions.playAgainmouse(mouse, playAgainButton.width, playAgainButton.height, playAgainButton.colorD, playAgainButton.colorL, playAgainButton.text)

    if deck.size < 15:
        del deck
        deck = CardDeck()
        for i in range(random.randint(1, 10)):
            deck.shuffle()

    for event in pygame.event.get():
        if gameOver == True and event.type == pygame.MOUSEBUTTONDOWN:
            if (X/2)-(GameOverButton.width/2) <= mouse[0] <= (X/2)-(GameOverButton.width/2)+GameOverButton.width and (Y/2)-(GameOverButton.height/2) <= mouse[1] <= (Y/2)-(GameOverButton.height/2)+GameOverButton.height:
                pygame.quit()
                exit()
        if start == False and playerTurn == False and winner != None and event.type == pygame.MOUSEBUTTONDOWN and gameOver == False:
            if (X/2)-(playAgainButton.width/2) <= mouse[0] <= (X/2)-(playAgainButton.width/2)+playAgainButton.width and (Y/2)-(playAgainButton.height/2) <= mouse[1] <= (Y/2)-(playAgainButton.height/2)+playAgainButton.height:
                start = True
                winner = None
                if(bank < 10):
                    gameOver = True
        if betting == True and event.type == pygame.MOUSEBUTTONDOWN and gameOver == False:
            if 5 <= mouse[0] <= 90 and 610 <= mouse[1] <= 695 and bank - 10 >= 0:
                bank = bank - 10
                bet += 10
            if 95 <= mouse[0] <= 185 and 610 <= mouse[1] <= 695 and bank - 20 >= 0:
                bank = bank - 20
                bet += 20
            if 190 <= mouse[0] <= 280 and 610 <= mouse[1] <= 695 and bank - 50 >= 0:
                bank = bank - 50
                bet += 50
            if 285 <= mouse[0] <= 375 and 610 <= mouse[1] <= 695 and bank - 100 >= 0:
                bank = bank - 100
                bet += 100
            if 380 <= mouse[0] <= 470 and 610 <= mouse[1] <= 695 and bank - 500 >= 0:
                bank = bank - 500
                bet += 500
        if playerTurn == True and winner == None and event.type == pygame.MOUSEBUTTONDOWN and start == True and gameOver == False:
            if (X/2)-(dealButton.width/2) <= mouse[0] <= (X/2)-(dealButton.width/2)+dealButton.width and (Y/2)-(dealButton.height/2) <= mouse[1] <= (Y/2)-(dealButton.height/2)+dealButton.height:
                screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
                betting = False
                start = False
                #Uses a list to create the player and dealer's hand arrays
                player = []
                dealer = []
                deck.displayMoney(bet)
                #Deals starting Hands
                player = deck.deal(player)
                dealer = deck.deal(dealer)
                player = deck.deal(player)
                dealer = deck.deal(dealer)

                deck.initialDeal(player, dealer)
                
                deck.drawPlayerValue(deck.handValue(player))
                
                if deck.handValue(player) == 21:
                    if deck.handValue(dealer) == 21:
                        winner = "Push!"
                    else:
                        winner = "Player Blackjack!"
                        bank += int(2.5*bet)
                    playerTurn = False
                    pygame.time.delay(300)
                    deck.displayDealerHand(dealer)
                pygame.time.delay(300)
                pygame.display.flip()
                
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #Player Hit and Standing
        if playerTurn == True and event.type == pygame.MOUSEBUTTONDOWN and winner == None and gameOver == False and betting == False:
            if ((X/2)-(3*hitButton.width/2) - 100) <= mouse[0] <= ((X/2)-(3*hitButton.width/2) - 100 + hitButton.width) and (Y/2)-(hitButton.height) <= mouse[1] <= (Y/2):
                player = deck.deal(player)
                screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
                deck.drawPlayerHand(player)
                deck.drawDealerHand(dealer)
                deck.displayPlayerHand(player)
                deck.displayMoney(bet)
                pygame.display.update()

                if deck.handValue(player) > 21:
                    playerTurn = False
                    winner = "Dealer Wins!"
                    
            if playerTurn == True and (X/2)+(standButton.width/2) + 100 <= mouse[0] <= (X/2)+(standButton.width/2)+standButton.width + 100 and (Y/2)-(standButton.height) <= mouse[1] <= (Y/2):
                playerTurn = False

        #Dealer's turn
        if deck.handValue(player) <= 21 and playerTurn == False and winner == None and betting == False and start == False and gameOver == False and deck.handValue(dealer) <= 21:
            #Delays revealing the first card so it isn't instantaneous
            pygame.time.delay(300)
            deck.displayDealerHand(dealer)
            if deck.handValue(dealer) < 17:
                dealer = deck.deal(dealer)
                deck.displayDealerHand(dealer)
            if deck.handValue(dealer) > 21:
                winner = "Player Wins!"
                
        #Deals with win cases
        if playerTurn == False and deck.handValue(dealer) >= 17 and winner == None and gameOver == False:
            winner = deck.winCheck()
            
        if winner != None and start == False and bet != 0 and gameOver == False:
            screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
            if winner == "Player Wins!":
                bank += 2*bet
            if winner == "Push!":
                bank += bet
            pygame.time.delay(300)
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(winner, True, 'black')
            deck.drawScreen(player, dealer)
            textRect = text.get_rect()
            textRect.center = (screen.get_width() // 2, screen.get_height() // 1.75)
            screen.blit(text, textRect)
            bet = 0
            deck.displayMoney(bet)
            player = []
            dealer = []

    pygame.display.update()
    
    



