import random

numbers = [15, 73, 29, 66, 35, 11, 43, 21]

print(numbers)

testing = []

for k in range(1,10000):
    testing.append(random.randrange(-10,10))
    



def insertionSort(nums):
    for i in range(1,len(nums)):
        nextItem = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > nextItem:
            nums[j+1] = nums[j]
            j = j - 1 
        nums[j+1] = nextItem
        print(nums)

insertionSort(testing)

# insertionSort(numbers)

# #ORIGINAL: [15, 73, 29, 66, 35, 11, 43, 21]
# 1 [15, 73, 29, 66, 35, 11, 43, 21]
# 2 [15, 29, 73, 66, 35, 11, 43, 21]
# 3 [15, 29, 66, 73, 35, 11, 43, 21]
# 4 [15, 29, 35, 66, 73, 11, 43, 21]
# 5 [11, 15, 29, 35, 66, 73, 43, 21]
# 6 [11, 15, 29, 35, 43, 66, 73, 21]
# 7 [11, 15, 21, 29, 35, 43, 66, 73]
# FINAL: [11, 15, 21, 29, 35, 43, 66, 73]