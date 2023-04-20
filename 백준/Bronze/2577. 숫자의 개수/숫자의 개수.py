nums = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

total = 1 
for _ in range(3): 
    total *= int(input())

for i in str(total): 
    nums[i] += 1 

for num in nums: 
    print(nums[num])