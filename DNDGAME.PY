import os 
import random
import sys
 #universal functions refrencing imports
def clear_terminal():
    os.system('cls' if os.name == 'nt' 
    else 'clear')
    
def restart_program():
    python = sys.executable
    os.execl(python, python,
*sys.argv)
 
 #universal variables   
charecter1 = "wizard"
charecter2 = "knight"
charecter3 = "thief"
charecter4 = "assassin"
charecter5 = "orc"
charecter6 = "dragonite"
dice_value = 0

#stats can be improved later for all charecters individually
stats = {
    "health": 100,
    "defense": 75,
    "attack": 50  
}

#dice rolling
def roll_dice():
    return random.randint(1, 6)
dice_value = roll_dice()

#game loop begins
clear_terminal()
print("You've been sent from your home town in Riverdale to Anastasia.")
print("The local Adventurers Guild has requested you to take care of a little problem..")
user_input = input("Enter 'c' to continue")
if user_input == "c":
 clear_terminal()
 
print ("Hello weary Adventurer! You must be the one they sent from Riverdale...")
print("You're not the usual guy we hire... well anyway, ")
print("What's you're name?")
name = input()
clear_terminal()

print ("Welcome: "+name)
print("We have a gold level mission: Take care of the goblin in the mountains.")
user_input = input("Enter 'r' to roll your CHARACRTER")
if user_input == "r":
        dice_value
clear_terminal()

#assigning te player a charecter based on dice_value
print("You have rolled: " +str(dice_value))

if dice_value == 1:
    print("YOU ARE A "+charecter1)
elif dice_value == 2:
    print("YOU ARE A " +charecter2)
elif dice_value == 3:
    print("YOU ARE A " +charecter3)
elif dice_value == 4:
    print("YOU ARE A " +charecter4)
elif dice_value == 5:
    print("YOU ARE A " +charecter5)
else :
    print("YOU ARE A " +charecter6)

user_input = input("Enter 'r' to roll your STATS")
clear_terminal()
if user_input == "r": 
    print(f"stats: {stats['health']}")
    print(f"stats: {stats['defense']}")
    print(f"stats: {stats['attack']}")
    
user_input = input("Lets begin your journey! Enter 'c' to begin")
clear_terminal()
if user_input == "c":
 print("You've traveled far across the plains of Anastasia.")
 print("You've come across a dreary cave titled: Goblins Den")
else : print("You must enter c")

user_input = input("Enter 'c' to enter the cave")
clear_terminal
if user_input == "c":
 print("After walking some distance, The Goblin appears!")
 print("The path back is too far...")
else : print("You must enter c")

user_input = input("You must ATTACK! Enter 'r' to determine your outcome")
if user_input == "r":
        dice_value = random.randint(1, 6)
clear_terminal()
print("You have rolled: " +str(dice_value))  
if dice_value == 1:
    print("You did little damage.. the goblin Kills you")
elif dice_value == 2:
    print("You did little damage.. the goblin Kills you")
elif dice_value == 3:
    print("You did little damage.. the goblin Kills you")
elif dice_value == 4:
    print("CRITICAL ATTACK! YOU KILLED THE GOBLIN! You are the champion of anastasia..")
elif dice_value == 5:
    print("CRITICAL ATTACK! YOU KILLED THE GOBLIN! You are the champion of anastasia..")
elif dice_value == 6:
    print("CRITICAL ATTACK! YOU KILLED THE GOBLIN! You are the champion of anastasia..")
    
user_input = input("Enter 's' to Restart!")
if user_input == 's':
   restart_program()
     