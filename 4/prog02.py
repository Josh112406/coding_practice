# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

nums = []
duplicates = {}
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except ValueError:
        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates[nums[i]] = 1
            else:
                duplicates[nums[i]] = duplicates[nums[i]] + 1                
        break
print(f"Number with most duplicate is: {max(duplicates, key=duplicates.get)}")