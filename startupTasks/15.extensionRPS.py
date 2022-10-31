# Write a program that plays rock, paper, scissors. 
# It will take a user input of “R”, “P” or “S”, the 
# computer will randomly generate it’s move and then 
# tell you whether you have won or lost. 
# Hint: This is tricky! You can use nested if statements.

userInput = input("Enter, in the form R:P, player 1 and 2's moves:   ")
p1 = userInput[0:1]
p2 = userInput[2:3]

print(p1)
print(p2)

if p1 == "R":
    if p2 == "P":
        print("Player 2 wins")
    # End if
    if p2 == "S":
        print("Player 1 wins")
    # End if
    if p2 == "R":
        print("Nobody wins")
    # End if
# End if
if p1 == "P":
    if p2 == "P":
        print("Nobody wins")
    # End if
    if p2 == "S":
        print("Player 2 wins")
    # End if
    if p2 == "R":
        print("Player 1 wins")
    # End if
# End if
if p1 == "S":
    if p2 == "P":
        print("Player 2 wins")
    # End if
    if p2 == "S":
        print("Nobody wins")
    # End if
    if p2 == "R":
        print("Player 1 wins")
    # End if
# End if
