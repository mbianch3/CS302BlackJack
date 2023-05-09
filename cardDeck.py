#Card and CardDeck class and member functions file
import pygame
from pygame.locals import *
import functions
from button import chipButton
import random

#Card Class
class Card:
    #Member variables
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    #Represents cards as string for easier access in functions
    def __repr__(self):
        faceCards = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        return f"{faceCards.get(self.value, str(self.value))}{self.suit}"

#CardDeck class for dealing, shuffling, and printing various items related to the cards and betting
class CardDeck:
    #Initializes with 4 decks n = 13 equates to 1 deck worth of cards n = 4*13=52 = 4 decks of cards
    def __init__(self, screen, n=52):
        self.size = n * 4
        self.deck = [Card((i % 13) + 1, suit) for i in range(n) for suit in ['H', 'D', 'C', 'S']]
        self.screen = screen
    #Shuffles Deck
    def shuffle(self):
        random.shuffle(self.deck)
        
    #Deals cards
    def deal(self, hand):
        new_hand = hand + [self.deck[0]]
        self.deck.pop(0)
        self.size += -1
        return new_hand
    
    #Calculates value of hand
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
    
    #Draws dealers handValue
    def drawDealerValue(self, value):
        functions.displayText((f"Hand Value: {value}"), self.screen.get_width()//2, self.screen.get_height()//3, 32)
        
    #Draws players handValue
    def drawPlayerValue(self, value):
        functions.displayText((f"Hand Value: {value}"), self.screen.get_width()//2, self.screen.get_height()//1.5, 32)
        
    #Used for play again screen to keep only the cards on screen
    def drawScreen(self, player, dealer):
        width = self.screen.get_width()
        #draws playerHand
        self.drawPlayerHand(player)
        #draws dealerHand
        for i in range(len(dealer)):
            card = pygame.image.load(functions.cardsPics(dealer[i])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            self.screen.blit(card , (width//2-90 + 30*i ,10+5*i))
        #displays hand values for the dealer hand
        self.drawDealerValue(self.handValue(dealer))
    
    #Used for updating images
    def drawPlayerHand(self, player):
        width = self.screen.get_width()
        for i in range(len(player)):
            card = pygame.image.load(functions.cardsPics(player[i])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            self.screen.blit(card , (width//2-90 + 30*(i) ,540 - 5*(i)))
        self.drawPlayerValue(self.handValue(player))
    
    #Used for updating the images
    def drawDealerHand(self, dealer):
        width = self.screen.get_width()
        cardback = pygame.image.load('graphics/cards/cardback.png').convert_alpha()
        cardback = pygame.transform.scale(cardback, (112.5, 164))
        self.screen.blit(cardback, (width//2-90 + 30*0 ,10))
        card = pygame.image.load(functions.cardsPics(dealer[1])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        self.screen.blit(card , (width//2-90 + 30, 15))
    
    #Displays dealer hand whenever the dealer hits flipping the hidden card and displaying new cards
    def displayDealerHand(self, hand):
        
        width = self.screen.get_width()
        #Used to print hidden card in dealers hand
        if(len(hand) == 2):
            card = pygame.image.load(functions.cardsPics(hand[0])).convert_alpha()
            card = pygame.transform.scale(card, (112.5, 164))
            self.screen.blit(card , (width//2-90 + 30*(0) ,10 + 5*(0)))
        #prints the last card in dealers hand usually used for hitting       
        card = pygame.image.load(functions.cardsPics(hand[(len(hand) - 1)])).convert_alpha()
        card = pygame.transform.scale(card, (112.5, 164))
        self.screen.blit(card , (width//2-90 + 30*(len(hand) - 1) ,10 + 5*(len(hand) - 1)))
        pygame.display.update()
                
    #Displays cards for player and dealer when deal is pressed so the first dealer card is hidden            
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
        
    #Checks who won based of hand values
    def winCheck(self, dealer, player):
        if self.handValue(player) > self.handValue(dealer) and self.handValue(player) <= 21:
            return "Player Wins!"
        elif self.handValue(player) < self.handValue(dealer) and self.handValue(dealer) <= 21:
            return "Dealer Wins!"
        elif self.handValue(player) == self.handValue(dealer):
            return "Push!"
        
    #used for storing the avaible chipButtons into a list then returns the list        
    def drawChips(self, chipSet, bank):
        i = 0
        chipButtons = []
        
        #Chipset is a map that is keyed on the value of the chip and holds a list of the chipImages as a value
        for val, chipImages in chipSet.items():
            
            #Only stores a chip into the list if that value chip can be bet
            if val <= bank:
                chipButtons.append(chipButton(chipImages[0],chipImages[1], 85, 85, 5 + 90*i, 610))
                i += 1
        return chipButtons
    
    #Displays the bet and bank of the player to the screen
    def displayMoney(self, bet, bank):
        functions.displayText((f"BET: {bet}"), self.screen.get_width() // 4.5, self.screen.get_height() // 1.25, 32)
        functions.displayText((f"BANK: {bank}"), self.screen.get_width() // 5, self.screen.get_height() // 8, 32)