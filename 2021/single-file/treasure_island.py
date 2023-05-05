print("Welcome to treasure island. Your mission is to find treassure.")
intersection = input("You have found the intersection, left or right ? ")

if intersection == "right":
    print("You have cough by the tiger. You dead!")
    
elif intersection == "left":
    sow = input("You found a great river in front of you? Should you swim or wait? ")

    if sow == "swim":
        print("Sudenlly came a big wave that swallow you. You dead!")
        
    elif sow == "wait":
        door = input("As you wait, you find a small boat that can take you accross the river. \
        After you reach the acros riverside, you find 3 door, red door, white door and blue. \
        Which door do you choose? ")

        if door == "red":
            print("You find a beast. You dead!")
            
        elif door == "white":
            print("You get into the hole. You dead")
            
        elif door == "blue":
            print("You find the treasure. You Win!")
            
        else:
            print("You choose what is not exist. You dead!")
            
    else:
        print("You choose what is not exist. You dead!")
else:
    print("You dead already!")      
