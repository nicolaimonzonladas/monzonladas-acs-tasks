nums = [10,23,51,7,2] # initialize a list of numbers

print(nums) # print the initial list of numbers

for i in range(len(nums)): # loop through the numbers in the list
    for j in range(len(nums)-i-1): # compare each number to the numbers that come after it
        if nums[j] > nums[j + 1]: # if the current number is greater than the number that comes after it
            nums[j],nums[j + 1] = nums[j + 1],nums[j] # swap the positions of the two numbers
            print(nums) # print the updated list of numbers after each swap