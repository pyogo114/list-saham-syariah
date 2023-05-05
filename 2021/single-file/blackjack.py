from art_blackjack import logo
import random

print(logo)
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt



#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Hint 6: Create a function called calculate_score() that takes a List of cards as input 
# and returns the score. 
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) 
# and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, 
# remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's 
# score is over 21, then the game ends.


def calculate_score(cardlist):
    
    total = sum(cardlist)
        
    if total > 21:
        
        i = 0

        for i in cardlist:
            if i == 11: # Kalau list maka i adalah valuenya, bukan key
                cardlist.remove(11)
                cardlist.append(1)
                return sum(cardlist)
    
    if total == 21:
        return 0

    return total

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. If the computer has 
# a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. 
# If the user_score is over 21, then the user loses. If the computer_score is over 21, then 
# the computer loses. If none of the above, then the player with the highest score wins.


def compare(userlist,complist):

    userscore = calculate_score(userlist)
    compscore = calculate_score(complist)

    if userscore == 0:
        print("You have blackjack. Good game!")
        play = False

    elif userscore > 21:         
        print("You are bust. You lose!")
        play = False

    elif compscore == 0:
        print(complist)
        print("Computer have blackjack. You lose!")
        play = False

    elif compscore > 21:         
        print("Computer is bust. You win!")
        play = False
    
    elif userscore > compscore:
        print("You have won. Great.")
        play = False 
    
    elif userscore < compscore:
        print(complist)
        print("Computer have won. You lose!")
        play = False 

    elif userscore == compscore:
        print("Tie!")
          

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []


play = True

user_card = []
computer_card = []

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

while play:
    print(f"Your cards are ", end="")
    
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in 
    # Hint 9 need to be repeated until the game ends.
    
    print(user_card, end="")

    print (f" Jumlah {sum(user_card)}")

    print(f"Computer card is ",end="")
    print(computer_card[0])

    # Hint 10: If the game has not ended, ask the user if they want to draw another card. 
    # If yes, then use the deal_card() function to add another card to the user_cards List. 
    # If no, then the game has ended.

    if sum(user_card) == 21 or sum(computer_card) == 21:
        compare(user_card,computer_card)
        exit()
    
    if sum(user_card) > 21 or sum(computer_card) > 21:
        compare(user_card,computer_card)
        exit()
        
    yn = input("Will you take another card? ('y' or 'n')")

    if yn == "y":
        user_card.append(deal_card())

        #Hint 12: Once the user is done, it's time to let the computer play. 
        # The computer should keep drawing cards as long as it has a score less than 17.

        if sum(computer_card) < 17:
            computer_card.append(deal_card())

    else:
        if sum(computer_card) < 17:
            computer_card.append(deal_card())

        print(f"Computer card are {computer_card} ",end="")
        print(f"Total is {sum(computer_card)}")
        compare(user_card,computer_card)
        print("Bye...")
        play = False

# Hint 14: Ask the user if they want to restart the game. If they answer yes, 
# clear the console and start a new game of blackjack and show the logo from art.py.










