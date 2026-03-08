#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

#shorter version
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
print(f"The smaller number is: {num_1 if num_1 < num_2 else num_2}")

#longer version
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
if num_1 < num_2:
    print(f"The smaller number is: {num_1}")
else:
    print(f"The smaller number is: {num_2}")