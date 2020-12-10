# Author:  Fardeen Yaqub
# Date:    10/19/18
# Description:
#   The program puts the user in a game where they are stuck in the woods with a monster chasing them. They user must survive 7 days or travel 150 miles
#   in order to beat the game. Throughout the game the user will be faced with random events that can give the user items or food or force the user to
#   fight the monster. If the user's health drops to 0 they lose the game. The user progresses throught the game by selecting the options shown on screen


##################################
#### DO NOT TOUCH THESE LINES ####
from random import randint, seed #
seed(100)                        #
##################################

#constants for player and monster health
MAX_HEALTH = 100
MIN_HEALTH = 0

DEM_MAX_HEALTH = 300

#constants for survival
SURVIVE_DAYS = 7
SURVIVE_DIST = 150

#constant lists of food and items
FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]
ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys","Walkman", "Laser Cannon", "Rubber Band"]


#constant list for menus
DAILY_CHOICES = ["View Inventory", "View Current Stats", "Eat an Eggo Waffle", "Nothing Else"]
INVENTORY_CHOICES = ["Equip", "Unequip", "I changed my mind"]
MOVEMENT_CHOICES = ["Pack up camp and go","Stay where you are"]
FOOD_CHOICES = ["Eat it","Put it back"]
FIGHT_CHOICES = ["Fight","Flail","Flee"]


# getUserChoice() asks the user to select a choice from a list of choices
#                 continuously prompts the user until the choice is valid
#                 a valid choice is one that is a valid index in the list
# Input:          choices; a list of all the possible choices available
# Output:         choice; the validated int choice that the user made
def getUserChoice(choices):

    userChoice = input("Enter a choice: ")
    flag = False

    #Prompts user to enter a choice until they enter a valid option
    while flag == False:

        #User enters invalid choice
        if int(userChoice) < 0 or int(userChoice) > len(choices):
            print("Invalid input")
            userChoice = input("Enter a choice: ")

        #User enters a valid choice
        else:
            flag = True
            return int(userChoice)

        
#displayMenu()   displays a menu based on the menu list; string menu
#Input:          choices; no return
#Output:
def displayMenu(options):
    count = 0

    print("Your options are:")
    while count < len(options):
        print(count+1,"-",options[count])
        count += 1

        
# calcDamage()    takes the user's current equipped weapon and calculates
#                 the amount of damage the weapon can do; a string that
# Input:          has the name of the user's equipped weapon; the integer
# Output:         amount of damage the weapon can do
def calcDamage(weapon):

    damage = 0
    #user has Flashlight equipped
    if weapon == "Flashlight":
        damage = 5
    #user has Walkie Talkie equipped
    elif weapon == "Walkie Talkie":
        damage = 10
    #user has Rubber Band equipped
    elif weapon == "Rubber Band":
        damage = 25
    #user has Sword equipped
    elif weapon == "Sword":
        damage = 50
    #user has Laser Cannon equipped
    elif weapon == "Laser Cannon":
        damage = 100

    return damage


# eatFood()       takes a list of foods and compares it to the food parameter
#                 to calculate the health increase or decrease that the
# Input:          food offers; the string food; the health increase
# Output:         or decrease the food gives as an int
def eatFood(food,player_health):

    userHealth = player_health
    
    #User finds Reese's pieces in backpack
    if food == FOODS[0]:
        userHealth -= 30
        print("You ate the",food)
        print("You suddenly remember you're allergic to peanut butter")
        
    #User finds Pop Rocks in backpack
    elif food == FOODS[1]:
        userHealth -= 5
        print("You ate the",food)
        print("The popping sound gives you a headache")
        
    #User finds Ovaltine is backpack
    elif food == FOODS[2]:
        userHealth += 15
        print("You ate the",food)
        print("The taste of",food,"puts your mind at ease")
        
    #User finds Wonder Bread in backpack
    elif food == FOODS[3]:
        userHealth += 25
        print("You ate the",food)
        print("The magical power of bread is awesome")
        
    #User finds Twinkies in backpack
    elif food == FOODS[4]:
        userHealth += 30
        print("You ate the",food)
        print(food,"are your favorite snack")

    #User eats an Eggo Waffle
    elif food == "Eggo Waffle":
        userHealth += 10
        print("You ate the",food)
        print("So bad yet, so good")
        
    #User already had 100 health
    if player_health == 100 and userHealth > 100:
        print("Your health has increased by 0 points. You already had full health")
        return player_health

    #User health remains under 100
    elif userHealth < MAX_HEALTH:

        #Food chosen increases health
        if player_health < userHealth:
            print("Your health has increased by",userHealth-player_health,"points")

        #Food chosen decreases health
        elif player_health > userHealth:
            print("Your health has decreased by",userHealth-player_health,"points")

    #User health goes over 100
    elif userHealth >= MAX_HEALTH:
        print("Your health has increased by", MAX_HEALTH - player_health,"points. Your health is now full")
        userHealth = MAX_HEALTH

    return userHealth


