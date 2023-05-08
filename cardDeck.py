
import pygame
from pygame.locals import *
import functions
from button import chipButton
import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        faceCards = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        return f"{faceCards.get(self.value, str(self.value))}{self.suit}"

class CardDeck:
    
    def __init__(self, screen, n=52):
        self.size = n * 4
        self.deck = [Card((i % 13) + 1, suit) for i in range(n) for suit in ['H', 'D', 'C', 'S']]
        self.screen = screen
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
        dealerValueRect.center = (self.screen.get_width() // 2, self.screen.get_height() // 3)
        self.screen.blit(dealerValueText, dealerValueRect)
    
    def drawPlayerValue(self, value):
        font = pygame.font.Font('freesansbold.ttf', 32)
        playerValueText = font.render(f"Hand Value: {value}", True, 'black')
        playerValueRect = playerValueText.get_rect()
        playerValueRect.center = (self.screen.get_width() // 2, self.screen.get_height() // 1.5)
        self.screen.blit(playerValueText, playerValueRect)  
        
    #Used for updating images
    def drawScreen(self, player, dealer):
        width = self.screen.get_width()
        self.drawPlayerHand(player)
        for i in range(len(dealer)):
            card = pygame.image.load(functions.cardsPics(dealer[i])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            self.screen.blit(card , (width//2-90 + 30*i ,10+5*i))
        self.drawDealerValue(self.handValue(dealer))
        self.drawPlayerValue(self.handValue(player))
    
    #Used for updating images
    def drawPlayerHand(self, player):
        width = self.screen.get_width()
        for i in range(len(player)):
            card = pygame.image.load(functions.cardsPics(player[i])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            self.screen.blit(card , (width//2-90 + 30*(i) ,540 - 5*(i)))
        self.drawPlayerValue(self.handValue(player))
        
    def drawDealerHand(self, dealer):
        width = self.screen.get_width()
        cardback = pygame.image.load('graphics/cards/cardback.png').convert_alpha()
        cardback = pygame.transform.scale(cardback, (112.5, 164))
        self.screen.blit(cardback, (width//2-90 + 30*0 ,10))
        card = pygame.image.load(functions.cardsPics(dealer[1])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        self.screen.blit(card , (width//2-90 + 30, 15))

    
    #Used for hitting        
    def displayPlayerHand(self, hand):
        width = self.screen.get_width()
        pygame.time.delay(250)
        card = pygame.image.load(functions.cardsPics(hand[len(hand) - 1])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        self.screen.blit(card , (width//2-90 + 30*(len(hand) - 1) ,540-5*(len(hand) - 1)))
        pygame.display.update()
    
    #Used for hitting
    def displayDealerHand(self, hand):
        width = self.screen.get_width()
        for i in range(len(hand)):
            if(i >= (len(hand) - 1) and i > 1):
                card = pygame.image.load(functions.cardsPics(hand[i])).convert_alpha()
                card = pygame.transform.scale(card, (112.5, 164))
                self.screen.blit(card , (width//2-90 + 30*i ,10 + 5*i))
                pygame.display.update()
            elif(len(hand) <= 2):
                card = pygame.image.load(functions.cardsPics(hand[i])).convert_alpha()
                card = pygame.transform.scale(card, (112.5, 164))
                self.screen.blit(card , (width//2-90 + 30*i ,10 + 5*i))
                pygame.display.update()
                
    def initialDeal(self, player, dealer):
        width = self.screen.get_width()
        
        pygame.time.delay(250)
        card = pygame.image.load(functions.cardsPics(player[0])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        self.screen.blit(card , (width//2-90 + 30*(0) ,540 - 5*(0)))
        pygame.display.update()
            
        pygame.time.delay(250)
        cardback = pygame.image.load('graphics/cards/cardback.png').convert_alpha()
        cardback = pygame.transform.scale(cardback, (112.5, 164))
        self.screen.blit(cardback, (width//2-90 + 30*0 ,10))
        pygame.display.update()
            
        pygame.time.delay(250)
        card = pygame.image.load(functions.cardsPics(player[1])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        self.screen.blit(card , (width//2-90 + 30*(1) ,540 - 5*(1)))
        pygame.display.update()
            
        pygame.time.delay(250)
        card = pygame.image.load(functions.cardsPics(dealer[1])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        self.screen.blit(card , (width//2-90 + 30, 15))
        pygame.display.update()
            
    def winCheck(self, dealer, player):
        #Deals with win conditions
        if self.handValue(player) > self.handValue(dealer) and self.handValue(player) <= 21:
            return "Player Wins!"
        elif self.handValue(player) < self.handValue(dealer) and self.handValue(dealer) <= 21:
            return "Dealer Wins!"
        elif self.handValue(player) == self.handValue(dealer):
            return "Push!"
            
    def drawChips(self, chipSet, bank):
        i = 0
        chipButtons = []
        for val, chipImages in chipSet.items():
            if val <= bank:
                chipButtons.append(chipButton(val, chipImages[0],chipImages[1], 85, 85, 5 + 90*i, 610))
                i += 1
        return chipButtons
    
    def displayMoney(self, bet, bank):
        font = pygame.font.Font('freesansbold.ttf', 32)
        betText = font.render(f"BET: {bet}", True, 'black')
        betTextRect = betText.get_rect()
        betTextRect.center = (self.screen.get_width() // 4.5, self.screen.get_height() // 1.25)
        self.screen.blit(betText, betTextRect)
        
        bankText = font.render(f"BANK: {bank}", True, 'black')
        bankTextRect = bankText.get_rect()
        bankTextRect.center = (self.screen.get_width() // 5, self.screen.get_height() // 8)
        self.screen.blit(bankText, bankTextRect)