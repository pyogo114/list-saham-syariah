# Guessing number game

from random import randint
from art_numberguess import logo

print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulties():
    """Set difficulties for hard or easy level"""

    eh = input("Choose a difficulty. Type 'easy' or 'hard' :")
    
    if eh == "hard":
        return HARD_LEVEL
    else:
        return EASY_LEVEL


def check_answer(guess,comp,lives):
    """Checks answer against guess and return the remaining lives"""
    
    if guess > comp:
        print("Too high.")
        return lives - 1

    elif guess < comp:
        print("Too low")
        return lives - 1

    else:
        print(f"Your guess is right. It is {comp}. You Win!!!")
        exit()


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#EH = input("Choose a difficulty. Type 'easy' or 'hard' :")

LIVES = set_difficulties()

comp = randint(0,100)

print(f"You have {LIVES} attempts remaining to guess the game number.")

PLAY = True

while PLAY:

    guess = int(input("Make a guess? "))
    
    LIVES = check_answer(guess, comp,LIVES)    
    
    if LIVES < 1:
        PLAY = False
    
    else:
        print("Guess again")
        print(f"You have {LIVES} attempts remaining to guess the number")


print(f"The answer is {comp}")
print("Bye")  