# fightMonster()  prompts the user to fight, flail, or flee until the user's
#                 health is 0, the monster's health is 0, or the user is able
#                 to flee. If the user has a specific item in their inventory
#                 they are able to affect the monster's stats. If user dies they
#                 are told game over; player's health(int),equipped weapon(string)
# Input:          ,and user's inventory(list); player's remaining health as an
# Output:         integer
def fightMonster(player_health, item, inventory):

    playerHealth = player_health
    weapon = item
    damage = calcDamage(weapon)

    #User has Hi-C in their inventory. Halves the monster's health
    if "Hi-C" in inventory:
        monsterHealth = DEM_MAX_HEALTH/2

    #Uesr does not have Hi-C in their inventory
    else:
        monsterHealth = DEM_MAX_HEALTH

    #User has Walkman in their inventory. Halves the monster's attack
    if "Walkman" in inventory:
        monsterDamage = 20 -(20*.25)

    #User does not have Walkman in their inventory
    else:
        monsterDamage = 20
        
    print("The Demogorgon appears in front of you.")
    print("Its face opens up like a flower to display rows and rows of teeth. It came here for a fight.")
    print()

    #Runs while the player or the monster don't have 0 health
    while playerHealth != 0 and monsterHealth !=0:
        print("Your health:",playerHealth)
        print("Monster health:", monsterHealth)
        print()

        print("What do you do now?")
        print()

        displayMenu(FIGHT_CHOICES)
        userChoice = getUserChoice(FIGHT_CHOICES)
        print()

        #User chooses to attack
        if userChoice == 1:
            #User does not have a weapon
            if weapon == "N/A":
                print("You strike the Demogorgon with your fists but it dodges your attack")
            #User attacks with a weapon
            else:
                print("You strike the Demogorgon with your",weapon,"for",damage,"damage")
                monsterHealth -= damage

            if monsterHealth != 0:
                print("The Demogorgon strikes you back for",monsterDamage,"damage")
                playerHealth -= monsterDamage

        #User chooses to flail
        if userChoice == 2:
            print("You flail around in an attempt to scare off the monster but your results are similar to those of a Magikarp's")
            print("The monster devours you")
            print("Game Over")
            playerHealth = 0
            return playerHealth

        #User chooses to run
        elif userChoice == 3:
            num = randint(1,10)

            #User is able to run away
            if num <=3:
                print("You try to run away from the fight. You are successful, and you live to die another day.")
                return playerHealth

            #User is not able to run away
            else:
                print("You try to run away from the fight. The monster blocks your path, preventing you from running away")
                print("The Demogorgon strikes you back for",monsterDamage/2,"damage")
                playerHealth -= monsterDamage/2

    #User defeats monster monster
    if monsterHealth == 0:
        print("You managed to force the beast to retreat. It leaves you alone for now, letting you live for another day")

    #User loses all their health
    elif playerHealth == 0:
        print("The beast overpowers you and you fall to your knees in defeat")
        print("The monster devours you")
        print("Game Over")

    return playerHealth


