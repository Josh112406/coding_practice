# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
num = 0
for i in range(1, 11): #used range(1,11) instead of range(10) so that the number starts with 1
    num += float(input(f"Enter number {i}: "))
    
print(f"The sum of all the numbers is: {num}")