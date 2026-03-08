#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
print(num_1 if num_1 < num_2 else num_2)