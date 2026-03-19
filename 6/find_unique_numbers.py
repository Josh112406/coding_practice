# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

nums = []
duplicates = {}
for i in range(10):
    nums.append(float(input(f"Enter number {i + 1}: ")))
    if nums[i] not in duplicates:
        duplicates[nums[i]] = 1
    else:
        duplicates[nums[i]] = duplicates[nums[i]] + 1                

print(f"Numbers without duplicates are: {[key for key, value in duplicates.items() if value == 1]}")