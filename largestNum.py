nums = [34,45,23,68,13]

largest_num = nums[0]

for i in range(len(nums)):
    if nums[i] > largest_num: 
        largest_num = nums[i]


print(f"The Largest number is {largest_num}")