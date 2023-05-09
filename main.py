# Matthew Bianchi and John Kutbay
# COSC 302 Final Project pyGame Blackjack

import pygame
from pygame.locals import *
import functions
from button import Button
import random
import cardDeck

#Inititilizes pygame and screen height and width
pygame.init()
X=1080
Y=720

# pygame window:
functions.startWindow()

# Intial text:
functions.displayText('Blackjack', int(X/2), int(Y/5), int(X/10))

# Initial Start Button:
# def __init__(self,font,color,imageL,image,width,height,text)
startButton = Button(250, 100, 'graphics/buttons/startButton.png', 'graphics/buttons/startButtonL.png')

#chipSet Map/Dict for printing chip buttons
#Map is keyed on chip value and holds a list of chip images for each value
chipSet = {10 : ['graphics/chips/green10Chip.png', 'graphics/chips/green10ChipL.png'], 
           20 : ['graphics/chips/blue20Chip.png','graphics/chips/blue20ChipL.png'], 
           50 : ['graphics/chips/red50Chip.png', 'graphics/chips/red50ChipL.png'], 
           100 : ['graphics/chips/black100Chip.png','graphics/chips/black100ChipL.png'], 
           500 : ['graphics/chips/grey500Chip.png', 'graphics/chips/grey500ChipL.png']}

#Starting bank value
bank = 1000

#Starting screen
run = True
while run == True:
    mouse = pygame.mouse.get_pos()
    functions.startmouse(mouse, startButton.width, startButton.height, startButton.image, startButton.imageL)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (X/2)-(startButton.width/2) <= mouse[0] <= (X/2)+(startButton.width/2) and (Y/2)-(startButton.height) <= mouse[1] <= (Y/2):
                run = False
                break
    pygame.display.flip()
    
#intializes all starting states, hands, and card deck
tmp = functions.gameWindow()
screen = tmp[0]
background = tmp[1]

deck = cardDeck.CardDeck(screen)
deck.shuffle()

start = True
playerTurn = True
betting = True
gameOver = False
winner = None

#List hands for player and dealer
player = []
dealer = []
bet = 0
temp = 0

#Initializes all buttons
# def __init__(self,font,color,imageL,image,width,height,text)
dealButton = Button(150, 75, 'graphics/buttons/dealButton.png', 'graphics/buttons/dealButtonL.png')
hitButton = Button(150, 75, 'graphics/buttons/hitButton.png', 'graphics/buttons/hitButtonL.png')
standButton = Button(150, 75, 'graphics/buttons/standButton.png', 'graphics/buttons/standButtonL.png')
GameOverButton = Button(150, 75, 'graphics/buttons/gameOverButton.png', 'graphics/buttons/gameOverButtonL.png')
playAgainButton = Button(150, 75, 'graphics/buttons/playAgainButton.png', 'graphics/buttons/playAgainButtonL.png')
clearBetButton = Button(125, 50, 'graphics/buttons/clearBetButton.png', 'graphics/buttons/clearBetButtonL.png')


pygame.display.flip()

