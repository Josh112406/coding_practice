#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = []
for i in range(1, 11): #used range(1,11) instead of range(10) so that the number starts with 1
    numbers += [float(input(f"Enter number {i}: "))]
    
print(numbers[0] - sum(numbers[1:]))
