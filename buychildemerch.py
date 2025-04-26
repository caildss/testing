# a mission to buy childe merch!!!

import time
money = 50

def money():
    global money
    print(f"you have {money} dollah")
    return money

def backstory():
    print("------🐋welcome to the childe haven!!🦊-------")
    user_choice = input("Want to buy childe exclusive plushie for 100 dollah??(y/n)")
    if user_choice == "y" or "yes":
        print(f"you only have {money} dollah... \n")
        time.sleep(2)
        print("need a job? become a seller!!")
        sell_choice = input("do you want to be a cupcake? pancake? or waffle seller?")
        while sell_choice not in ["cupcake", "pancake", "waffle"]:
            print("you only have 3 options...")
            sell_choice = input("do you want to be a cupcake? pancake? or waffle seller?")
        sell = sell_choice
        print(f"you are now a {sell} seller!")
    else:
        print("your money is safe then.. byebye!")
    return sell

def buy_ingredients():
    pass
    
def see_ingredients():
    pass
    
def see_inventory():
    pass
    
    
def money():
    global money
    print(f"you have {money} dollah!")
    return money

def start_selling():
    pass

def menu():
    print("----------- let's get started! ------------")
    print("1. buy ingredients")
    print("2. see ingredients")
    print("3. see inventory")
    print("4. money...")
    print("5. start selling")
    activities = input("please chose an activity: ")
    if activities == "1":
        buy_ingredients()
    elif activities == "2":
        see_ingredients()
    elif activities == "3":
        see_inventory()
    elif activities == "4":
        money()
    elif activities == "5":
        start_selling()
    else:
        print("you thought this is a deposit?")
        menu()
    return activities

backstory()