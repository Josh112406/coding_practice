#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

count = 0
for i in range(1, 11): #used range(1,11) instead of range(10) so that the number starts with 1
    num = int(input(f"Enter number {i}: "))
    if num % 2 == 0:
        count += 1
        
print(f"Even number count: {count}")