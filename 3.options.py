#Set temporary variable
blahblah = 0

#While loop, ending when a valid number is inputted.
while blahblah == 0:
    #Prompts and inputs, converts str input to int variable type
    print("Enter a number between 1 and 3:")
    inputtedNumber = int(input())

    #If statement, to check input is between 1 and 3
    if inputtedNumber >= 1 and inputtedNumber <= 3:
        #If input is valid, sets temporary variable to 1 to exit the main while loop,
        #prints selected option
        blahblah = 1
        print("You have selected option number " + str(inputtedNumber) + ".")
    else:
        #Reprompts to enter again if input is not valid
        print("Enter again (from 1-3).")
    #end if
#end while.

