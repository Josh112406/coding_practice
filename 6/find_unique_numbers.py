# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

duplicates = {}
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num not in duplicates:
        duplicates[num] = 1
    else:
        duplicates[num] = duplicates[num] + 1                

print(f"Numbers without duplicates are: {[key for key, value in duplicates.items() if value == 1]}")