# Matthew Bianchi and John Kutbay
# COSC 302 Final Project pyGame Blackjack

import pygame
from pygame.locals import *
import functions
from button import Button
import random
import cardDeck

pygame.init()
clock=pygame.time.Clock()
clock.tick(60)
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
chipSet = {10 : ['graphics/chips/green10Chip.png', 'graphics/chips/green10ChipL.png'], 
           20 : ['graphics/chips/blue20Chip.png','graphics/chips/blue20ChipL.png'], 
           50 : ['graphics/chips/red50Chip.png', 'graphics/chips/red50ChipL.png'], 
           100 : ['graphics/chips/black100Chip.png','graphics/chips/black100ChipL.png'], 
           500 : ['graphics/chips/grey500Chip.png', 'graphics/chips/grey500ChipL.png']}

#Starting bank value
bank = 1000


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

tmp = functions.gameWindow()
screen = tmp[0]
background = tmp[1]

deck = cardDeck.CardDeck(screen)
deck.shuffle()

playerTurn = True
winner = None
start = True
gameOver = False
betting = True
player = []
dealer = []


bet = 0

# def __init__(self,font,color,imageL,image,width,height,text)
dealButton = Button(150, 75, 'graphics/buttons/dealButton.png', 'graphics/buttons/dealButtonL.png')
hitButton = Button(150, 75, 'graphics/buttons/hitButton.png', 'graphics/buttons/hitButtonL.png')
standButton = Button(150, 75, 'graphics/buttons/standButton.png', 'graphics/buttons/standButtonL.png')
GameOverButton = Button(150, 75, 'graphics/buttons/gameOverButton.png', 'graphics/buttons/gameOverButtonL.png')
playAgainButton = Button(150, 75, 'graphics/buttons/playAgainButton.png', 'graphics/buttons/playAgainButtonL.png')
clearBetButton = Button(125, 50, 'graphics/buttons/clearBetButton.png', 'graphics/buttons/clearBetButtonL.png')

pygame.display.flip()
while True:   
    mouse = pygame.mouse.get_pos()
    if gameOver == True:
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
        start = False
        gameOverText = font.render("Out of Money!", True, 'black')
        gameOverRect = gameOverText.get_rect()
        gameOverRect.center = (screen.get_width() // 2, screen.get_height() // 3)
        screen.blit(gameOverText, gameOverRect)
        functions.gameOvermouse(mouse, GameOverButton.width, GameOverButton.height, GameOverButton.image, GameOverButton.imageL)  
    elif start == True:
        winner = None
        betting = True
        screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
        chipButtons = deck.drawChips(chipSet, bank)
        #This for loop lags the screen maybe try and find someway to make it faster
        for i in range(len(chipButtons)):
            functions.chipMouse(mouse, chipButtons[i].value, chipButtons[i].image, chipButtons[i].imageL, chipButtons[i].width, chipButtons[i].height, chipButtons[i].xpos, chipButtons[i].ypos)
            
        deck.displayMoney(bet, bank)
        if(bet > 0):
            functions.clearBetmouse(mouse, clearBetButton.width, clearBetButton.height, clearBetButton.image, clearBetButton.imageL)
            functions.dealmouse(mouse, dealButton.width, dealButton.height, dealButton.image, dealButton.imageL)
            playerTurn = True
    elif winner == None and playerTurn == True and start == False:
        functions.hitmouse(mouse, hitButton.width, hitButton.height, hitButton.image, hitButton.imageL)
        functions.standmouse(mouse, standButton.width, standButton.height, standButton.image, standButton.imageL)
    elif winner != None and start == False and playerTurn == False:
        functions.playAgainmouse(mouse, playAgainButton.width, playAgainButton.height, playAgainButton.image, playAgainButton.imageL)

    if deck.size < 15:
        del deck
        deck = cardDeck.CardDeck(screen)
        for i in range(random.randint(1, 10)):
            deck.shuffle()

    for event in pygame.event.get():
        if gameOver == True and event.type == pygame.MOUSEBUTTONDOWN:
            if (X/2)-(GameOverButton.width/2) <= mouse[0] <= (X/2)+(GameOverButton.width/2) and (Y/2)-(GameOverButton.height) <= mouse[1] <= (Y/2):
                pygame.quit()
                exit()
        if start == False and playerTurn == False and winner != None and event.type == pygame.MOUSEBUTTONDOWN and gameOver == False:
            if (X/2)-(playAgainButton.width/2) <= mouse[0] <= (X/2)+(playAgainButton.width/2) and (Y/2)-(playAgainButton.height) <= mouse[1] <= (Y/2):
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
            if (X/14)-clearBetButton.width/2 <= mouse[0] <= (X/14)+(clearBetButton.width/2) and (Y/1.2)-(clearBetButton.height) <= mouse[1] <= (Y/1.2):
                bank = bank + bet
                bet = 0
            if (X/2)-(dealButton.width/2) <= mouse[0] <= (X/2)+(dealButton.width/2) and (Y/2)-(dealButton.height) <= mouse[1] <= Y/2:
                screen.blit(pygame.transform.scale(background, screen.get_size()), (0,0))
                betting = False
                start = False
                #Uses a list to create the player and dealer's hand arrays
                player = []
                dealer = []
                deck.displayMoney(bet, bank)
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
                deck.displayMoney(bet, bank)
                pygame.display.update()

                if deck.handValue(player) > 21:
                    playerTurn = False
                    winner = "Dealer Wins!"
                    
            if playerTurn == True and (X/2)+(standButton.width/2) + 100 <= mouse[0] <= (X/2)+(standButton.width/2)+standButton.width + 100 and (Y/2)-(standButton.height) <= mouse[1] <= (Y/2):
                playerTurn = False

        #Dealer's turn
        if deck.handValue(player) <= 21 and playerTurn == False and winner == None and betting == False and start == False and gameOver == False and deck.handValue(dealer) <= 21:
            #Delays revealing the first card so it isn't instantaneous
            if(len(dealer) <= 2):
                pygame.time.delay(300)
                deck.displayDealerHand(dealer)
                
            if deck.handValue(dealer) < 17:
                dealer = deck.deal(dealer)
                pygame.time.delay(500)
                deck.displayDealerHand(dealer)
            if deck.handValue(dealer) > 21:
                winner = "Player Wins!"
                
        #Deals with win cases
        if playerTurn == False and deck.handValue(dealer) >= 17 and winner == None and gameOver == False:
            winner = deck.winCheck(dealer, player)
            
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
            deck.displayMoney(bet, bank)
            player = []
            dealer = []

    pygame.display.update()
    
    