# backpackEvent() user finds a random food item and are given the option to eat
#                 or not eat the food.; player's current health(int);player's
# Input:          health after the food's effect(int)
# Output:
def backpackEvent(health):

    userHealth = health
    num = randint(0,len(FOODS)-1)
    
    print("As you were walking, you found a backpack.")
    print("Inside the backpack, there was some", FOODS[num])
    print("Do you want to eat it")

    displayMenu(FOOD_CHOICES)
    userInput = getUserChoice(FOOD_CHOICES)

    #User chooses to eat the food he found
    if userInput == 1:
        userHealth = eatFood(FOODS[num],userHealth)
        return userHealth
        
    #User chooses not to eat food
    elif userInput == 2:
        print("You didn't eat the",FOODS[num])
        return userHealth
            
    
# shedEvent()     user finds a random item from the item list; no input;
# Input:          the item the user found (string)
# Output:
def shedEvent():

    num = randint(0,len(ITEMS)-1)
    print()
    print("You pass by an old shed and decide to go inside. Something on the shelf catches your eye.")
    print("You reach up to the item. It's a",ITEMS[num])
    print("The", ITEMS[num], "has been added to your inventory")

    return ITEMS[num]


# trenchEvent()   The user's movement is halved for that day; user's health(int)
# Input()         and inventory(list); the distance the user traveled(float)
# Output()
def trenchEvent(health,inventory):
    print("You fell into a trench because you weren't paying attention to where you were stepping.")
    print("It takes you a whole extra day to climb out.")
    
    userHealth = health
    trenchDistance = travelDistance(userHealth,inventory) / 2
    return float(trenchDistance)


# displayStats()  Displays the user's health, distance traveled, and
# Input()         equipped item; user's health(int), distance traveled(float),
# Output()        and equipped item(string); no return
def displayStats(health, distance, item):
    print()
    print("Health:",health)
    print("Distance traveled:",distance,"miles")
    print("Equipped item:",item)

    
# viewInventory() the user's inventory is displayed and they can choose to equip
# Input()         or unequip an item or exit the menu; the user's inventory(list)
# Output()        and the user's current equipped item(string); the new item the
#                 user has equipped(string)
def viewInventory(inventory,item):

    userItem = item
    print()
    print("Here is what your inventory looks like:")
    print(inventory)
    print()

    #User does not have an item equipped
    if userItem == "N/A":
        print("Do you want to equip an item?")

    #User has a weapon equipped
    else:
        print("Do you want to change your equipped item?")
        print()

    displayMenu(INVENTORY_CHOICES)
    userChoice = getUserChoice(INVENTORY_CHOICES)

    #User chooses to equip an item
    if userChoice == 1:
        print()
        displayMenu(inventory)
        userChoice = getUserChoice(inventory)
        print("You have equipped",inventory[userChoice-1])

        return inventory[userChoice-1]
              
    #User chooses to unequip an item
    elif userChoice == 2:
        print()
        #User doesn't have an item equipped
        if userItem == "N/A":
            print("You don't have an equipped item to unequip")

        #User unequips an item
        else:
            print("You have unequipped your item")
        return "N/A"

    #User chooses not to equip or unequip
    elif userChoice == 3:
        print()
        print("OK, that's fine.")
        return userItem
            

# travelDistance() calculates the distance the user travels based on their health
# Input()          and items in their inventor; user's health(int) and user's
# Output()         inventory(list); the distance the user traveled(float)
def travelDistance(health, inventory):

    #User has Heelys and Bicycle in inventory
    if "Heelys" in inventory and "Bicycle" in inventory:
        print("The Bicycle you found helped improve your distance traveled")
        userDistance = ((health/4)+5) * 1.5

    #User has bicycle in inventory
    elif "Bicycle" in inventory:
        print("The Bicycle you found helped improve your distance traveled")
        userDistance = ((health/4)+5) * 1.5

    #User has heelys in inventory    
    elif "Heelys" in inventory:
        print("The Heelys you found helped improve your distance traveled")
        userDistance = ((health/4)+5) * 1.25

    #User has no movement items in inventory
    else:
        userDistance = (health/4) + 5 

    return userDistance


