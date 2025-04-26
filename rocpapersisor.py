# Thi is a rock paper scicor game! 

import random

def get_comp_choice ():
    return random.choice(["roc","peper","scicor"])

def get_user_choice ():
    while True:
        user_choice = input("roc, peper, or scicor? choose wisely....").lower()
        if user_choice in ["roc","peper", "scicor"]: 
            return user_choice
        else:
            print("naw bro wym???")
     
def start():
    user_choice = (get_user_choice())
    computer_choice = (get_comp_choice())
    computer_choice = get_comp_choice()
    print(f"🤖computer chose {computer_choice}")
    print(f"👯you chose {user_choice}")
    return user_choice, computer_choice

def winner():
    if user_choice == computer_choice:
        print("tie!!😐")
    elif (user_choice == "scicor" and computer_choice == "peper") or \
        (user_choice == "roc" and computer_choice == "scicor") or \
        (user_choice == "peper" and computer_choice == "roc"):
            print("WINNER!!!!🤯🤯🤯🤯🤯🤯")
    else:
        print("you lose.........😭😭")

user_choice, computer_choice = start()
winner()