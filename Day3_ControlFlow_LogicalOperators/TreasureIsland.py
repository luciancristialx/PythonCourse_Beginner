#You're at a cross road. Where do you want to go? Type "left" or "rigth"
#You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to
# swim across.
#You arrive at the island unharmed. There is a house with 3 doors. Onre red, one yellow and one blue. Which color do
# you chosse?

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

question_1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if question_1 == "left":
    question_2 = input("You arrive to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across!\n").lower()
    if question_2 == "wait":
        question_3 = input("You arrive on the island and found 3 houses. Type 'red' to enter red house; Type 'blue' "
                           "to enter blue house; Type 'yellow' to enter yellow house.\n").lower()
        if question_3 == "yellow":
            print("You chose the winning path! YOU WON!")
        elif question_3 == "blue":
            print("The house was hiding criminals! Game over!")
        elif question_3 == "red":
            print("The house is a bear shelter! Game over!")
        else:
            print("Game over!")
    else:
        print("You got an infection, and died while swimming!\nGame over!")
else:
    print("Game over! You have been eaten!\nGame over!")