#Prompts and asks for user input
print("Enter an integer between 100 and 999")
#Input user's number
userNum = input()
#Prints 
print(userNum[0:1:] + " hundreds, " + userNum[1:2:] + " tens, and " + userNum[2:3] + " units.")