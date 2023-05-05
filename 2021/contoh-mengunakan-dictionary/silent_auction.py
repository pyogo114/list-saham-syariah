# Silent auctions

print("Welcome to the secret auction program.")

bid_dict = {}
other = True

while other:

    name = input("What is your name? ")
    bid = input("What is your bid? ")
    
    bid_dict[name] = bid

    is_other = input("Are there any other bidders? Type 'yes' or 'no'.")
    
    if is_other == "no":
        other = False


biddername = ""
maxbid = 0

for key in bid_dict:
    if int(bid_dict[key]) > maxbid:
        biddername = key
        maxbid = int(bid_dict[key])
        
print(f"The winner is {biddername} with a bid of ${maxbid}")    