nums = [10,23,51,7,2]

print(nums)

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j + 1]:
            nums[j],nums[j + 1] = nums[j + 1],nums[j]
            print(nums)
