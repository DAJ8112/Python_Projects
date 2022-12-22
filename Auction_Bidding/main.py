from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
auct={}
auction_state=True
while auction_state:
    print(logo)
    name=input("Enter your name here: ")
    bid=input("Enter your bid: $")
    auct[name]=bid
    cont=input("Are there any more bidders(Yes or No)?: ").lower()
    if cont=='yes':
        clear()
    else:
        list_val=list(auct.values())
        list_keyz=list(auct.keys())
        highest_bid=max(list_val)
        a=list_val.index(highest_bid)
        auction_state=False
clear()
print(logo)
print(f"The highest bid is given by {list_keyz[a]} of a whopping price of ${list_val[a]}")
        
        