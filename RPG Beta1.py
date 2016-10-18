print("Welcome to my RPG game\n")
print("INSTRUCTIONS:\nFor every prompt, type '/' to go back.")
print("To start the game, type 'start()'")

gold = 500
bag = []
CAT = ["Attack Damage","Movement Speed","Health","Consumables"]
AD = ["Long Sword","Doran's Blade","Bloodthirster"]
AD_PRICE = [350,400,900]
SPEED = ["Light Boots","Zeal"]
SPEED_PRICE = [300,540]
HEALTH = ["Ruby Crystal","Locket of Luck","Giant's Belt"]
HEALTH_PRICE = [400,850,1000]
CONS = ["Health Potion","Nora's Potion of Strength"]
CONS_PRICE = [50,300]
levelDes = ["You enter a room, and is met with a toad.",
            "There is a chest nearby, but with a lock no one will ever break.\nThe lock has 2 digits - make your guess.",
            "You are confronted by a cohort of knights.\nThey ask you for a password, representative of a riddle."]
NUMBERS = [45,78,99,12]
RIDDLES_QUES = ["What goes up but never comes down?",
                "I have holes on my top, bottom, and sides, but I still hold water. What am I?",
                "I am in your class, and in me is a lot of people."]
RIDDLES_ANSW = ["age","sponge","city"]
BOTS_ID = ["Toad","Knight","Master"]
BOTS = [30,100,50,130,100,200] #[AD,HEALTH,AD,HEALTH...]


def shop():
    print()
    print("Your gold --> " + str(gold))
    choice = input("Buy or Sell [b/s]: ")
    if choice.lower() == "b": #BUY ACTION
        print()
        print("Your inventory:")
        print(bag)            #OUTPUT INVENTORY
        print()
        mainController = True
        while mainController:
            for item in CAT:
                print("["+str(CAT.index(item)+1)+"] " + item) #PRINT CATEGORIES
            choice = input()
            if choice == "1":
                for item in AD:
                    price = AD_PRICE[AD.index(item)]
                    print("["+str(AD.index(item)+1)+"] " + item + " - " + str(price) + " gold")
                controller = True
                while controller:
                    choice = input()
                    if choice != "/":
                        bag.append(AD[int(choice)-1])
                        print("Your inventory:")
                        print(bag)
                    elif choice == "/":
                        controller = False
            elif choice == "2":
                for item in SPEED:
                    price = SPEED_PRICE[SPEED.index(item)]
                    print("["+str(SPEED.index(item)+1)+"] " + item + " - " + str(price) + " gold")
                controller = True
                while controller:
                    choice = input()
                    if choice != "/":
                        bag.append(SPEED[int(choice)-1])
                        print("Your inventory:")
                        print(bag)
                    elif choice == "/":
                        controller = False
            elif choice == "3":
                for item in HEALTH:
                    price = HEALTH_PRICE[HEALTH.index(item)]
                    print("["+str(HEALTH.index(item)+1)+"] " + item + " - " + str(price) + " gold")
                controller = True
                while controller:
                    choice = input()
                    if choice != "/":
                        bag.append(HEALTH[int(choice)-1])
                        print("Your inventory:")
                        print(bag)
                    elif choice == "/":
                        controller = False
            elif choice == "4":
                for item in CONS:
                    price = CONS_PRICE[CONS.index(item)]
                    print("["+str(CONS.index(item)+1)+"] " + item + " - " + str(price) + " gold") #THIS SEREIS OF IF STATEMENTS MAY BE ITERATED USING 2D LISTS?
                controller = True
                while controller:
                    choice = input()
                    if choice != "/":
                        bag.append(CONS[int(choice)-1])
                        print("Your inventory:")
                        print(bag)
                    elif choice == "/":
                        controller = False
            elif choice == "/":
                shop()
    elif choice.lower() == "s": #SELL ACTION
        print()
        print("Your inventory:")
        print(bag)              #OUTPUT INVENTORY
        controller = True
        while controller:
            choice = input()
            if choice != "/":
                target = bag[int(choice)-1]
                bag.remove(target)
                print("Your inventory:")
                print(bag)
            elif choice == "/":
                shop()
    elif choice == "/":
        start()
def levelSelect():
    print()
    print("Level 1\nLevel 2\nLevel 3")
    choice = int(input())
    for counter in range(3):
        if counter+1 == choice:
            print()
            print(levelDes[choice-1])

    if choice == 1:
        print(BOTS_ID[choice-1] + " - Health: " + str(BOTS[choice]) + " Damage: " + str(BOTS[choice-1]))
    elif choice == 2:
        controller = True
        number = NUMBERS[1]
        while controller:
            print(number)           #CHEAT FOR CALIBRATION
            guess = int(input("Enter your guess: "))
            if number - guess > 30 or number - guess < -30:
                print("Too far!")
            elif number - guess > 10 or number - guess < -10:
                print("Nearly there...")
            elif number - guess > 1 or number - guess < -1:
                print("Just one...")
            elif number == guess:
                print("ACCESS GRANTED!")
                controller = False
    elif choice == "/":
        start()
    else:
        print("Invalid selection")
        levelSelect()

def credit():
    print("Made by: Panhaboth Kun")
    print("Coming soon:\n1. Proper purchasing mechanism\n2. Stats update from items")
    choice = input()
    if choice == "/":
        start()

def start():
    print("[1] Shop\n[2] Level Select\n[3] Credits")
    choice = int(input("Please select one: "))
    if choice == 1:
        shop()
    elif choice == 2:
        levelSelect()
    elif choice == 3:
        credit()