def main():
    
    print("After miles and miles of hiking in the woods, you finally setup your camp.")
    print("You decide to go camping on the wrong weekend.")
    print("Your phone buzzes: THE DEMOGORON HAS ESCAPED.               RUN.")
    
    userHealth = MAX_HEALTH
    userDistance = 0
    userDays = 1
    userEquippedItem = "N/A"
    userChoice = 0
    userInventory = ["Walkie Talkie","Flashlight"]
    
    # while the player isn't dead and hasn't made it far enough and hasn't survived long enough
    while userHealth > MIN_HEALTH and userDistance < SURVIVE_DIST and userDays < SURVIVE_DAYS:
        print()
        print("The sun rises on the DAY", userDays,"in the forest.")
        print()
        print("What would you like to do this morning?")
        print()


        # perform the daily tasks
        displayMenu(DAILY_CHOICES)
        userChoice = getUserChoice(DAILY_CHOICES)

        flag = True
        #Runs as long as the user doesn't enter 4 
        while userChoice != 4:

            #user chooses to view Inventory
            if userChoice == 1:
                userEquippedItem = viewInventory(userInventory,userEquippedItem)

                print()
                print("What else would you like to do this morning?")
                print()

                displayMenu(DAILY_CHOICES)
                userChoice = getUserChoice(DAILY_CHOICES)
                

            #user chooses to view stats
            elif userChoice == 2:
                displayStats(userHealth,userDistance,userEquippedItem)

                print()
                print("What else would you like to do this morning?")
                print()

                displayMenu(DAILY_CHOICES)
                userChoice = getUserChoice(DAILY_CHOICES)

            #user eats an Eggo Waffle
            elif userChoice == 3:
                
                #User already ate Eggo Waffle for the day
                if not flag:
                    print("You can only eat an Eggo Waffle once a day")

                #User eats an Eggo Waffle
                else:
                    userHealth = eatFood("Eggo Waffle",userHealth)
                    flag = False

                print()
                print("What else would you like to do this morning?")
                print()

                displayMenu(DAILY_CHOICES)
                userChoice = getUserChoice(DAILY_CHOICES)


        print()
        print("The Demogorgon looms in the distance. Do you leave your camp, or do you stay?")
        print()

        displayMenu(MOVEMENT_CHOICES)
        userChoice = getUserChoice(MOVEMENT_CHOICES)

        #Generates random number from 1-10
        num = randint(1,10)
        
        #User chooses to leave camp
        if userChoice == 1:
            print()
            print("You quickly pack up your camp.")
            print("You begin heading in the direction of the nearest town.")
            print()

            #Backpack event runs
            if num == 1 or num == 2:
                userDistance += travelDistance(userHealth,userInventory)
                userHealth = backpackEvent(userHealth)
                userDays +=1

            #Shed event runs
            elif num == 3 or num == 4:
               userInventory.append(shedEvent())
               userDays +=1

            #Trench events run
            elif num == 5 or num == 6:
                
                userDistance += trenchEvent(userHealth,userInventory)
                userDays +=2

            #Battle event runs
            elif num >=7 or num <=9:
                userDistance += travelDistance(userHealth,userInventory)
                userHealth = fightMonster(userHealth,userEquippedItem,userInventory)
                userDays +=1

            #Nothing happens for the day
            else:
                print("Nothing happened today but at least you're still alive")
                userDays += 1 

            #Trench event, monster event, and backpack event does not run and user isn't dead so user travels normally
            if (num <= 4 or num >= 10) and (num !=1 and num != 2) and userHealth != 0:
                userDistance += travelDistance(userHealth,userInventory)

            if userHealth != 0:
                print()
                print("You have now traveled",userDistance,"miles")

        #User chooses to stay at camp
        elif userChoice == 2:

            #User fights monster
            if num <= 7:
                userHealth = fightMonster(userHealth, userEquippedItem, userInventory)
                userDays += 1

            #User rests at camp
            else:
                userHealth = MAX_HEALTH
                print("You get to rest at camp and restore your health")
                userDays += 1

    #User survives with more than 0 health
    if userHealth != 0:
        print()
        print("Congratulations!")
        print("You made it to civilization alive.")

        #User lives for 7 days
        if userDays > 7:
            print("It took 7 days to go",userDistance,"miles")

        #User manages to travel required distance in less than 7 days
        else:
            print("It took",userDays,"days to go",userDistance,"miles")

        print()

    print("Final Stats:")
    displayStats(userHealth,userDistance,userEquippedItem)
    
main()

