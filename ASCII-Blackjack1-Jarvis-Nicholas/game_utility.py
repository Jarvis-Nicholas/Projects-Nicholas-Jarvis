"""
Author: Nicholas Jarvis
Date: 1/30/2023
Purpose: Python Blackjack
"""

def displayTable(dealer, player):

    # Cool Terminal Art in my humble opinion :)
    print("**************************************************")
    print("                  ---------------\n                 | DEALER'S HAND |\n                  ---------------")  
    print("                      Sum:", dealer.sum)

    # No use displaying numbers larger than 21
    if dealer.aceCount > 0 and dealer.alternateAceSum <= 21:
        print("                   Alternate:", dealer.alternateAceSum)

    dealer.displayHand()
    print("__________________________________________________")

    player.displayHand()
    print("                      Sum:", player.sum)

    # No use displaying numbers larger than 21
    if player.aceCount > 0 and player.alternateAceSum <= 21:
        print("                   Alternate:", player.alternateAceSum)

    print("                  ---------------\n                 | PLAYER'S HAND |\n                  ---------------")


def dealerMultiHit(cardDeck, dealer):

    # Do while loop
    while True:
        dealer.hit(cardDeck[0])
        cardDeck.pop(0)

        if dealer.isBusted() == True:
            break
        # Dealer stops from 17 to 21, also accounting for aces
        elif (dealer.sum >= 17 and dealer.sum <= 21) or (dealer.alternateAceSum >= 17 and dealer.alternateAceSum <= 21):
            dealer.stand()
            break

def gameOver(dealer, player):

    # Player Busts from hitting
    if player.isBusted() == True:
        dealer.wins = dealer.wins + 1
        print("Dealer wins!!\n")
        return True

    # Play stood and dealer busted from hitting
    elif dealer.isBusted() == True:
        player.wins = player.wins + 1
        print("Player wins!!\n")
        return True

    
    # Both are standing (this also covers a player's natural 21)
    elif dealer.isStanding == True:

        if dealer.sum > player.sum:
            dealer.wins = dealer.wins + 1
            print("Dealer wins!!\n")
            
        elif player.sum > dealer.sum:
            player.wins = player.wins + 1
            print("Player wins!!\n")
            
        elif player.sum == dealer.sum:
            print("It's a tie!!\n")
            
        return True
    return False

def playFirstHand(dealer, player, cardDeck):

    # Initial setup
    dealer.hit(cardDeck[0])
    cardDeck.pop(0)
    player.hit(cardDeck[0])
    cardDeck.pop(0)
    player.hit(cardDeck[0])
    cardDeck.pop(0)

    # Display
    displayTable(dealer, player)

    # Natural Blackjack
    if player.sum == 21:

        player.stand()

        # Dealer hits (checking for dealer natural)
        dealer.hit(cardDeck[0])
        cardDeck.pop(0)
        dealer.stand()

        # Display
        displayTable(dealer, player)