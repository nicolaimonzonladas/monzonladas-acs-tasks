# Input plain text code to be encrypted, split
plainText = list(input("Enter your code to be encrypted:  "))
# Input shift
shift = int(input("Enter your desired shift for encryption:   "))

# Output string
encrypted = ""

# For loop to go through length of plain text,
for i in range(len(plainText)):
    if plainText[i].isalpha(): # Checks if the character is a letter
        ord_value = ord(plainText[i]) # Converts to ASCII
        cipherValue = ord_value + shift # Shifts the ASCII value by the shift
        if cipherValue > ord('z'):
            cipherValue -= 26 # For case of going above a-z in ASCII values, goes back 1 alphabet length
        # End if
        encrypted += (chr(cipherValue))
    else:
        encrypted += (plainText[i]) # If the character is not a letter, appends to the string
    # End if

# Print encrypted data
print(encrypted)