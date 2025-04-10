print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("😎   //Welcome to Treasure Island//  😎")

print("Your mission is to find the treasure.(Khajana) 💀💀💀 ")

print("You have two Options  ")

Dir=str(input("Tell me in which direction you want to go ?? Left or Right \n Choose wisely  💀💀💀 !!  ").lower())

if  Dir=="left":
    print("That's a gr8 choice , You are a master \n Now give me answer of next question ")
    Do=str(input("Tell me , Are you Good at Swimming ?? if yes then type swim or else wait ").lower())

    if  Do=="wait":
        print("\nYou come across three mysterious doors...")
        print("🔴 Red: The Door of #BLOOD#")
        print("🟡 Yellow: The Door of #HEAT#")
        print("🔵 Blue: The Door of #WATER#")
        door = input("\n Which door do you choose? (Red / Yellow / Blue): ").lower()

        if  door=="red":
            print("Best choice nhi hai bhai firse khel  !!")
            print("Burned by fire Game over!!")

        elif door=="blue":
            print("You are Born Loser ")
            print("Eaten by beasts Game over !!")

        elif door=="yellow":
            print("Bravoo!! 🏆🏆🏆🏆 ")
            print("Congo!! You Win !! 🏆🏆🏆🏆")

        else:
            print("Game over ")

    else:
        print("Fantastic !! Do Swimming !! Game over !!")

else:
    print("You are not Right this time!! 💀💀💀")
    print("Fall into a hole ! Game over !!")