#Main game loop
while True:   
    #Gets mouse position for buttons
    mouse = pygame.mouse.get_pos()
    
    #Loop runs when gameOver var is true
    if gameOver == True:
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
        start = False
        #displays Game Over Text
        functions.displayText("Out of Money!", screen.get_width()//2, screen.get_height()//3, 32)
        functions.gameOvermouse(mouse, GameOverButton.width, GameOverButton.height, GameOverButton.image, GameOverButton.imageL)
    #Loop runs when player is betting  
    elif start == True:
        winner = None
        betting = True
        
        #Whenever a bet is made it updates the chips that get displayed as well as the bank and bet on screen text
        if(bet == 0 or temp != bet):
            screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
            chipButtons = deck.drawChips(chipSet, bank)
            temp = bet
            deck.displayMoney(bet, bank)
            
        #Only runs chipFunctions if bet = 0 or if the mouse is in a rect around the chips to help improve performance during the betting screen
        if(bet == 0 or (0 <= mouse[0] <= 1080 and 400 <= mouse[1] <= 720)):       
            for i in range(len(chipButtons)):
                functions.chipMouse(mouse, chipButtons[i].image, chipButtons[i].imageL, chipButtons[i].width, chipButtons[i].height, chipButtons[i].xpos, chipButtons[i].ypos)
                
        #displays clear and deal buttons if a bet has been made   
        if(bet > 0):
            functions.clearBetmouse(mouse, clearBetButton.width, clearBetButton.height, clearBetButton.image, clearBetButton.imageL)
            functions.dealmouse(mouse, dealButton.width, dealButton.height, dealButton.image, dealButton.imageL)
            playerTurn = True
    #displays hit and stand buttons after betting
    elif winner == None and playerTurn == True and start == False:
        functions.hitmouse(mouse, hitButton.width, hitButton.height, hitButton.image, hitButton.imageL)
        functions.standmouse(mouse, standButton.width, standButton.height, standButton.image, standButton.imageL)
    #displays play again after round is completed
    elif winner != None and start == False and playerTurn == False:
        functions.playAgainmouse(mouse, playAgainButton.width, playAgainButton.height, playAgainButton.image, playAgainButton.imageL)
        
    #If deck size falls below 15 cards it shuffles it a random number of times
    if deck.size < 15:
        del deck
        deck = cardDeck.CardDeck(screen)
        for i in range(random.randint(1, 10)):
            deck.shuffle()

    for event in pygame.event.get():
        #Deals with knowing the game is over and closes the window
        if gameOver == True and event.type == pygame.MOUSEBUTTONDOWN:
            if (X/2)-(GameOverButton.width/2) <= mouse[0] <= (X/2)+(GameOverButton.width/2) and (Y/2)-(GameOverButton.height) <= mouse[1] <= (Y/2):
                pygame.quit()
                exit()
        #Deals with knowing if the playAgain button was pressed to reset game states
        if start == False and playerTurn == False and winner != None and event.type == pygame.MOUSEBUTTONDOWN and gameOver == False:
            if (X/2)-(playAgainButton.width/2) <= mouse[0] <= (X/2)+(playAgainButton.width/2) and (Y/2)-(playAgainButton.height) <= mouse[1] <= (Y/2):
                start = True
                winner = None
                #If bank is less than a bettable amount game is over
                if(bank < 10):
                    gameOver = True
        #Deals with knowing if the any of the chip buttons were pressed
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
        #Used to deal with clear button and deal button
        if playerTurn == True and winner == None and event.type == pygame.MOUSEBUTTONDOWN and start == True and gameOver == False:
            #Clears bet
            if (X/14)-clearBetButton.width/2 <= mouse[0] <= (X/14)+(clearBetButton.width/2) and (Y/1.2)-(clearBetButton.height) <= mouse[1] <= (Y/1.2):
                bank = bank + bet
                bet = 0
            #Deals cards and prints cards to screen
            if (X/2)-(dealButton.width/2) <= mouse[0] <= (X/2)+(dealButton.width/2) and (Y/2)-(dealButton.height) <= mouse[1] <= Y/2:
                screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
                betting = False
                start = False
                
                #Uses a list to create the player and dealer's hand arrays
                player = []
                dealer = []
                
                #Displays bank and bet
                deck.displayMoney(bet, bank)
                
                #Deals starting Hands
                player = deck.deal(player)
                dealer = deck.deal(dealer)
                player = deck.deal(player)
                dealer = deck.deal(dealer)

                #If you want to test with specific cards
                #player/dealer[index] = cardDeck.Card(Value,"Suit") where Value = 1-13 and Suit = D,H,S,C
                
                #Prints starting hands with dealer first card hidden
                deck.initialDeal(player, dealer)
                
                #Displays player value
                deck.drawPlayerValue(deck.handValue(player))
                
                #If player starting hand is 21 it ends the players turn and checks if the dealer has 21
                if deck.handValue(player) == 21:
                    #If the dealer also has 21 its a push
                    if deck.handValue(dealer) == 21:
                        winner = "Push!"
                    #If not the player hits black jack and wins 1.5x their bet
                    else:
                        winner = "Player Blackjack!"
                        bank += int(2.5*bet)
                    playerTurn = False
                    pygame.time.delay(500)
                    deck.displayDealerHand(dealer)
                pygame.display.flip()
                
        #If the exit button is pressed in the top right screen closes
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #Player Hit and Standing
        if playerTurn == True and event.type == pygame.MOUSEBUTTONDOWN and winner == None and gameOver == False and betting == False:
            #Hitting
            if ((X/2)-(3*hitButton.width/2) - 100) <= mouse[0] <= ((X/2)-(3*hitButton.width/2) - 100 + hitButton.width) and (Y/2)-(hitButton.height) <= mouse[1] <= (Y/2):
                #Deals card and updates the player hand
                player = deck.deal(player)
                screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
                deck.drawPlayerHand(player)
                deck.drawDealerHand(dealer)
                deck.displayMoney(bet, bank)
                pygame.display.update()
                #If player goes over 21 they bust and lose
                if deck.handValue(player) > 21:
                    playerTurn = False
                    winner = "Dealer Wins!"
                    
            #Standing       
            if playerTurn == True and (X/2)+(standButton.width/2) + 100 <= mouse[0] <= (X/2)+(standButton.width/2)+standButton.width + 100 and (Y/2)-(standButton.height) <= mouse[1] <= (Y/2):
                playerTurn = False

    #Dealer's turn
    if deck.handValue(player) <= 21 and playerTurn == False and winner == None and betting == False and start == False and gameOver == False and deck.handValue(dealer) <= 21:
        #Delays revealing the first card so it isn't instantaneous
        if(len(dealer) <= 2):
            pygame.time.delay(300)
            deck.displayDealerHand(dealer)
        #Dealer hits until value is at least a soft 17
        if deck.handValue(dealer) < 17:
            dealer = deck.deal(dealer)
            pygame.time.delay(650)
            deck.displayDealerHand(dealer)
        #If dealer busts player wins
        if deck.handValue(dealer) > 21:
            winner = "Player Wins!"
                
    #Deals with win cases if no one busts
    if playerTurn == False and deck.handValue(dealer) >= 17 and winner == None and gameOver == False:
        winner = deck.winCheck(dealer, player)
    
    #Prints winner to screen and gives bets to player if they win/push
    if winner != None and start == False and bet != 0 and gameOver == False:
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
        if winner == "Player Wins!":
            bank += 2*bet
        if winner == "Push!":
            bank += bet
        pygame.time.delay(300)
        #Draws dealer and player final hands
        deck.drawScreen(player, dealer)
        #prints winner to screen
        functions.displayText(winner, screen.get_width()//2, screen.get_height() // 1.75, 32)
        bet = 0
        deck.displayMoney(bet, bank)
        #Clears hands
        player = []
        dealer = []

    pygame.display.update()
    
    



