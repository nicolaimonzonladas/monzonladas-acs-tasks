# Input user's number
integer = int(input("Enter your number: "))
# Create list for correct factors
factors = []

# For loop to loop through i to the integer, checks if divisible, 
# adds to factors[] if a factor
for i in range(1,integer + 1):
    if integer%i == 0:
        factors.append(i)
    # End if
# End for

# Print factors
print("Factors of ", integer, " are ", factors)