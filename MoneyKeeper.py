money = 0  # Define money as a global variable

def balance():
    global money
    return money

def deposit():
    global money
    deposit_amount = input("how much money do you want to deposit? ")
    if int(deposit_amount) >= 10000:
        print("did you just stole a bank? 🤨")
        print("\n")
        return
    money += int(deposit_amount)
    print(f"you deposited {deposit_amount} dollah")
    print("\n")
    return money

def withdraw():
    global money
    withdraw_amount = input("how much money are you taking? ")
    if int(withdraw_amount) > money:
        print("you're broke.....")
        print("\n")
        return
    money -= int(withdraw_amount)
    print(f"you withdrew {withdraw_amount} dollah")
    print("\n")
    return money

def balance():
    global money
    print(f"you have {money} dollah")
    print("\n")
    return money

def start():
    global money
    user_choice = ""
    print("\n")
    print("\n")
    while user_choice not in ["q" or "quit"]:
        print("----- Welcome to the 🤑 Money Keeper! 🤑 how may i help you? ----")
        user_choice = input("         (balance, deposit, withdraw, quit)...? ")
        print("\n")
        if user_choice == "balance" or user_choice == "b":
            balance()
        elif user_choice == "withdraw" or user_choice == "w":
            withdraw()
        elif user_choice == "deposit" or user_choice == "d":
             deposit()
        elif user_choice == "quit" or user_choice == "q":
            print("sayonara!! thank you for using the 🤑 Money Keeper! 🤑 ")
            print("\n")
            break
        else:
            print("typo huh?")
            print("\n")
            start()

start()
