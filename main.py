#Matthew Bianchi
import pygame
import random


from pygame.locals import *
from sys import exit
#Deals with assigning card pictures
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
    
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        faceCards = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        return f"{faceCards.get(self.value, str(self.value))}{self.suit}"

class CardDeck:
    def __init__(self, n=13):
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

    def displayPlayerHand(self, hand):
        width = screen.get_width()
        height = screen.get_height()
        for i in range(len(hand)):
            card = pygame.image.load(cardsPics(hand[i])).convert()
            card = pygame.transform.scale(card, (120, 180))
            screen.blit(card , (width//2-120 + 70*i ,height-200 - 20*i))
            
    def displayDealerHand(self, hand, reveal):
        width = screen.get_width()
        height = screen.get_height()
        if reveal == True:
            for i in range(len(hand)):
                card = pygame.image.load(cardsPics(hand[i])).convert()
                card = pygame.transform.scale(card, (120, 175))
                screen.blit(card , (width//2 + 70*i ,20*i))
        else:
            pygame.draw.rect(screen, 'white', [width//2, 0, 120, 175])
            card = pygame.image.load(cardsPics(hand[1])).convert()
            card = pygame.transform.scale(card, (120, 175))
            screen.blit(card , (width//2 + 70 ,20))
            
    def winCheck(self):
        #Deals with win conditions
        if deck.handValue(player) > deck.handValue(dealer) and deck.handValue(player) <= 21:
            print("Player Wins!\n")
            return "Player"
            #playerWin += 1
        elif deck.handValue(player) < deck.handValue(dealer) and deck.handValue(dealer) <= 21:
            print("Dealer Wins!\n")
            return "Dealer"
            #dealerWin += 1
        elif deck.handValue(player) == deck.handValue(dealer):
            print("Push!\n")
            return "Push"
            #tie += 1


pygame.init()

screen = pygame.display.set_mode((720,480), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('Blackjack')
clock = pygame.time.Clock()

background = pygame.image.load('graphics/SolidBackground.png').convert()
background = pygame.transform.scale(background, screen.get_size())
screen.blit(background,(0,0))

deck = CardDeck()
deck.shuffle()

playerTurn = True
winner = None
player = []
dealer = []

while True:
        
    if deck.size < 15:
        print("Deck reset!!!!!")
        del deck
        deck = CardDeck()
        for i in range(random.randint(1, 10)):
            deck.shuffle()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
            screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
            pygame.display.flip()
        
        #Player Hit and Standing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and winner == None:
                print("Player Hit!")
                player = deck.deal(player)
                deck.displayPlayerHand(player)

                if deck.handValue(player) > 21:
                    playerTurn = False
                    winner = "Dealer"
                    print("Player Bust!")
                    
                print("Player Hand Value: ", deck.handValue(player))
                    
            if event.key == pygame.K_s and playerTurn == True:
                print("Player Stand!")
                playerTurn = False
            
            #Starts game with inital card dealing
            if event.key == pygame.K_d:
                screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
                playerTurn = True
                #Uses a list to create the player and dealer's hand arrays
                player = []
                dealer = []
                #Used to know if dealer hand should be revealed
                reveal = False
                winner = None
                
                #Deals starting Hands
                player = deck.deal(player)
                dealer = deck.deal(dealer)
                player = deck.deal(player)
                dealer = deck.deal(dealer)
                print("Dealt Cards")
                #Displays Dealer's Cards
                deck.displayDealerHand(dealer, reveal)

                # Shows the player's hand
                deck.displayPlayerHand(player)
                

                print("Player Hand Value: ", deck.handValue(player))


        #Dealer's turn
        if deck.handValue(player) <= 21 and playerTurn == False and deck.handValue(dealer) <= 21:
            reveal = True
            #Delays revealing the first card so it isn't instantaneous
            pygame.time.delay(500)
            deck.displayDealerHand(dealer,reveal)
            pygame.display.update()
            if deck.handValue(dealer) < 17:
                dealer = deck.deal(dealer)
                pygame.time.delay(1000)
                deck.displayDealerHand(dealer,reveal)
            if deck.handValue(dealer) > 21:
                print("Dealer busts")
                playerTurn = True
            print("Dealer Hand Value: ", deck.handValue(dealer))
        
        #Deals with win cases
        if playerTurn == False and deck.handValue(dealer) >= 17:
            winner = deck.winCheck()
            playerTurn = True
            
    
    pygame.display.update()
    clock.tick(60)