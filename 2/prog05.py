#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
#almost same as prog03 and prog04

num = float(input("Enter first number: "))
num %= float(input("Enter second number: "))
print(f"The remainder of the two numbers is: {num}")