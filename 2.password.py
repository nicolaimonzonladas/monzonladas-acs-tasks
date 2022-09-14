#While loop to loop forever
while True:
    #Prompt to ask for password input
    print("Input your password:")
    #Input password 
    password = input()
    #If statement to check length of password is greater than 6 characters.
    if len(password) > 6:
        print("Password is valid")
    else:
        print("Password is invalid")
    #end if
#end while.

