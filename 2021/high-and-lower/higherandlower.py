# Higher and lower game

from pickle import FALSE
from art import logo,vs
from data import data
from random import randint

# Print logo dan pembuka
print(logo)

DATA_A = {}
DATA_B = {}
SCORE = 0
FAILED = 0
PLAY = True

while PLAY:

    DATA_A = data[randint(0,len(data)-1)]
    DATA_B = data[randint(0,len(data)-1)]

    if DATA_A == DATA_B:
        DATA_B = data[randint(0,len(data)-1)]

    print(f"{DATA_A['name']}, {DATA_A['description']}, from {DATA_A['country']}")

    print(vs)

    print(f"{DATA_B['name']}, {DATA_B['description']}, from {DATA_B['country']}")

    print(DATA_A["follower_count"])
    print(DATA_B["follower_count"])

    AB = input("Who has more followers? Type 'A' or 'B': ")
        
    if AB.upper() == 'A' and DATA_A["follower_count"] > DATA_B["follower_count"]:
        SCORE += 1
        print(f"You're right! Current score : {SCORE}") 

    elif AB.upper() == 'B' and DATA_A["follower_count"] < DATA_B["follower_count"]:
        SCORE += 1
        print(f"You're right! Current score : {SCORE}") 

    else:
        print(f"Sorry, that's wrong. Final score : {SCORE}")
        FAILED += 1
    
    if FAILED == 3:
        exit()

print(f"Current score : {SCORE}, Bye bye...")
    
    

# Compare A : data A

# Print VS

# Compare B, data

#print how has more followers? Type 'A' or 'B':

#print hasilnya : Sorry, that's wrong. Final score : 0

# Print You're right! Current score : 