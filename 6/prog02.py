# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#same logic as prog01 but change in output

nums = []
duplicates = {}
for i in range(10):
    nums += [float(input(f"Enter number {i + 1}: "))]
    if nums[i] not in duplicates:
        duplicates[nums[i]] = 1
    else:
        duplicates[nums[i]] = duplicates[nums[i]] + 1                

print(f"First entry of duplicate is: {max(duplicates, key=duplicates.get)}")