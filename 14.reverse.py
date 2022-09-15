# Inputs user word to reverse, converts to list
# Creates output string
reverse = list(input("Enter your word to reverse:   "))
reversed = ""

# Iterates from end to start of inputted list backwards, 
# adds to output string
for i in range(len(reverse)-1, -1, -1):
    reversed += reverse[i]
# End for

# Prints output
print(reversed)