#Prompts user for integer and inputs it.
print("Input your integer:")
userInteger = int(input())

#Prompts user for divisor and inputs it.
print("Input your divisor:")
userDivisor = int(input())


#Calculates the whole integer devision and the remainder.
divisor, mod = divmod(userInteger, userDivisor)

#Prints output
print(divisor, " remainder ", mod)


